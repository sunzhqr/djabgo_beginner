from django.urls import path, re_path
from blog import views

urlpatterns = [
    # path(route, view, kwargs=None, name=None)
    # re_path(route, view, kwargs=None, name=None)
    path('', views.index),
    path('about/', views.about),
    re_path(r'^contact/', views.contact),
    path('details/', views.details),
    path('user/', views.user),
    path('access/<int:age>/', views.access),
]
