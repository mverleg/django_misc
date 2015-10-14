
from django.utils.safestring import SafeData
from bs4 import BeautifulSoup, Comment, NavigableString
try:
	from urllib.parse import urlparse
except ImportError:
	from urlparse import urlparse
from re import sub, IGNORECASE
from django.conf import settings


DEFAULT_NOSCR_ALLOWED_TAGS = 'strong:title b i em:title p:title h1:title h2:title h3:title h4:title h5:title ' + \
	'div:title span:title ol ul li:title a:href:title:rel img:src:alt:title dl td:title dd:title' + \
	'table:cellspacing:cellpadding thead tbody th tr td:title:colspan:rowspan br'


def single_escape(text):
	# DEPRECATED: BEAUTIFULSOUP DOES ESCAPING OF <, >, & ALREADY
	"""
		Escapes HTML special characters if not already SafeDate,
		but attempts to skip those that have already been escaped;
	"""
	if isinstance(text, SafeData):
		return text
	text = sub(r'&(?!amp|lt|gt|quot|#39)', r'&amp;', text, flags = IGNORECASE)
	return text.replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;').replace("'", '&#39;')


def _escape_child_strings(tag, soup):
	# DEPRECATED: BEAUTIFULSOUP DOES ESCAPING OF <, >, & ALREADY
	"""
		Used by sanitize_html.

		Takes a soup and finds all direct descendant text nodes, replacing each of them with an escaped version.

		Returns soup, but substitution also happens in-place.
	"""
	for child in tag.children:
		if isinstance(child, NavigableString):
			clean_text = single_escape(str(child))
			child.replace_with(soup.new_string(clean_text))
		return tag


#todo: turn caching back on (broken now)
#@settings.mem_cache
def sanitize_html(text, add_nofollow = False,
		allowed_tags = getattr(settings, 'NOSCR_ALLOWED_TAGS', DEFAULT_NOSCR_ALLOWED_TAGS)):
	"""
		Cleans an html string:

		* remove any not-whitelisted tags
			- remove any potentially malicious tags or attributes
			- remove any invalid tags that may break layout
		* esca[e any <, > and & from remaining text (by bs4); this prevents
			> >> <<script>script> alert("Haha, I hacked your page."); </</script>script>\
		* optionally add nofollow attributes to foreign anchors
		* removes comments
		:comment * optionally replace some tags with others:

		:arg text: Input html.
		:arg allowed_tags: Argument should be in form 'tag2:attr1:attr2 tag2:attr1 tag3', where tags are allowed HTML
			tags, and attrs are the allowed attributes for that tag.
		:return: Sanitized html.

		This is based on https://djangosnippets.org/snippets/1655/
	"""

	""" function to check if urls are absolute
		note that example.com/path/file.html is relative, officially and in Firefox """
	is_relative = lambda url: not bool(urlparse(url).netloc)

	""" regex to remove javascript """
	#todo: what exactly is the point of this? is there js in attribute values?
	#js_regex = compile(r'[\s]*(&#x.{1,7})?'.join(list('javascript')))

	""" allowed tags structure """
	allowed_tags = [tag.split(':') for tag in allowed_tags.split()]
	allowed_tags = {tag[0]: tag[1:] for tag in allowed_tags}

	""" create comment-free soup """
	soup = BeautifulSoup(text)
	for comment in soup.findAll(text = lambda text: isinstance(text, Comment)):
		comment.extract()

	for tag in soup.find_all(recursive = True):
		if tag.name not in allowed_tags:
			""" hide forbidden tags (keeping content) """
			tag.hidden = True
		else:
			""" whitelisted tags """
			tag.attrs = {attr: val for attr, val in tag.attrs.items() if attr in allowed_tags[tag.name]}
			#""" remove javascript from tags """
			#tag.attrs = {attr: js_regex.sub('', val) for attr, val in tag.attrs.items()}
		#""" escape string children """
		#_escape_child_strings(tag, soup)
		""" add nofollow to external links if requested """
		if add_nofollow and tag.name == 'a' and 'href' in tag.attrs:
			if not is_relative(tag.attrs['href']):
				tag.attrs['rel'] = (tag.attrs['rel'] if 'rel' in tag.attrs else []) + ['nofollow']

	#""" escape soup for top-level string nodes """
	#_escape_child_strings(soup, soup)

	""" return as unicode """
	return soup.renderContents().decode('utf8')


