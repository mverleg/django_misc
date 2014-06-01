
'''
	add this one to cron hourly so as to fire the signal that other apps can use
'''

from django.core.management.base import BaseCommand
from misc.signals.hourly import hourly


class Command(BaseCommand):
	
	option_list = BaseCommand.option_list + ()
	help = 'add a cron job so that this command is run each hour; it will send a custom signal that other apps can listen for'
	
	def handle(self, verbosity, *args, **options):
		print 'sending hourly signal'
		hourly.send(sender = None, last_app = 'misc', verbosity = verbosity, interactive = False)


