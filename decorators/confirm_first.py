
'''
	decorators that, for a view given post data, shows a page with a message that 
	lets the user confirm or cancel the action (an extra step as failsafe)
		@confirm_first('are you sure you want to do this?')
		def delete_everything(request);
'''

from django.shortcuts import render


CONFIRM_FIELD_NAME = 'confirmed'

def confirm_first(message, subject = '', submit_text = 'continue', submit_class = 'btn-success', confirm_field_name = CONFIRM_FIELD_NAME):
	def actual_decorator(view_func):
		def wrapped_func(request, *args, **kwargs):
			''' check if this is a POST request and whether it's already confirmed '''
			if request.method == 'POST':
				if confirm_field_name not in request.POST:
					return render(request, 'confirm_first.html', {
						'post': request.POST.items(),
						'subject': subject,
						'message': message,
						'cancel_url': request.POST['next'] if 'next' in request.POST else '/',
						'submit_url': '', # same page
						'submit_text': submit_text,
						'submit_class': submit_class,
						'confirm_field_name': confirm_field_name,
					})
			''' not submitting or already confirmed '''
			return view_func(request, *args, **kwargs)
		return wrapped_func
	return actual_decorator


confirm_delete = confirm_first(message = 'Are you sure you want to delete this item?', subject = 'Delete?', submit_text = 'delete', submit_class = 'btn-danger', confirm_field_name = CONFIRM_FIELD_NAME)


