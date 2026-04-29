from . import views
from django.urls import path


urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
]