
from django.template.defaultfilters import striptags
from django.utils.html import escape
from haystack.query import SearchQuerySet
from haystack.utils import Highlighter
from misc.response.json_response import JSONResponse


def autocomplete(request):
	query = escape(request.GET.get('q', '')).strip()
	if len(query) < 2:
		suggestions = []
	else:
		lighter = Highlighter(query, max_length=64)
		sqs = SearchQuerySet().autocomplete(auto=query)[:7]
		suggestions = []
		for result in sqs:
			match = ' '.join(striptags(lighter.highlight(result.auto)).strip('.').split())
			url = None
			if hasattr(result.object, 'get_absolute_url'):
				url = result.object.get_absolute_url()
			suggestions.append({
				'name': match,
				#'title': result.title,
				'url': url,
			})
	return JSONResponse(request, suggestions)


