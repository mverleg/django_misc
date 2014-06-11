
'''
	take plain text / html crawled from a webpage and convert it
	to something sort-of displayable as simple text
'''

from re import compile, sub
from bs4 import BeautifulSoup, Comment


def cleanup_text(value, allowed_tags = 'p:title a:href:title img:src:alt:title table:cellspacing:cellpadding tbody th tr td:title:colspan:rowspan ol ul li:title br'):
	
	value = unicode(value)
	
	js_regex = compile(r'[\s]*(&#x.{1,7})?'.join(list('javascript')))
	allowed_tags = {parts[0]: parts[1:] for parts in (tag.split(':') for tag in allowed_tags)}
	
	if '<p>' not in value:
		value = '<p>%s</p>' % value
	value = sub(r'\<br *\/?\>', '</p><p>', value)
	
	soup = BeautifulSoup(value)
	for comment in soup.findAll(text = lambda text: isinstance(text, Comment)):
		comment.extract()
	
	for tag in soup.findAll(True):
		if tag.name not in allowed_tags:
			tag.hidden = True
		else:
			tag.attrs = dict((attr, js_regex.sub('', val)) for attr, val in tag.attrs.items() if attr in allowed_tags[tag.name])
	
	html = soup.prettify().renderContents().decode('utf8')
	html.replace('\r\n','\n').replace('\r','\n')


