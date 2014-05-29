
from admin_settings import Setting
from django.http import Http404
from misc.views.notification import notification


'''
	show the value of an admin_setting as a page
'''
def setting_flatpage(request, setting):
	try:
		body_text = Setting.objects.get(name = setting).value
	except Setting.DoesNotExist:
		raise Http404('page not found because of missing database value')
	try:
		subject_text = Setting.objects.get(name = '%s_SUBJECT' % setting).value
	except Setting.DoesNotExist:
		subject_text = ''
	return notification(request, message = body_text, subject = subject_text, home_button = False)


