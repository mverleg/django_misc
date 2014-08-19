
from django.shortcuts import render


def template(template):
	"""
		like this in urlconf:

			url(r'^staff/$', template('staff_overview.html'), name = 'staff_overview'),
	"""
	def template_view(request):
		return render(request, template, {})
	return template_view


