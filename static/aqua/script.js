


$(document).ready(function() {

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


