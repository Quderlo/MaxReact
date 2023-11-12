from django.contrib import admin
from django.urls import path

from kek.views import receive_request

urlpatterns = [
    path('signup', receive_request, name='receive_request'),
]