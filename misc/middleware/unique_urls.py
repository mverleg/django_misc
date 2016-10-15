
from django.conf import settings
from django.core.urlresolvers import resolve, Resolver404

assert not getattr(settings, 'PREPEND_WWW', False), \
	'the setting PREPEND_WWW cannot be true when RemoveWWW middleware is enabled'


class RemoveWwwMiddleware():
	"""
		Opposite of PREPEND_WWW (this will apparently never be added to Django).

		Largely from https://gist.github.com/dryan/290771
	"""
	def process_request(self, request):
		if request.META['HTTP_HOST'].lower().find('www.') == 0:
			from django.http import HttpResponsePermanentRedirect
			return HttpResponsePermanentRedirect(request.build_absolute_uri().replace('//www.', '//'))


class RemoveSlashMiddleware():
	"""
		Opposite of APPEND_SLASH.
	"""
	def process_request(self, request):
		url = request.path
		if url.endswith('/'):
			try:
				# use full path here instead of absolute uri; resolve doesn't handle domain names
				resolve(url[:-1])
			except Resolver404:
				""" Version without / at the end doesn't exist - do not redirect. """
			else:
				from django.http import HttpResponsePermanentRedirect
				get = request.GET.urlencode()
				return HttpResponsePermanentRedirect(url[:-1] + ('?{0:s}'.format(get) if get else ''))


class WwwSlashMiddleware():
	"""
		Combination of RemoveWwwMiddleware and AppendSlashMiddleware
	"""
	def process_request(self, request):
		original = request.build_absolute_uri()
		nw = original.replace('//www.', '//')
		if nw.endswith('/'):
			try:
				# use full path here instead of absolute uri; resolve doesn't handle domain names
				resolve(request.get_full_path()[:-1])
			except Resolver404:
				""" Version without / at the end doesn't exist - do not redirect. """
			else:
				nw = nw[:-1]
		else:
			try:
				resolve(request.get_full_path())
			except Resolver404:
				try:
					# use full path here instead of absolute uri; resolve doesn't handle domain names
					resolve(request.get_full_path() + '/')
				except Resolver404:
					""" Current version and version witg / at the end both don't exist - do not redirect. """
				else:
					nw = nw + '/'
			else:
				""" Version without slash exists, don't add it back! """
		if not original == nw:
			from django.http import HttpResponsePermanentRedirect
			return HttpResponsePermanentRedirect(nw)


