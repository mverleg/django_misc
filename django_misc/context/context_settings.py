
import settings


'''
	put some settings into the default context
'''
def context_settings(request):
	return {
		'SITE_URL':             settings.SITE_URL,
		'BASE_TEMPLATE':        settings.BASE_TEMPLATE,
		'BASE_EMAIL_TEMPLATE':  settings.BASE_EMAIL_TEMPLATE,
		'USE_CDN':              settings.USE_CDN,
		#'AUTH_REQUIRE_SECURE':  settings.AUTH_REQUIRE_SECURE,
	}


