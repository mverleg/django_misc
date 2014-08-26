
$(document).ready(function() {
	/*
		upgrade e.g. tr or li containing a href to itself being a clickable element
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
		make tables marked as such sortable (for different settings, use your own class)
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
		}.bind(null, link, elem));
	});
});


