from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    #path('login/', views.login, name="login"),
    #path('login/', views.CustomLoginView.as_view(), name='login_view'),
    #path('signup/', views.CustomSignupView.as_view(), name='signup_view'),
    path('register/', views.register, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('camera_input/', views.camera_input, name="camera_input"),
    path('stats/', views.stats, name='stats'),
    path('results_saved/',views.results_saved , name='update_statistics'),
    path('send_email/', views.send_email, name='send_email')
    
]