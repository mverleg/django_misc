
"""
	middleware to redirect certain parts of the site to https
	http://www.redrobotstudios.com/blog/2010/02/06/requiring-https-for-certain-paths-in-django/
	alternative to decorators, and the only way for admin and external apps
"""

from django.conf import settings
from misc.functions.secure import secure_redirect


class RequireSecureMiddleware(object):
	def process_request(self, request):
		if getattr(settings, 'AUTH_REQUIRE_SECURE') and not request.is_secure():
			for path in getattr(settings, 'REQUIRE_SECURE_PATHS'):
				if request.get_full_path().startswith(path):
					return secure_redirect(request)
		return None


