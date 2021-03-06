
"""
	decorator makes the page redirect to https if the connection is not secure.
	credits go to http://www.redrobotstudios.com/blog/2009/02/18/securing-django-with-ssl/
	note that this is still not very secure if you allow sending session cookies over http
"""

from django.conf import settings

from misc.functions.secure import secure_redirect


def redirect_to_secure(view_func):
	"""
		always redirect to https if on http
	"""
	def guarantee_secure_view(request, *args, **kwargs):
		if not request.is_secure():
			return secure_redirect(request)
		return view_func(request, *args, **kwargs)
	return guarantee_secure_view


def conditional_redirect_to_secure(view_func):
	"""
		redirect to https if on http and the settings say so
	"""
	def guarantee_secure_view(request, *args, **kwargs):
		if not request.is_secure():
			if getattr(settings, 'AUTH_REQUIRE_SECURE', False):
				return secure_redirect(request)
		return view_func(request, *args, **kwargs)
	return guarantee_secure_view


secure = conditional_redirect_to_secure


