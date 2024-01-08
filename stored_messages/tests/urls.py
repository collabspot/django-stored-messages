from django.conf.urls import include
from django.contrib import admin
from django.urls import re_path

from stored_messages.tests.views import (message_create, message_create_mixed,
                                         message_view)

admin.autodiscover()

urlpatterns = [
    re_path(r'^consume$', message_view),
    re_path(r'^create$', message_create),
    re_path(r'^create_mixed$', message_create_mixed),
    re_path(r'^messages', include('stored_messages.urls', namespace='stored_messages'))
]
