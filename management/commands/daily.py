
"""
	add this one to cron daily so as to fire the signal that other apps can use
"""

from django.core.management.base import BaseCommand
from misc.signals.daily import daily


class Command(BaseCommand):

	option_list = BaseCommand.option_list + ()
	help = 'add a cron job so that this command is run each hour; ' + \
		'it will send a custom signal that other apps can listen for'

	def handle(self, verbosity, *args, **options):
		print 'sending daily signal'
		daily.send(sender = None, last_app = 'misc', verbosity = verbosity, interactive = False)


