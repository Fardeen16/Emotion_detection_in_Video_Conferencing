from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('camera_input/', views.camera_input, name='camera_input')
]