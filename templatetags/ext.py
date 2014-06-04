
from math import ceil
from django.core.serializers.json import DjangoJSONEncoder
from django.core.urlresolvers import reverse
from django.utils.html import escape, mark_safe
from django import template
from misc.functions.list_sample import list_sample
from misc.functions.obfuscate import obfuscate_letter
from misc.functions.html_filter import html_filter
from random import random
from json import dumps


register = template.Library()

'''
	return output if the url matches the reverse or url_name, else ''
	used to highlight currently active menu items
'''
@register.simple_tag(takes_context = True)
def if_url(context, url_name, output = 'active'):
	if 'request' in context:
		url = reverse(url_name)
		if context['request'].path == url:
			return output
	return ''

''' 
	obfuscate text (probably email) with javascript
	(40 chosen to exclude &)
'''
@register.filter
def obfuscate(clear):
	''' the obfuscation '''
	cypher = ''.join(obfuscate_letter(letter, pos) for pos, letter in enumerate(escape(clear)))
	''' wrap it to mark for deobfuscating '''
	span = '<span class=\'obfuscated\' title=\'this text was obfuscated to hide it from spammers; please enable javascript to see it\'>[enable JS]<span style="display: none;">%s</span></span>' % cypher
	return mark_safe(span)


''' 
	given an ordered collection (list, tuple, ...), return a string representation
	of the first limit items (or fewer), e.g. "itemA, itemB, itemC and 7 more"
	rsample does the sample, but shuffles the first 50 items and picks from that
'''
@register.filter
def sample(collection, limit = 3):
	return list_sample(collection, limit)
@register.filter
def rsample(collection, limit = 3):
	return list_sample(sorted(collection[:50], key = lambda x: random()), limit)


''' 
	apply a whitelist filter, which allows a limited selection of 
	secure HTML tags and attributes
'''
@register.filter
def noscr(text):
	return mark_safe(html_filter(text))


'''
	combine (update, extend) one or several data structures and convert them to json 
	note that this should only be used with trusted data (otherwise cross-site-script vulnerable)
	note also that *extra apparently does not work for template tags for some reason
'''
@register.filter
def json(obj, extra1 = None, extra2 = None, extra3 = None, extra4 = None, extra5 = None):
	for extra in filter(None, (extra1, extra2, extra3, extra4, extra5,)):
		try:
			obj.update(extra)
		except (TypeError, AttributeError):
			try:
				obj = obj + extra
			except TypeError:
				raise TypeError('|json filter called with incompatible arguments that could not be combined: %s and %s' % (type(obj), type(extra)))
	try:
		js = dumps(obj, cls = DjangoJSONEncoder)
	except TypeError:
		raise TypeError('called |json filter on an object that is not serializable by DjangoJSONEncoder')
	return mark_safe(js)


'''
	|euro: euro amount
	|ieuro: rounded euro amount
'''
@register.filter
def euro(amount, min = None, round = False):
	if min:
		amount = -amount
	if amount == '':
		raise ValueError('|euro filter applied to empty string (perhaps the variable was not found)')
	try:
		if round:
			return mark_safe('&euro; %d' % float(amount))
		return mark_safe('&euro; %.2f' % float(amount))
	except ValueError:
		raise ValueError('|euro filter should be applied to something that can be cast to a float (got %s)' % amount)
@register.filter
def ieuro(amount, min = None):
	return euro(ceil(amount), min = min, round = True)


'''
	in a template, use:
		{% call obj.method inst=my_inst %}
	to execute
		return obj.method(request, inst = my_inst)
'''
@register.simple_tag(takes_context = True)
def call(context, func, **kwargs):
	if not 'request' in context:
		raise Exception('{% call %} invoked without RequestContext')
	if func == '':
		raise Exception('you invoked {% call func %} with either an unknown func, or func directly the function you want to call; this is regretably not possible, as the function is evaluated before reaching call; you need to pass a function that returns the function you want.')
	return func(context['request'], **kwargs)


'''
	idea by /admin/admin_settings/setting/
'''
@register.filter
def upto(text, delimiter = None):
	return unicode(text).split(delimiter)[0]

