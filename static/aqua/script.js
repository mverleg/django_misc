
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

$(document).ready(function() {
	/*
		de-obfuscate obfuscated text, such as email addresses
	*/
	$('.obfuscated').each(function(k) {
		var cypher = $(this).find('span').get(0).innerHTML;
		var clear = deobfuscate(cypher);
		$(this).replaceWith(clear);
	});
	
	/*
		upgrade link menus
	*/
	$('.li_a_upgrade li a').each(function(k) {
		var url = $(this).attr('href');
		$(this).parent().click(function (url) {
			window.location.href = url;
		}.bind(null, url));
	});
	
	/*
		update classes and html to make datepicker work
		
	*/
	$('.datetimeinput').each(function(k) {
		$(this).parent().addClass('input-group date insert-datetimeinput');
		$(this).next().remove();
		$(this).after('<span class="input-group-addon"><span class="glyphicon glyphicon-calendar"></span></span>');
	});
	$('.dateinput').each(function(k) {
		$(this).parent().addClass('input-group date insert-dateinput');
		$(this).next().remove();
		$(this).after('<span class="input-group-addon"><span class="glyphicon glyphicon-calendar"></span></span>');
	});
	$('.timeinput').each(function(k) {
		$(this).parent().addClass('input-group date insert-timeinput');
		$(this).next().remove();
		$(this).after('<span class="input-group-addon"><span class="glyphicon glyphicon-time"></span></span>');
	});
	/*
		now attach the datepickers
	*/
	$('.insert-datetimeinput').each(function(k) {
		$(this).datetimepicker({
			format: document.settings.DATETIME_INPUT_FORMAT,
			sideBySide: true, 
			showToday: true,
			minuteStepping: 5,
			useSeconds: false,
		});
	});
	$('.insert-dateinput').each(function(k) {
		$(this).datetimepicker({
			format: document.settings.DATE_INPUT_FORMAT,
			pickTime: false,
			showToday: true,
		});
	});
	$('.insert-timeinput').each(function(k) {
		$(this).datetimepicker({
			format: document.settings.TIME_INPUT_FORMAT,
			pickDate: false,
			minuteStepping: 5,
			useSeconds: false,
		});
	});
});


