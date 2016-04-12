"""cs60 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles import views as static_view
from django.conf import settings

from ckeditor_uploader import views as ck_views
from register import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^ckeditor/upload/', ck_views.upload, name='ckeditor_upload'),
    url(r'^ckeditor/browse/', ck_views.browse, name='ckeditor_browse'),

    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^record/list/$', views.RecordListView.as_view(), name='record_list'),
    url(r'^record/(?P<pk>[0-9]+)/detail/$', views.RecordDetailView.as_view(), name='record_detail'),
    url(r'^record/csv/$', views.CreateCSVView.as_view(), name='get_csv')
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', static_view.static.serve, {'document_root': settings.STATIC_ROOT}, name="static"),
        url(r'^media/(?P<path>.*)$', static_view.static.serve, {'document_root': settings.MEDIA_ROOT}, name="media")
    ]
