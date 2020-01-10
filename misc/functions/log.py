
import logging


_LOGGED_CACHE = set()


def warn(message, *args, **kwargs):
	logging.warning(message.format(*args, **kwargs))
	

def warn_once(message, *args, **kwargs):
	if message in _LOGGED_CACHE:
		return
	_LOGGED_CACHE.add(message)
	return warn(message, *args, **kwargs)



