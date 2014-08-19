
from dogpile.cache import make_region


mem_cache = make_region().configure(
	'dogpile.cache.pylibmc',
	expiration_time = 150,
	arguments = {
		'url':['127.0.0.1'],
	}
).cache_on_arguments(to_str = lambda obj: str(obj.__hash__()))


