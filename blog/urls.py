from django.urls import path
from blog import views

urlpatterns = [
    # path(route, view, kwargs=None, name=None)
    path("", views.index),
    path("about/", views.about),
    path("contact/", views.contact),
]
