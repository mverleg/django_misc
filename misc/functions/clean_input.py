
from re import sub

from bs4 import BeautifulSoup
from misc.functions.sanitize import sanitize_html


def purify_input(text, max_header = 3, add_nofollow = False):
	"""
		combination of sanitize_html and clean_input_html
	"""
	clean = sanitize_html(text, add_nofollow = add_nofollow)
	return clean_input_html(clean, max_header = max_header)


#todo: caching
#@settings.mem_cache
def clean_input_html(text, max_header = 3):
	"""
		Cleans an already santitized html string:

		* remove redundant whitespace, keep/insert basic newlines
		* replace <br /> tags with <p>
		* insert <p> around inlines at top level or inside <div>s
		* replace <b> and <i> with either headers or <strong> and <em>
		* downgrade headers higher than max_header, e.g. <h1> to <h3>
		* remove empty paragraphs

		Problems:

		* doesn't insert <p> when removing <br />
		* removes whitespace inside textareas (those are not allowed by sanitize() though)
	"""

	""" remove redundant whitespace """
	text = sub(r'[\s]+', ' ', text)

	""" create soup """
	soup = BeautifulSoup(text)

	""" block level elements (and br) """
	blocks = ('p', 'table', 'ul', 'ol', 'dl', 'h1', 'h2', 'h3', 'h4', 'h5', 'div',)
	blocksbr = blocks + ('br',)

	""" utility func for creating <p> """
	def _create_p(ptags):
		if ptags:
			newp = soup.new_tag('p')
			for ptag in ptags:
				newp.append(ptag)
			return newp
		return None

	""" utility func for removing whitespace """
	def _remove_whitespace(soup):
		for element in soup.find_all(recursive = True, text = True):
			txt = element.string
			if element.next_sibling is None:
				txt = str(txt).rstrip()
			if element.previous_sibling is None:
				txt = str(txt).lstrip()
			if txt:
				element.replace_with(soup.new_string(txt))
			else:
				element.extract()

	""" make sure br tags close properly """
	for tag in soup.find_all(recursive = True):
		if tag.name == 'br':
			tag.insert_before(soup.new_tag('br'))
			tag.unwrap()

	""" remove b and i with strong and em """
	for tag in soup.find_all('b', recursive = True):
		tag.name = 'strong'
	for tag in soup.find_all('i', recursive = True):
		tag.name = 'em'

	""" downgrade headers """
	for tag in soup.find_all(recursive = True):
		for header_nr in range(1, max_header):
			if tag.name == 'h%d' % header_nr:
				tag.name = 'h%d' % max_header

	""" split paragraphs with blocks or br's inside """
	paragraphs = [paragraph for paragraph in soup.find_all('p')]
	for paragraph in paragraphs:
		if not paragraph.find(blocksbr):
			continue
		ptags = []
		before_tag = paragraph.next_sibling
		children = [child for child in paragraph.children]
		paragraph.unwrap()
		for child in children:
			""" check if it contains any blocks (not just directly being one) """
			#todo:
			if child.name not in blocksbr:
				ptags.append(child.extract())
			else:
				newp = _create_p(ptags)
				if newp:
					child.insert_before(newp)
				if child.name == 'br':
					child.extract()
				ptags = []
		newp = _create_p(ptags)
		if newp:
			if before_tag:
				before_tag.insert_before(_create_p(ptags))
			else:
				soup.append(_create_p(ptags))

	""" create paragraphs around inline elements at top level or inside divs """
	for container in [soup] + [div for div in soup.find_all('div')]:
		ptags = []
		children = [child for child in container.children]
		for child in children:
			if child.name not in blocksbr:
				ptags.append(child.extract())
			else:
				newp = _create_p(ptags)
				if newp:
					child.insert_before(newp)
				ptags = []
				if child.name == 'br':
					child.extract()
		newp = _create_p(ptags)
		if newp:
			container.append(_create_p(ptags))

	""" remove extrema empty whitespace and br """
	_remove_whitespace(soup)

	for element in soup.find_all('br', recursive = True):
		if element.next_sibling is None or element.previous_sibling is None:
			element.extract()

	_remove_whitespace(soup)

	""" remove empty paragraphs """
	for tag in soup.find_all(recursive = True):
		if tag.name == 'p':
			children = [child for child in tag.children]
			if not children:
				tag.extract()

	""" upgrade <p><strong>text</strong><p> to <h?>text</h?> """
	for tag in soup.find_all('p', recursive = True):
		if len(tag.contents) == 1:
			child = tag.contents[0]
			if child.name == 'strong':
				tag.replace_with(child)
				child.name = 'h%d' % max_header
			if child.name == 'em':
				tag.replace_with(child)
				child.name = 'h%d' % (max_header + 1)

	""" make slightly readable """
	for container in [soup] + [div for div in soup.find_all('div')]:
		for block in container.find_all(blocksbr, recursive = False)[:-1]:
			block.insert_after(soup.new_string('\n'))

	""" return as unicode """
	return soup.renderContents().decode('utf8')


