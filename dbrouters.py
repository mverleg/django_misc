
#todo: deprecated because djangocms is being a bitch

class BaseRouter:
	dbname = 'dbname'
	apps = set()

	def db_for_read(self, model, **hints):
		if model._meta.app_label in self.apps:
			return self.dbname
		return None

	def db_for_write(self, model, **hints):
		return self.db_for_read(model, **hints)

	def allow_relation(self, obj1, obj2, **hints):
		if obj1._state.db in self.apps and obj2._state.db in self.apps:
			return True
		return None

	def allow_migrate(self, db, app_label, model=None, **hints):
		if app_label in self.apps:
			return db == self.dbname
		return None


class ScratchRouter(BaseRouter):
	dbname = 'scratch'
	apps = {'sessions',}

	def allow_relation(self, obj1, obj2, **hints):
		return None


class LoggingRouter(BaseRouter):
	dbname = 'scratch'
	apps = {'admin', 'reversion',}


class DataRouter(BaseRouter):
	dbname = 'default'

	def db_for_read(self, model, **hints):
		return self.dbname

	def allow_relation(self, obj1, obj2, **hints):
		return True

	def allow_migrate(self, db, app_label, model=None, **hints):
		return True


"""SETTINGS:

DATABASES = {
	'data': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': join(BASE_DIR, 'dev', 'data.sqlite3'),
	},
	'logging': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': join(BASE_DIR, 'dev', 'logging.sqlite3'),
	},
	'scratch': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': join(BASE_DIR, 'dev', 'scratch.sqlite3'),
	},
	#todo: search index? task queue?
}

DATABASE_ROUTERS = [
	'base.inout.ScratchRouter',
	'base.inout.LoggingRouter',
	'base.inout.DataRouter',
]
"""