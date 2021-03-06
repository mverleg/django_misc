
import string
from os import chmod, makedirs
from os.path import join, exists, dirname, abspath
from random import choice
from sys import stderr

template = '''
"""
A few local, potentially secret, settings.

Do not include this in your repository!
"""

from os.path import dirname, join


BASE_DIR = dirname(dirname(__file__))

SITE_URL = '{0:s}.markv.nl' #todo: update url
ALLOWED_HOSTS = ['.{0:s}'.format(SITE_URL), 'localhost', '.localhost.markv.nl']

SECRET_KEY = '{1:s}'

DATABASES = {{  #todo: disable one of the databases
	'default': {{
		'ENGINE': 'django.db.backends.mysql',
		'NAME': '{0:s}',
		'USER': '{0:s}',
		'PASSWORD': 'PASSWORD',
		'HOST': '127.0.0.1',
		'PORT': '3306',
		'CONN_MAX_AGE': 120,
	}}
}}
DATABASES = {{
	'default': {{
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': join('data', 'sqlite', '{0:s}', 'db.sqlite3'),
	}}
}}

MEDIA_ROOT = join('data', 'media', '{0:s}')
STATIC_ROOT = join('data', 'static', '{0:s}')

DEBUG = True
\n\n'''


def generate_local(_file, project='PROJECT', create=False):
	stderr.write('\nno local settings file was found; a sample one will be generated\n')
	chars = string.printable.rstrip().replace('\'', '').replace('"', '')
	key = ''.join(choice(chars) for k in range(32))
	content = template.format(project, key)
	if create:
		pth = join(dirname(abspath(_file)), 'local.py')
		if not exists(pth):
			try:
				with open(pth, 'w+') as fh:
					fh.write(content)
			except:
				stderr.write('local.py could not be created at "{0:s}"\n'.format(pth))
			else:
				try:
					chmod(pth, 0o600)
				except:
					stderr.write('could not set permissions for local.py at "{0:s}"\n'.format(pth))
			mpth = join('/', 'data', 'media', project)
			try:
				makedirs(mpth, mode=0o770, exist_ok=True)
			except Exception as err:
				stderr.write('could not create media directory "{0:s}": {1:s}\n'.format(mpth, str(err)))
			spth = join('/', 'data', 'static', project)
			try:
				makedirs(spth, mode=0o7450, exist_ok=True)
			except Exception as err:
				stderr.write('could not create static directory "{0:s}": {1:s}\n'.format(spth, str(err)))
		else:
			stderr.write('local.py exists after all at "{0:s}"\n'.format(pth))
	else:
		print(content)
	print('[ ] check the generated settings')
	print('[ ] check that local settings are not world readable')
	print('[ ] check that media files are writable by the server')
	print('[ ] check that local.py is not in your VCS (e.g. add to .gitignore)')
	print('[ ] test if everything works')
	exit(1)


