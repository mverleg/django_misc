
'''
	decorator for functions that take a unique model attribute as
	url parameter (or other string argument), and convert that 
	into an actual instance of that model as argument for the function
	e.g. django url sees this function:
		my_view(request, example_pk)
	which is defined as
		@instantiate(Example)
		def my_view(request, example)
	uses primary key by default, with modelname as instance kwarg 
	and modelname_pk as input string kwargs (can all be changed)
'''

from django.http import Http404


def instantiate(Model, in_kw_name = None, out_kw_name = None, model_attr_name = 'pk', model_attr_type = int):
	if out_kw_name is None:
		out_kw_name = Model.__name__.lower()
	if in_kw_name is None:
		in_kw_name = '%s_pk' % out_kw_name
	def convert_to_instance_decorator(func):
		def func_with_instance(request, *args, **kwargs):
			identifier = kwargs.pop(in_kw_name)
			try:
				instance = Model.objects.get(**{model_attr_name: model_attr_type(identifier)})
			except Model.DoesNotExist:
				message = 'This page expectes a %s with %s = %s, but no such %s was found.' % (Model.__name__, model_attr_name, identifier, Model.__name__)
				raise Http404(message)
			kwargs[out_kw_name] = instance
			return func(request, *args, **kwargs)
		return func_with_instance
	return convert_to_instance_decorator


