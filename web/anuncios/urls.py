from django.urls import path
from anuncios import views

urlpatterns = [
    path('anuncios/',views.anuncios,name="anuncios"),
    path('',views.home,name="home"),
]
