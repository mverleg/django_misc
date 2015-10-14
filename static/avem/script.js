
$(document).ready(function()
{
	/*
		de-obfuscate obfuscated text, such as email addresses
	*/
	$('.obfuscated').each(function(k) {
		var cypher = $(this).find('span').get(0).innerHTML;
		var clear = deobfuscate(cypher);
		$(this).replaceWith(clear);
	});

	/*
		select text in autofocus fields
	*/
	$('[autofocus]').each(function(k, elem) {
		$(elem).select();
	});

	/*
		Dropdown closes as soon as search field is clicked; prevent that.
	 */
	$('#menu-search-dropdown').click(function(event)
	{
		event.stopPropagation();
	});

	/*
		When selecting a dropdown that has inputs, focus and select the first field.
	 */
	function focus_and_select_input(elem)
	{
		elem.select();
		elem.focus();
	}
	$('.dropdown-toggle').click(function(event)
	{
		var inputs = $(this).parent().find('input');
		if (inputs.length)
		{
			var input = inputs.first();
			setTimeout(focus_and_select_input.bind(null, input), 0);
		}
	});

	/*
		Let ctrl+H open the search bar.
		http://stackoverflow.com/a/14180949/723090
	 */
	$(window).bind('keydown', function(event)
	{
	    if (event.ctrlKey || event.metaKey) {
	        switch (String.fromCharCode(event.which).toLowerCase())
			{
				case 'h':
					event.preventDefault();
					var msdb = $('#menu-search-dropdown-button');
					if (msdb.is(":visible"))
					{
						/* The search is in dropdown menu mode */
						var input = $('#menu-search-dropdown').find('input').first();
						msdb.click();
					}
					else
					{
						var msm = $('#menu-search-mainbar');
						/* The search is in menubar mode, but it might be collapsed */
						if ( ! msm.is(":visible"))
						{
							/* It's collapsed; probably the user doesn't have a ctrl key if their screen is this small... */
							$('#menubar-toggle-collapse').click();
						}
						var input = msm.find('input').first();
					}
					setTimeout(focus_and_select_input.bind(null, input), 0);
					break;
	        }
	    }
	});
});

/*
	'Fix' modulo (use the mathematical definition for negative numbers)
	http://stackoverflow.com/questions/4467539/javascript-modulo-not-behaving
*/
function mod(a, n)
{
	return a - (n * Math.floor(a/n));
}

/*
	Make text readable that has been hidden to prevent crawling.
 */
function deobfuscate_letter(letter, pos)
{
	var encchars = document.settings.ENCCHARS;
	var nr = encchars.indexOf(letter);
	if (nr < 0) { return letter; }
	oldnr = mod(nr - pos*pos - 42, encchars.length);
	return encchars.charAt(oldnr);
}

function deobfuscate(text)
{
	var clear = '';
	for (var i = 0; i < text.length; i += 1)
	{
		clear += deobfuscate_letter(text[i], i)
	}
	return clear
}


