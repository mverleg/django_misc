
from datetime import datetime
from io import StringIO
from django.contrib.sites.shortcuts import get_current_site
from django.core.management import call_command
from django.http import FileResponse, HttpResponseForbidden
from functions.permission import lazy_create_permission
from display_exceptions import NotYetImplemented


def download_database(request):
	"""
		Make a json dump of the entire database excluding sessions.
	"""
	lazy_create_permission('make_backup')
	if not request.user.has_perm('svsite.make_backup'):
		return HttpResponseForbidden('you do not have permission to create backups')
	data = StringIO()
	call_command('dumpdata', exclude = ['sessions.session'], natural_foreign = True, natural_primary = True, stdout = data)
	response = FileResponse(data.getvalue(), content_type = 'application/json')
	response['Content-Disposition'] = "attachment; filename={0:s}_{1:s}.json".format(
		get_current_site(request).domain, datetime.now().strftime('%Y%b%d').lower())
	return response


def upload_database(request):
	"""
		Upload a json dump as exported by download_database, and overwrite the database with it.
	"""
	lazy_create_permission('restore_backup')
	if not request.user.has_perm('svsite.restore_backup'):
		return HttpResponseForbidden('you do not have permission to create backups')
	raise NotYetImplemented('upload database')
	#todo


