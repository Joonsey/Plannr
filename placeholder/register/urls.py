from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.register, name='registerView'),
    path('login/', views.loginView, name='loginView'),
    path('logout/', views.logoutView, name="logout")
]
