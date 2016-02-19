
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.shortcuts import redirect
from haystack.views import SearchView
from .forms.search import SearchForm
from .views.autocomplete import autocomplete
from .views.db_backups import download_database, upload_database, download_media


misc_urlpatterns=[
	 url(r'^admin/', include(admin.site.urls)),
	 url(r'^admin/backup/media$', download_media, name='backup_media'),
	 url(r'^admin/backup/db$', download_database, name='backup_db'),
	 url(r'^admin/backup$', lambda request: redirect(reverse('backup_db')), name='backup'),
	 url(r'^admin/restore$', upload_database, name='restore'),
	 url(r'^search$', SearchView(template='search_page.html', form_class=SearchForm), name='search'),
	 url(r'^autocomplete$', autocomplete, name='autocomplete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


