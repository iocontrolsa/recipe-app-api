""" URLS for the user API """
from django.urls import path

from user import views


app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('tokens/', views.CreateUserView.as_view(), name='token'),
]
