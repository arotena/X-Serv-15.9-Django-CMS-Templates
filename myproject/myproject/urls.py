from django.conf.urls import url, patterns, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login','django.contrib.auth.views.login'),
    url(r'^logout','django.contrib.auth.views.logout'),
    url(r'^accounts/profile/$' , 'cms.views.login'),
    url(r'^annotated/(\d+)$' , 'cms.views.mostrar'),
    url(r'^$' , 'cms.views.listar'),
    url(r'.*' , 'cms.views.notFound')
]
