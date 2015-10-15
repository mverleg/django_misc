
from random import choice
from string import ascii_letters
from warnings import warn
from django.template.loader import render_to_string
from django.forms import FileInput as DjangoFileInput


class FileInput(DjangoFileInput):
	"""
		Widget for showing a pretty Bootstrap3 file form.
	"""

	def __init__(self, attrs = None, clearable = None):
		super(FileInput, self).__init__(attrs = attrs)
		self.clearable = clearable
		if clearable is None:
			self.clearable = not self.attrs.get('required', False)
		self._warned_initial_value = False

	def render(self, name, value = None, attrs = None):
		if value and not self._warned_initial_value:
			warn('BootstrapFileInput initial value is ignored, <input type="file" /> allows no initial value.')
		final_attrs = self.build_attrs(attrs, type = self.input_type, name = name)
		return render_to_string('file_input.html', {
			'rand_id': ''.join(choice(ascii_letters) for k in range(12)),
			'filewidget': final_attrs,
			'clearable': self.clearable,
		})


