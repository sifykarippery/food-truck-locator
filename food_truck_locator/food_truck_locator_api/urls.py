from django.urls import path
from . import views

urlpatterns = [
    # Hello, world!
    path('', views.index, name='index')
]