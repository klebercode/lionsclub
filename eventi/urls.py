from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from filebrowser.sites import site

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^$', 'eventi.core.views.home', name='home'),
    url(r'^inscricao/', include('eventi.subscriptions.urls',
        namespace='subscriptions')),
    url(r'^comprovante/', include('eventi.receipts.urls',
        namespace='receipts')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/filebrowser/', include(site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
