
from django.http import HttpResponse


not_accessible_response = HttpResponse('This page is not ready yet; please come back at a later time!')
def disable(func):
	def disabled_view(request, *args, **kwargs):
		return not_accessible_response
	return disabled_view


no_interaction_response = HttpResponse('This page is not interactive yet; please come back at a later time!')
def disable_interaction(func):
	def disabled_post_view(request, *args, **kwargs):
		if request.method == 'POST':
			return no_interaction_response
		return func(request, *args, **kwargs)
	return disabled_post_view


