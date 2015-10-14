
"""
	automatically upgrade models to their subclass if they have one
	by setting objects = AutoSubclassManager()
	no extra queries, but queries do get slower (more joins)
"""

from model_utils.managers import InheritanceManager


class AutoSubclassManager(InheritanceManager):
	def get_queryset(self):
		return super(AutoSubclassManager, self).get_queryset().select_subclasses()


