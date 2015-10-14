
"""
	filefield that stores the uniquified, uploaded name to a specified (optionally
	unique) model field (actually, it doesn't even have to be a field, it could
	just be a model property)

	directory can be specified with Class.UPLOAD_DIR or kwargs upload_to = '/path/'
	upload field name can be specified by Class.FILENAME_FIELD or kwarg name_field
	(default to MEDIA_ROOT and 'name' respectively)

	this raises a validation error if in one request (or simultaneous ones), two files
	with the same name are uploaded, because they'll generate the same .name field
	(both availabilities are checked before saving file or instance). However,
	that seems like a pretty rare and useless care; limit new file uploading if worried.
"""

from functools import partial
from os.path import basename, splitext, join
from django.conf import settings
from django.utils.text import slugify
from django.db.models import FileField, ImageField


def filename_to_name_field(instance, filename, upload_dir, name_field):
	barename, extension = splitext(basename(filename))
	path = join(upload_dir, '%s.%s' % (slugify(barename).replace('-', '_'), slugify(extension)))
	newpath = instance.file.storage.get_available_name(path)
	if not getattr(instance, name_field, None):
		setattr(instance, name_field, basename(newpath))
	return newpath


class AutoNameFileField(FileField):
	def __init__(self, name_field = 'name', *args, **kwargs):
		if 'upload_to' in kwargs:
			if not isinstance('upload_to', str):
				raise Exception('for %(cls)s, \'upload_to\' should be a string pointing to a directory, not a callable, as %(cls)s determines the filename')
			upload_dir = kwargs.pop('upload_to')
		else:
			upload_dir = getattr(self, 'UPLOAD_DIR', settings.MEDIA_ROOT)
		upload_func = partial(filename_to_name_field, upload_dir = upload_dir, name_field = name_field)
		super(AutoNameFileField, self).__init__(self, *args, upload_to = upload_func, **kwargs)


class AutoNameImageField(ImageField):
	pass


