
from django.conf.global_settings import LOGIN_URL
from django.shortcuts import redirect
from django.http import HttpResponseForbidden


def staff_required(func):
	def check_perm_func(request, *args, **kwargs):
		if not request.user.is_authenticated():
			return redirect(to = '%s?next=%s' % (LOGIN_URL, request.get_full_path()))
		elif not request.user.is_staff:
			return HttpResponseForbidden('You need to be a staff member to perform this action (you account \'%s\' is not a staff account).' % getattr(request.user, request.user.USERNAME_FIELD))
		return func(request, *args, **kwargs)
	return check_perm_func


