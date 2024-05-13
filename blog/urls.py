from django.urls import path, re_path
from blog import views

urlpatterns = [
    # path(route, view, kwargs=None, name=None)
    path("", views.index),
    # re_path(route, view, kwargs=None, name=None)
    re_path(r'^about/contact/', views.contact),
    re_path(r'^about/', views.about),
]
