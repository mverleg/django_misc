
'''
	this decorator replaces func with a function that returns func
	this is useful for functions needed in templates, because they
	  are always evaluated, even when passing them to tags
	hence the name: it's a decorator for functions passed to {% call %}
'''

from functools import partial


def for_call(func):
	def func_that_returns_func(self):
		return partial(func, self)
	return func_that_returns_func
