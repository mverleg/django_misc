
$(document).ready(function() {
	/*
		Upgrade e.g. tr or li containing a href to itself being a clickable element.
	*/
	$('.upgrade_anchor').each(function(k, elem) {

		var anchors = $(elem).find('a[href]');
		if (anchors.length == 1)
		{
			var anchor = anchors.first();
			var url = anchor.attr('href');
			anchor.replaceWith(anchor.html());
			$(elem).click(function(anchor) {

				location.href = anchor;

			}.bind(null, url));
		}
	});

	/*
		de-obfuscate obfuscated text, such as email addresses
	*/
	$('.obfuscated').each(function(k) {
		var cypher = $(this).find('span').get(0).innerHTML;
		var clear = deobfuscate(cypher);
		$(this).replaceWith(clear);
	});

	/*
		Make tables marked as such sortable (for different settings, use your own class).
	*/
	$('.table-sortable').each(function(k, elem) {

		$(elem).tablesorter({
			sortList: [[0,0], [1,0]]
		});
	});

	/*
		select text in autofocus fields
	*/
	$('[autofocus]').each(function(k, elem) {
		$(elem).select();
	});

	/*
		Elements that are hidden until something is clicked (menu's, read-mores, etc...)
	*/
	$('.unfold_block').each(function(k, elem) {

		var elem = $(elem)
		if ($(elem).attr('data-label') == undefined) {
			console.log('please add data-label to all .unfold_block elements, e.g.', elem);
			return;
		};
		var link = $('<a href="#">' + $(elem).attr('data-label') + '</a>');
		link.insertBefore(elem);
		elem.hide();
		link.click(function(link, elem, event) {
			link.remove();
			elem.show();
			event.preventDefault();
		}.bind(null, link, elem));
	});
});

/*
	'fix' modulo (use the mathematical definition for negative numbers)
	http://stackoverflow.com/questions/4467539/javascript-modulo-not-behaving
*/
function mod(a, n)
{
	return a - (n * Math.floor(a/n));
}
function deobfuscate_letter(letter, pos)
{
	var encchars = document.settings.ENCCHARS
	var nr = encchars.indexOf(letter);
	if (nr < 0) { return letter; }
	oldnr = mod(nr - pos*pos - 42, encchars.length)
	return encchars.charAt(oldnr);
}
function deobfuscate(text, pos)
{
	var clear = '';
	for (var i = 0; i < text.length; i += 1)
	{
		clear += deobfuscate_letter(text[i], i)
	}
	return clear
}

function fsize_unit(sz)
{
	/*
		Display  filesizes as e.g. 53 B, 0.9 kB, 1.3 MB or 27 GB
		http://stackoverflow.com/questions/10420352/converting-file-size-in-bytes-to-human-readable
	*/
	var i = 0;
	var unit = ['B', 'kB', 'MB', 'GB', 'TB'];
	while (sz > 103)
	{
		sz = sz / 1024;
		i++;
	}
	console.log(sz);
	sz = sz.toFixed(sz > 20 ? 0: 1);
	console.log(sz);
	return sz + ' ' + unit[i];
}

