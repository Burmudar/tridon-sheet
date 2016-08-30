# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the UserListView
    url(
        regex=r'^$',
        view=views.index,
        name='index'
    ),
    url(
        regex=r'^invoice/$',
        view=views.invoice,
        name='invoice'
    ),
    url(
        regex=r'^upload/$',
        view=views.sheet_upload,
        name='upload'
    ),
    url(
        regex=r'^(?P<workbook_pk>[0-9]+)/view/$',
        view=views.SheetEntryView.as_view(),
        name='entries'
    ),
    url(
        regex=r'^documents/$',
        view=views.documents,
        name='documents'
    ),
    url(
        regex=r'^about/$',
        view=views.about,
        name='about'
    ),
    url(
        regex=r'^contact/$',
        view=views.contact,
        name='contact'
    ),
    url(
        regex=r'^invoice/$',
        view=views.invoice,
        name='invoice'
    ),
    url(
        regex=r'^invoice/(?P<pk>[0-9]+)$',
        view=views.SheetDetailView.as_view(),
        name='invoice-detail'
    ),
]
