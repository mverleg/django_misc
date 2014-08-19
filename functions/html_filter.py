
"""
	filters a string to only allow whitelisted tags
	argument should be in form 'tag2:attr1:attr2 tag2:attr1 tag3', where tags
	  are allowed HTML tags, and attrs are the allowed attributes for that tag.
	http://djangosnippets.org/snippets/1655/
"""

from re import compile
from bs4 import BeautifulSoup, Comment
import settings


def whitelist_tags(soup, allowed_tags):
	"""
		takes soup, returns text
	"""

	if not isinstance(soup, BeautifulSoup):
		soup = BeautifulSoup(unicode(soup))

	js_regex = compile(r'[\s]*(&#x.{1,7})?'.join(list('javascript')))
	#allowed_tags = [tag.split(':') for tag in allowed_tags.split()]
	#allowed_tags = dict((tag[0], tag[1:]) for tag in allowed_tags)
	allowed_tags = {parts[0]: parts[1:] for parts in (tag.split(':') for tag in allowed_tags)}

	for comment in soup.findAll(text = lambda text: isinstance(text, Comment)):
		comment.extract()

	for tag in soup.findAll(True):
		if tag.name not in allowed_tags:
			tag.hidden = True
		else:
			tag.attrs = dict((attr, js_regex.sub('', val)) for attr, val in tag.attrs.items() if attr in allowed_tags[tag.name])

	return soup.renderContents().decode('utf8')


def html_filter(value):
	"""
		apply the whitelist filter to make sure there is no possibility of scripting
		invalid html (e.g. extra closing tags) should also be removed this way
	"""

	DEFAULT_NOSCR_ALLOWED_TAGS = 'p:title h1:title h2:title h3:title div:title span:title a:href:title img:src:alt:title table:cellspacing:cellpadding thead tbody th tr td:title:colspan:rowspan ol ul li:title br'
	allowed_tags = getattr(settings, 'NOSCR_ALLOWED_TAGS', DEFAULT_NOSCR_ALLOWED_TAGS)

	return whitelist_tags(value, allowed_tags)


def cleanup_html_text(value,
		allowed_blocks = 'p:title img:src:alt:title table:cellspacing:cellpadding ol ul',
		allowed_inlines = 'span:title a:href:title thead tbody th tr td:title:colspan:rowspan ol ul li:title'):
	"""
		given a html text, apply agressive filtering to get displayable format (paragraphs etc)
	"""

	value = unicode(value)
	blocks = []

	allowed_blocks = {parts[0]: parts[1:] for parts in (tag.split(':') for tag in allowed_blocks)}
	allowed_inlines = {parts[0]: parts[1:] for parts in (tag.split(':') for tag in allowed_inlines)}

	oldsoup = BeautifulSoup(value)
	for block in oldsoup.find_all(recursive = False):
		if block.name in allowed_blocks.keys():
			extracted = block.extract()
		else:
			extracted = oldsoup.new_tag('p')
			extracted.append(block.text)
		extracted = whitelist_tags(extracted, allowed_inlines)
		blocks.append(extracted)

	newsoup = oldsoup.new_tag('div')
	for block in blocks:
		newsoup.append(block)

	return newsoup.renderContents().decode('utf8')


