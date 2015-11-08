
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
try:
	""" Django 1.9 & backward compatibility """
	from django.apps import apps
	get_model = apps.get_model
except ImportError:
	from django.db.models.loading import get_model


def lazy_create_permission(codename):
	"""
		Have to lazy-create this, since it can't reasonably be created during migration since ContentType doesn't exist.

		https://stackoverflow.com/questions/29296757/django-data-migrate-permissions
	"""
	app_label, model = settings.AUTH_USER_MODEL.split('.')
	UserType = ContentType.objects.get(app_label=app_label, model=model.lower())
	Permission = get_model('auth', 'Permission')
	try:
		perm = Permission.objects.get(
			codename = codename,
			content_type = UserType
		)
	except Permission.DoesNotExist:
		perm = Permission.objects.create(
			codename = codename,
			content_type = UserType
		)
		perm.save()
	return perm


