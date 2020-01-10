
from datetime import datetime
from io import StringIO
from os import chmod
from os.path import join
from shutil import make_archive
from tempfile import gettempdir

from display_exceptions import NotYetImplemented
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.management import call_command
from django.http import FileResponse, HttpResponseForbidden

from misc.functions.permission import lazy_create_permission
from misc.views.serve_file import serve_file


def download_database(request):
	"""
		Make a json dump of the entire database excluding sessions.
	"""
	lazy_create_permission('make_backup')
	if not request.user.has_perm('make_backup'):
		return HttpResponseForbidden('you do not have permission to create backups')
	data = StringIO()
	call_command('dumpdata', exclude=['sessions.session',], natural_foreign=True, natural_primary=True, stdout=data, indent=1)
	response = FileResponse(data.getvalue(), content_type='application/json')
	response['Content-Disposition'] = 'attachment; filename={0:s}_{1:s}.json'.format(
		get_current_site(request).domain.replace('.', '-'), datetime.now().strftime('%Y%b%d').lower())
	return response


def upload_database(request):
	"""
		Upload a json dump as exported by download_database, and overwrite the database with it.
	"""
	lazy_create_permission('restore_backup')
	if not request.user.has_perm('svsite.restore_backup'):
		return HttpResponseForbidden('you do not have permission to create backups')
	raise NotYetImplemented('upload database')


def download_media(request):
	"""
		Make a gzip copy of all media files.
	"""
	lazy_create_permission('make_backup')
	if not request.user.has_perm('make_backup'):
		return HttpResponseForbidden('you do not have permission to create backups')
	zip_pth = join(gettempdir(), 'media_export')
	make_archive(zip_pth, 'zip', root_dir=settings.MEDIA_ROOT)
	chmod(zip_pth + '.zip', 0o600)
	return serve_file(zip_pth + '.zip', content_type='application/zip',
		filename='media_export_{0:s}.zip'.format(datetime.now().strftime('%Y%b%d').lower()))


