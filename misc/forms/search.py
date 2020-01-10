
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from haystack.forms import SearchForm as HaySearchForm


class SearchForm(HaySearchForm):

	helper = FormHelper()
	helper.form_method = 'GET'
	helper.add_input(Submit('', 'Search'))
	helper.form_show_labels = False

	def __init__(self, *args, **kwargs):
		super(SearchForm, self).__init__(*args, **kwargs)
		self.fields['q'].widget.attrs['placeholder'] = 'Your search query...'
		self.fields['q'].widget.attrs['autofocus'] = 'autofocus'
		self.fields['q'].widget.attrs['autocomplete'] = 'off'
		self.fields['q'].widget.attrs['class'] = self.fields['q'].widget.attrs.get('class', '') + ' search-typeahead'


