
from django.shortcuts import render


def notification(request, message, subject = '', next = None, home_button = True, status_code = None):
	"""
		show a simple notification
		possibly inside another view, as confirmation or error
	"""
	response = render(request , 'notification.html', {
		'subject': subject,
		'message': message,
		'next': next,
		'home_button': home_button,
	})
	if status_code:
		response.status_code = status_code
	return response


def error_notification(request, message, subject = '', next = None, home_button = True):
	return notification(request, message, subject = subject, next = next, home_button = home_button, status_code = 500)


