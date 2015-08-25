#Novo arquivo connectedin/perfi/urls.py

from django.conf.urls import patterns, url
from perfis import views

urlpatterns = patterns('',
    url(r'^$',views.index, name='index'),
    url(r'^perfis/(?P<perfil_id>\d+)$',views.exibir, name='exibir'),
    url(r'^perfis/(?P<perfil_id>\d+)/convidar$', views.convidar, name='convidar'),
    url(r'^perfis/(?P<convite_id>\d+)/aceitar$', views.aceitar, name='aceitar')
)