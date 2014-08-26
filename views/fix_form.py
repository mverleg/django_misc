
from crispy_forms.layout import Button
from django.shortcuts import render


def fix_form(request, form, subject = '', cancel_url = None):
	"""
		Show a view that let's a user fix errors in a Crispy form.

		Not a very user friendly way, but usable for forms that under normal circumstances should not throw errors,
		such as multiple choice ones.
	"""
	if cancel_url is None:
		cancel_url = request.get_full_path()
	form.helper.inputs.insert(-1, Button('', 'Cancel', onclick = 'location.href=\'%s\'' % cancel_url, tabindex = -1))
	return render(request, 'fix_form.html', {
		'form': form,
		'subject': subject,
	})


