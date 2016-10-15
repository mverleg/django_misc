
from django import forms
from django.forms import ModelForm, Form
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button
from django.core.urlresolvers import reverse


def BaseFormHelper(url_name = None, submit_name = 'submit', submit_css = '', back = '', back_name = 'back', back_css = 'btn_danger'):
	"""
		The default actions already implemented, but not overriding __init__ so that you
		can add more actions (actually a generator, not a class).
	"""
	helper = FormHelper()
	if url_name:
		helper.form_action = reverse(url_name)
	if back:
		#todo: this should work without javascript
		helper.add_input(Button('', back_name, onclick = 'location.href=\'%s\'' % reverse(back), css_class = back_css, tabindex = -1))
	""" It is not advisable to use 'submit' or 'post' as input names, because jquery gets confused. """
	if submit_name:
		helper.add_input(Submit('', submit_name, css_class = submit_css))
	return helper


class SimpleCrispyForm(Form):
	"""
		A simply form (like 80%) with just an action and a submit button (possibly a back button).
	"""

	next = forms.CharField(max_length = 64, widget = forms.HiddenInput, required = False, initial = '')

	URL_NAME = None
	SUBMIT_NAME = 'submit'
	SUBMIT_CSS = '' #'btn-warning btn-xs'
	BACK = ''
	BACK_NAME = 'back'
	BACK_CSS = 'btn-danger'

	def __init__(self, data = None, url_name = None, submit_name = None, back = None, back_name = None, submit_css = None, back_css = None, *args, **kwargs):
		self.helper = BaseFormHelper(
			url_name = url_name or self.URL_NAME,
			submit_name = submit_name or self.SUBMIT_NAME,
			back = back or self.BACK,
			back_name = back_name or self.BACK_NAME,
			submit_css = submit_css or self.SUBMIT_CSS,
			back_css = back_css or self.BACK_CSS,
		)
		super(SimpleCrispyForm, self).__init__(data, *args, **kwargs)


class SimpleCrispyModelForm(ModelForm):
	"""
		ModelForm version of SimpleCrispyForm.
	"""

	next = forms.CharField(max_length = 64, widget = forms.HiddenInput, required = False, initial = '')

	URL_NAME = None
	SUBMIT_NAME = 'submit'
	SUBMIT_CSS = '' #'btn-warning btn-xs'
	BACK = ''
	BACK_NAME = 'back'
	BACK_CSS = 'btn-danger'

	def __init__(self, data = None, url_name = None, submit_name = None, back = None, back_name = None, submit_css = None, back_css = None, *args, **kwargs):
		self.helper = BaseFormHelper(
			url_name = url_name or self.URL_NAME,
			submit_name = submit_name or self.SUBMIT_NAME,
			back = back or self.BACK,
			back_name = back_name or self.BACK_NAME,
			submit_css = submit_css or self.SUBMIT_CSS,
			back_css = back_css or self.BACK_CSS,
		)
		super(SimpleCrispyModelForm, self).__init__(data, *args, **kwargs)


class ReadonlyFormMixin(object):
	""" Needs to come before Form / ModelForm """

	URL_NAME = SUBMIT_NAME = BACK_NAME = ''

	def __init__(self, *args, **kwargs):
		super(ReadonlyFormMixin, self).__init__(*args, **kwargs)
		for field in self.fields.values():
			field.widget.attrs['disabled'] = 'true'


class ReadonlyCrispyForm(ReadonlyFormMixin, SimpleCrispyForm):
	pass


class ReadonlyCrispyModelForm(ReadonlyFormMixin, SimpleCrispyModelForm):

	def save(self, *args, **kwargs):
		raise NotImplementedError('form %s is read-only and should not be saved' % self.__class__)


