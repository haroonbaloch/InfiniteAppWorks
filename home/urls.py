
from django.views.static import serve
from django.urls import include, re_path
from InfiniteAppWorks import settings

from django.urls import path

from home import views as home_views, views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', home_views.about, name='about'),
    path('services/', home_views.services, name='services'),
    path('contact/', home_views.contact, name='contact'),
    # re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
