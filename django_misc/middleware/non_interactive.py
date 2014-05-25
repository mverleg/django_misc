
'''
	shuts down all post requests to the site to make the site static
	  there could be non-POST interaction, but that's usually a bad idea
	  use @disable decorator if it exists and you want to disable it anyway
'''

from misc.decorators.disable_view import no_interaction_response


class NonInteractiveModeMiddleware(object):
	def process_request(self, request):
		if request.method == 'POST' and not request.get_full_path().startswith('/account/'):
			return no_interaction_response
		return None


