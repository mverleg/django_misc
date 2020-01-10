
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import reverse, path
from haystack.views import SearchView

from .forms.search import SearchForm
from .views.autocomplete import autocomplete
from .views.db_backups import download_database, upload_database, download_media

misc_urlpatterns=[
	path(r'admin/', admin.site.urls),
	path(r'admin/backup/media', download_media, name='backup_media'),
	path(r'admin/backup/db', download_database, name='backup_db'),
	path(r'admin/backup', lambda request: redirect(reverse('backup_db')), name='backup'),
	path(r'admin/restore', upload_database, name='restore'),
	path(r'search', SearchView(template='search_page.html', form_class=SearchForm), name='search'),
	path(r'autocomplete', autocomplete, name='autocomplete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


