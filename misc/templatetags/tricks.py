
from django.utils.html import escape, mark_safe
from django import template
from misc.functions.obfuscate import obfuscate_letter


register = template.Library()


@register.filter
def obfuscate(clear, email = False):
	"""
		obfuscate text (probably email) with javascript
		(40 chosen to exclude &)
	"""
	''' the obfuscation '''
	cypher = ''.join(obfuscate_letter(letter, pos) for pos, letter in enumerate(escape(clear)))
	''' wrap it to mark for deobfuscating '''
	span = ('<span class="obfuscated {1:s}" title="This text was obfuscated to hide it from spammers; please enable javascript to see it.">' +
	    '[enable JS]<span style="display: none;">{0:s}</span></span>').format(cypher, 'obfuscated_email' if email else '')
	return mark_safe(span)


@register.filter
def obfuscate_email(clear):
	return obfuscate(clear, email = True)


@register.simple_tag(takes_context = True)
def call(context, func, **kwargs):
	"""
		in a template, use:
			{% call obj.method inst=my_inst %}
		to execute
			return obj.method(request, inst = my_inst)
	"""
	if not 'request' in context:
		raise Exception('{% call %} invoked without RequestContext')
	if func == '':
		raise Exception('you invoked {% call func %} with either an unknown func, or func directly the function you want to call; this is regretably not possible, as the function is evaluated before reaching call; you need to pass a function that returns the function you want.')
	return func(context['request'], **kwargs)

