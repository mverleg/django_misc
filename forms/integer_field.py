
from django.core.validators import MinValueValidator
from django.db.models import BigIntegerField, PositiveIntegerField
from django.forms import IntegerField as IntegerFormField
from django.utils.functional import cached_property


"""
	Form fields
"""
class BigPositiveIntegerFormField(IntegerFormField):
	def __init__(self, min_value, max_value, *args, **kwargs):
		super(BigPositiveIntegerFormField, self).__init__(self,
			max(min_value, 0),
			min(max_value, BigIntegerField.MAX_BIGINT),
			*args, **kwargs
		)


class StrictlyPositiveIntegerFormField(IntegerFormField):
	def __init__(self, min_value, max_value, *args, **kwargs):
		super(StrictlyPositiveIntegerFormField, self).__init__(self,
			max(min_value, 1),
			min(max_value, IntegerFormField.MAX_BIGINT),
			*args, **kwargs
		)


"""
	Model fields
"""
class BigPositiveIntegerField(BigIntegerField):
	@cached_property
	def validators(self):
		return super(BigPositiveIntegerField, self).validators + [MinValueValidator(0)]

	def formfield(self, **kwargs):
		defaults = {
			'form_class': BigPositiveIntegerFormField,
			'min_value': 0,
			'max_value': BigIntegerField.MAX_BIGINT
		}
		defaults.update(kwargs)
		return super(BigPositiveIntegerField, self).formfield(**defaults)


class StrictlyPositiveIntegerField(PositiveIntegerField):
	@cached_property
	def validators(self):
		return super(StrictlyPositiveIntegerFormField, self).validators + [MinValueValidator(1)]

	def formfield(self, **kwargs):
		defaults = {
			'form_class': BigPositiveIntegerFormField,
			'min_value': 0,
			'max_value': BigIntegerField.MAX_BIGINT
		}
		defaults.update(kwargs)
		return super(StrictlyPositiveIntegerField, self).formfield(**defaults)


