from django.urls import path
from . import views

urlpatterns = [
	path('', views.login),
    path('dashboard/<str:pk>/', views.home, name = "home"),
    path('about/<str:pk>/', views.about, name = "about"), #past statement
    path('customer/<str:pk>/', views.customer, name = "customer"), #prediction chart
    path('createStatement/<str:pk>/', views.statement, name = "createStatement"),
    path('updateStatement/<str:pk>/', views.update, name = "updateStatement"),
    #path('loginPage/', views.login),
    path('registration/', views.registration, name = 'registration')

    #pass in <str:pk> in each url after you figure out how to take input from login and set that as pk value

]