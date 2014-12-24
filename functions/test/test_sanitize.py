
from misc.functions.sanitize import sanitize_html


str1 = '''Business &amp; Society takes a fundamental and historical perspective on a key phenomenon in Western society:
the company. In the process, we introduce you to the key issues of the Management &amp; Technology master track.
Business &amp; Society has the following specific objectives:<br /><br />
You understand the importance of the company in capitalist economic systems:<br />
<ul><li>You analyze how the company has developed in capitalist economic systems;</li>
<li>You analyze why the company has developed in this particular way;</li>
<li>You assess the future of the company.</li></ul><script></script></p>'''
str2 = ''' <<script>script> alert("hacked"); </</script>script> '''
str3 = '''<a href="http://malicious.ru/hack.html" rel="author">free money</a><a href="#mypage"></a>'''


def test_sanitize_html_whitelist():
	clean = sanitize_html(str1)
	print(clean)
	assert '<li>' in clean
	assert '<script>' not in clean
	assert '</p>' not in clean


def test_sanitize_html_hacks():
	clean = sanitize_html(str2)
	print(clean)
	assert '<' not in clean
	assert '>' not in clean


def test_sanitize_html_nofollow():
	clean = sanitize_html(str3, True)
	print(clean)
	assert 'author nofollow' in clean
	assert '"nofollow"' not in clean
	clean = sanitize_html(str3)
	print(clean)
	assert 'nofollow' not in clean


if __name__ == '__main__':
	print(sanitize_html(str1, True))
	print(sanitize_html(str2, True))
	print(sanitize_html(str3, True))


