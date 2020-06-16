
from genericpath import exists
from os.path import basename, getsize

from django.conf import settings
from django.http import HttpResponse


def serve_file(pth, filename=None, content_type='application/octet-stream'):
	if not exists(pth):
		raise FileNotFoundError('file "{0:s}" not found while trying to serve for download'.format(pth))
	if filename is None:
		filename = basename(pth.rstrip('/'))
	filesize = getsize(pth)
	if settings.DEBUG:
		"""
			Serve the file through Django; only for development!
		"""
		with open(pth, 'rb') as fh:
			response = HttpResponse(fh.read())
	else:
		"""
			Let Apache do the work by giving it a X-Sendfile header as authorization.
		"""
		response = HttpResponse('')
		response['X-Sendfile'] = pth
	response['Content-type'] = content_type
	response['Content-Disposition'] = 'attachment; filename="{0:s}"'.format(filename)
	response['Content-Length'] = filesize
	return response


def serve_from_memory(data, filename, content_type='application/octet-stream'):
	assert data
	response = HttpResponse(data)
	response['Content-type'] = content_type
	response['Content-Disposition'] = 'attachment; filename="{0:s}"'.format(filename)
	response['Content-Length'] = len(data)
	return response

