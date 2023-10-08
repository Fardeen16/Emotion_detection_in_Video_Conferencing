from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('login/', views.CustomLoginView.as_view(), name='login_view'),
    path('signup/', views.CustomSignupView.as_view(), name='signup_view'),
    path('camera_input/', views.camera_input, name="camera_input"),
    # path('analytics/', views.analytics, name = 'analytics')
    
]