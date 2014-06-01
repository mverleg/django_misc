
from django.http import HttpResponseRedirect
import settings


'''
	turns a request into a securified redirect
'''
def secure_redirect(request, url = None):
	if url is None:
		url = request.build_absolute_uri(request.get_full_path())
	url = request.build_absolute_uri(url)
	url = url.replace('http://', 'https://')
	if settings.DEBUG:
		url = url.replace(':8000/', ':8443/')
	return HttpResponseRedirect(url)

def desecure_redirect(request, url = None):
	if url is None:
		url = request.get_full_path()
	url = request.build_absolute_uri(url)
	url = url.replace('https://', 'http://')
	if settings.DEBUG:
		url = url.replace(':8443/', ':8000/')
	print url
	return HttpResponseRedirect(url)
