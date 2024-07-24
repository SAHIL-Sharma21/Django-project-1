
from django.urls import path
from . import views

#url-> localhost:8000/new_app
urlpatterns = [
    path('', views.all_chai, name='all_chai'),
]
