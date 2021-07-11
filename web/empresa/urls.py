from django.urls import path
from empresa import views

urlpatterns = [
    path("empresa/", views.mostrarEmpresa,name="empresa"),
]