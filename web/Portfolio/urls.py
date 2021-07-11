from django.urls import path
from Portfolio import views

urlpatterns = [
    path("portfolio/", views.portfolio,name="portfolio"),
]