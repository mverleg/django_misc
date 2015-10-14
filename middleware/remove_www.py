
from django.conf import settings


assert not getattr(settings, 'PREPEND_WWW', False), \
	'the setting PREPEND_WWW cannot be true when RemoveWWW middleware is enabled'


class RemoveWwwMiddleware():
	"""
		Opposite of PREPEND_WWW, which will apparently never be added to Django.

		Largely from https://gist.github.com/dryan/290771
	"""
	def process_request(self, request):
		try:
			if request.META['HTTP_HOST'].lower().find('www.') == 0:
				from django.http import HttpResponsePermanentRedirect
				return HttpResponsePermanentRedirect(request.build_absolute_uri().replace('//www.', '//'))
		except:
			pass


