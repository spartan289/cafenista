from django.urls import path
from . import views
urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('forget_pass',views.forget_pass,name='forget_pass'),
    path('verify',views.verify,name='verify'),
    path('reset',views.reset,name='reset')
    ]