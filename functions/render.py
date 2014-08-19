
from django.template import Template, Context
from django.template.context import RequestContext
from django.template.loader import get_template


def strender(request, template, context = {}):
	"""
		analogue to the render shortcut that renders a
		named template to a string (rather than response)
	"""
	return get_template(template).render(RequestContext(request, context))


def render_str2str(request, in_str, context = {}):
	"""
		render a string to a string
	"""
	return Template(in_str).render(RequestContext(request, context))


def strender_norequest(template, context = {}):
	"""
		render a template to a string without request
	"""
	return get_template(template).render(Context(context))


