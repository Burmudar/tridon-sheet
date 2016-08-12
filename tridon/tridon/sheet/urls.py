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
        regex=r'^upload/$',
        view=views.sheet_upload,
        name='upload'
    ),
]
