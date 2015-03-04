# coding: utf-8
from django.conf.urls import patterns, url


urlpatterns = patterns(
    'eventi.receipts.views',
    url(r'^$', 'receipt', name='receipt'),
    url(r'^(\d+)/$', 'detail', name='detail'),
)
