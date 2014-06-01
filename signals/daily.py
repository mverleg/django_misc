
'''
	this signal is sent once each day if the correct cron job is added
		python /path/management.py daily
'''

from django.dispatch import Signal


daily = Signal(providing_args = ['last_app', 'verbosity', 'interactive',])


