
'''
    filters a string to only allow whitelisted tags
    argument should be in form 'tag2:attr1:attr2 tag2:attr1 tag3', where tags
      are allowed HTML tags, and attrs are the allowed attributes for that tag.
    http://djangosnippets.org/snippets/1655/
'''

from re import compile
from bs4 import BeautifulSoup, Comment
import settings


def html_filter(value):
    
    DEFAULT_NOSCR_ALLOWED_TAGS = 'p:title h1:title h2:title h3:title div:title span:title a:href:title img:src:alt:title table:cellspacing:cellpadding tbody th tr td:title:colspan:rowspan ol ul li:title br'
    allowed_tags = getattr(settings, 'NOSCR_ALLOWED_TAGS', DEFAULT_NOSCR_ALLOWED_TAGS)
    value = unicode(value)
    
    js_regex = compile(r'[\s]*(&#x.{1,7})?'.join(list('javascript')))
    allowed_tags = [tag.split(':') for tag in allowed_tags.split()]
    allowed_tags = dict((tag[0], tag[1:]) for tag in allowed_tags)
    
    soup = BeautifulSoup(value)
    for comment in soup.findAll(text = lambda text: isinstance(text, Comment)):
        comment.extract()
    
    for tag in soup.findAll(True):
        if tag.name not in allowed_tags:
            tag.hidden = True
        else:
            tag.attrs = dict((attr, js_regex.sub('', val)) for attr, val in tag.attrs.items() if attr in allowed_tags[tag.name])
    
    return soup.renderContents().decode('utf8')


