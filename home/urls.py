from django.template.defaulttags import url
from django.urls import path
from django.views.static import serve
from django.urls import include, re_path
from InfiniteAppWorks import settings
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
