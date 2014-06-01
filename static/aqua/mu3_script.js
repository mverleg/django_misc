
/* 'fix' modulo (use the mathematical definition for negative numbers)
	http://stackoverflow.com/questions/4467539/javascript-modulo-not-behaving */
function mod(a, n)
{
	return a - (n * Math.floor(a/n));
}
function deobfuscate_letter(letter, pos, mi, ma)
{
	// return chr((nr - mi - pos ** 2) % (ma - mi) + mi)
	var nr = String.charCodeAt(letter);
	if ((mi <= nr) && (nr <= ma))
	{
		return String.fromCharCode(mod(nr - mi - pos*pos, ma - mi) + mi);
	}
	else
	{
		return letter;
	}
}
function deobfuscate(text, pos, mi = 32, ma = 126)
{
	var clear = '';
	for (var i = 0; i < text.length; i += 1)
	{
		clear += deobfuscate_letter(text[i], i, mi ,ma)
	}
	return clear
}

$(document).ready(function() {
	/*
		de-obfuscate obfuscated text, such as email addresses
	*/
	$('.obfuscated').each(function(k) {
		var cypher = $(this).find('span').get(0).innerHTML;
		var clear = deobfuscate(cypher);
		$(this).replaceWith(clear);
	});
});


