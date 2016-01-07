
"""
	Some default settings and settings related to misc features.
"""


BASE_TEMPLATE = 'base.html'
BASE_EMAIL_TEMPLATE = 'base_email.html'

PREPEND_WWW = False   # stripping middleware active
APPEND_SLASH = False  # stripping middleware active

LANGUAGE_CODE = 'en'

MEDIA_URL = '/media/'
STATIC_URL = '/static/'

# https://docs.djangoproject.com/en/1.7/ref/templates/builtins/#std:templatefilter-date
DATE_FORMAT = 'b jS Y'
TIME_FORMAT = 'G:i:s'
DATETIME_FORMAT = '{0:s} {1:s}'.format(DATE_FORMAT, TIME_FORMAT)

STATICFILES_DIRS = []

HAYSTACK_CONNECTIONS = {
	'default': {
		'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
		'URL': 'http://127.0.0.1:9200/',
		'INDEX_NAME': 'haystack',
	},
}
HAYSTACK_ITERATOR_LOAD_PER_QUERY = HAYSTACK_SEARCH_RESULTS_PER_PAGE = 20
HAYSTACK_LIMIT_TO_REGISTERED_MODELS = True
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

CRISPY_TEMPLATE_PACK = 'bootstrap3'


