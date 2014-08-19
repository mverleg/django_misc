
"""
	this signal is sent once each hour if the correct cron job is added
		python /path/management.py hourly
"""

from django.dispatch import Signal


hourly = Signal(providing_args = ['last_app', 'verbosity', 'interactive',])


