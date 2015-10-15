
"""
	Limit the rate at which a function can be executed, by sleeping after a certain number of steps. Use e.g. when
	accessing remote resources to prevent overloading the service.
"""

from time import sleep


def limit_rate(itercount = 100, waittime = 1., showmsg = False):
	def decorated(func):
		def limited_func(*args, **kwargs):
			limit_rate.iter += 1
			if limit_rate.iter >= itercount:
				if showmsg:
					print('sleep %.3fs after %d steps' % (waittime, limit_rate.iter))
				sleep(waittime)
				limit_rate.iter = 0
			return func(*args, **kwargs)
		return limited_func
	return decorated

limit_rate.iter = 0


