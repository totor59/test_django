from django.conf.urls import url
from . import views

urlpatterns = [
             url(r'^$', views.accueil, name='accueil'),
             url(r'^article/(\d+)$', views.lire, name='lire')
            ]
