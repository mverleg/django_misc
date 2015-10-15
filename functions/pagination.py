

def pagination_nearby(items):
	"""
		Get a list of pages to display for pagination, and None values for continuation dots.

		Shows up to 12 values, always shows the fist and last two elements and the two elements left and right of the current one.

		See e.g. the template pagination_bootstrap.html
	"""
	if items.paginator.num_pages <= 10:
		return range(1, items.paginator.num_pages + 1)
	if items.number <= 6:
		return range(1, 9) + [None, items.paginator.num_pages, items.paginator.num_pages + 1]
	if items.number >= items.paginator.num_pages - 6:
		return [1, 2, None] + range(items.paginator.num_pages - 8, items.paginator.num_pages + 1)
	return [1, 2, None] + range(items.number - 2, items.number + 3) + [None, items.paginator.num_pages, items.paginator.num_pages + 1]


