
from django.template import Template
from django.template.context import RequestContext
from django.template.loader import get_template


'''
	analogue to the render shortcut that renders a 
	named template to a string (rather than response)
'''
def strender(request, template, context = {}):
    return get_template(template).render(RequestContext(request, context))


'''
	render a string to a string
'''
def render_str2str(request, in_str, context = {}):
	return Template(in_str).render(RequestContext(request, context))


