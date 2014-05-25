
import settings
from misc.functions.obfuscate import ENCCHARS


def datetime_py_to_js(pyformat):
	return pyformat.replace('%Y', 'YYYY').replace('%y', 'YY').replace('%m', 'MM').replace('%d', 'DD').replace('%H', 'HH').replace('%M', 'mm').replace('%S', 'SS')


'''
	put some settings into javascript
'''
def javascript_settings(request):
	return {'BASE_JS_SETTINGS': {
		'DATETIME_INPUT_FORMAT': datetime_py_to_js(settings.DATETIME_INPUT_FORMATS[0]),
		'DATE_INPUT_FORMAT':     datetime_py_to_js(settings.DATE_INPUT_FORMATS[0]),
		'TIME_INPUT_FORMAT':     datetime_py_to_js(settings.TIME_INPUT_FORMATS[0]),
		'ENCCHARS':              ENCCHARS,
	}}


