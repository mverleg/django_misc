
"""
	A default form for representing a button that handles something about an instance, e.g. delete.
"""

from django import forms
from django.core.exceptions import ValidationError

from misc.forms.crispy import SimpleCrispyForm
from misc.functions.render import render_str2str


class ObjectButtonForm(SimpleCrispyForm):

	pk = forms.IntegerField(required = True, widget = forms.HiddenInput)

	URL_NAME = None
	SUBMIT_NAME = 'ok'
	SUBMIT_CSS = ''
	BACK = None

	def clean_pk(self):
		pk = self.cleaned_data['pk']
		if not self.cls is None:
			try:
				self.instance = self.cls.objects.get(pk = pk)
			except self.cls.DoesNotExist:
				raise ValidationError('no %s with pk %d' % (self.cls.__name__, pk))
		return pk

	def __init__(self, data = None, instance = None, cls = None, url_name = None, submit_name = None, back = None, back_name = None, submit_css = None, back_css = None, small = None, initial = None, *args, **kwargs):
		if initial is None:
			initial = {}
		if instance and not cls:
			cls = type(instance)
		if small is None:
			small = not back
		if small:
			submit_css = ('%s btn-xs' % submit_css).strip()
		self.cls = cls
		if not 'pk' in initial and instance is not None:
			if not hasattr(instance, 'pk'):
				raise Exception('no primary key supplied and instance of %s does not have one' % type(instance))
			initial['pk'] = instance.pk
		super(ObjectButtonForm, self).__init__(data = data, url_name = url_name, submit_name = submit_name, back = back, back_name = back_name, submit_css = submit_css, back_css = back_css, *args, initial = initial, **kwargs)

	'''
		render to string so you can do
			return ObjectButtonForm(data = None, instance = self, url_name = 'my_url_name', initial = {'next': request.get_full_path()}).render(request)
	'''
	def render(self, request):
		return render_str2str(request, ''' {% load crispy_forms_tags %} <div class="object_button">{% crispy form %}</div> ''', {'form': self})
