from django.urls import path
from . import views


urlpatterns = [
    path("", views.company, name="company"),
    path("news/", views.news, name="news"),
    path("management/", views.management, name="management"),
    path("about/", views.about, name="about"),
    path("contacts/", views.contacts, name="contacts"),
    path("branches/", views.all_branches, name="branches"),
    path("branches/paris/", views.paris, name="paris"),
    path("branches/london/", views.london, name="london"),
]
