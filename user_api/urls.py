from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('users', views.UserView.as_view())
]