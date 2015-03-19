
"""
	Decorators that, for a view given post data, shows a page with a message that
	lets the user confirm or cancel the action (an extra step as failsafe)
		@confirm_first('are you sure you want to do this?')
		def delete_everything(request);

	:arg cancel_url_func: function that returns the url to redirect to (because reverse does not work in a decorator
		declaration, as this is executed as url's are loading)
"""

from django.core.urlresolvers import reverse
from django.shortcuts import render


CONFIRM_FIELD_NAME = 'confirmed'


def confirm_first(message, subject = '', submit_text = 'continue', submit_class = 'btn-success',
	confirm_field_name = CONFIRM_FIELD_NAME, cancel_url_name = None):
	def actual_decorator(view_func):
		def wrapped_func(request, *args, **kwargs):
			''' check if this is a POST request and whether it's already confirmed '''
			if request.method == 'POST':
				if confirm_field_name not in request.POST:
					cancel_url = '/'
					if cancel_url_name:
						cancel_url = reverse(cancel_url_name)
					elif 'next' in request.POST:
						cancel_url = request.POST['next']
					return render(request, 'confirm_first.html', {
						'post': list(request.POST.items()),
						'subject': subject,
						'message': message,
						'cancel_url': cancel_url,
						'submit_url': '', # same page
						'submit_text': submit_text,
						'submit_class': submit_class,
						'confirm_field_name': confirm_field_name,
					})
			''' not submitting or already confirmed '''
			return view_func(request, *args, **kwargs)
		return wrapped_func
	return actual_decorator


confirm_delete = confirm_first(message = 'Are you sure you want to delete this item?', subject = 'Delete?',
	submit_text = 'delete', submit_class = 'btn-danger')


