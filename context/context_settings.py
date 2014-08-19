
import settings


def context_settings(request):
	"""
		put some settings into the default context
	"""
	return {
		'SITE_URL':             settings.SITE_URL.rstrip('/'),
		'BASE_TEMPLATE':        settings.BASE_TEMPLATE,
		'BASE_EMAIL_TEMPLATE':  settings.BASE_EMAIL_TEMPLATE,
		'USE_CDN':              settings.USE_CDN,
		#'AUTH_REQUIRE_SECURE':  settings.AUTH_REQUIRE_SECURE,
	}


