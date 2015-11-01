
from random import choice
from string import ascii_letters
from crispy_forms.layout import Submit, Layout, HTML
from django.template.loader import render_to_string, get_template


class SubmitWithProgress(Submit):
	"""
		*** DEPRECATED ***
		#todo remove

		Show a submit button that turns into a progress bar when the form is submitted.

		This didn't work due to https://github.com/maraujop/django-crispy-forms/issues/537
	"""
	input_type = 'submit'

	def __init__(self, *args, **kwargs):
		super(SubmitWithProgress, self).__init__(*args, **kwargs)
		raise DeprecationWarning('replaced due to not working (which might be a bug in crispy-forms); see SubmitProgress')

	def render(self, *args, **kwargs):
		button_html = super(SubmitWithProgress, self).render(*args, **kwargs)
		progress_html = render_to_string('submit_progress_bar.html', {
			'rand_id': ''.join(choice(ascii_letters) for k in range(12)),
		})
		return '{0:s}\n{1:s}'.format(button_html, progress_html)


class SubmitProgress(Layout):

	def __init__(self, *args, **kwargs):
		super(SubmitProgress, self).__init__(*args, **kwargs)
		widget = get_template('submit_progress_bar.html').render({
			'rand_id': ''.join(choice(ascii_letters) for k in range(12)),
		})
		self.fields = [HTML(widget)]


