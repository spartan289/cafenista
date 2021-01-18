from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('ex_list',views.ex_list,name='ex_list'),
    path('email_to_be_sent',views.email_to_be_sent,name='email_to_be_sent')

]