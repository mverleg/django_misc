
from misc.functions.clean_input import clean_input_html
from misc.functions.sanitize import sanitize_html


str1 = '''<b>Subjects</b><br><p class="MsoNormal">This course gives students an introduction to the concepts of
environmental and natural resource economics. <br> We will deal with the following topics in this course:</p><em>Core
concepts of environmental economic thought</em>  <ul><li>The history of environmental economic thought <br></li>
<li>&nbsp;Economic concepts to analyze the causes of environmental detoriation and resource use<br></li></ul><em>
Economic valuation and its applications</em>  <ul><li>Valuation methods for ecosystem services</li><li>Cost-benefit
analysis</li></ul><em>Economic governance instruments</em>  <ul><li>Economic instruments theory <br></li><li>&nbsp;
Application: value capturing in land development <br></li><li>Application: EU Emission Trading Scheme <br></li></ul>
<div class="sidebox"> <p> <h1>special test</h1>
text
<a href="http://test.nl"></a>
<br>
just a string </p>
<img src="elephant.jpg" alt="some big and gray thing idk" /> </div>'''
str2 = '''<div><strong>hi</strong></div>'''


if __name__ == '__main__':
	print(clean_input_html(sanitize_html(str1, True)))


