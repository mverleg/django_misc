
'''
	shuts down all post requests to the site to make the site static
	  there could be non-POST interaction, but that's usually a bad idea
	  use @disable decorator if it exists and you want to disable it anyway
'''

from misc.decorators.disable_view import no_interaction_response


class NonInteractiveModeMiddleware(object):
	def process_request(self, request):
		excluded = ('/account/', '/admin/',)
		for exclusion in excluded:
			if request.get_full_path().startswith(exclusion):
				return None
		if request.method == 'POST':
			return no_interaction_response
		return None


