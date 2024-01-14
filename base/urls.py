from django.urls import path
from . import views

urlpatterns = [

path('', views.home, name='home'),
path('main/', views.main, name='main'),
path('TeaCollection/', views.TeaCollection, name='TeaCollection'),

path('login/', views.login_view, name='login'),
path('logout/', views.logout_view, name='logout'),
path('register/', views.register_view, name='register'),
path('about/', views.about, name='about'),
path('contact/', views.contact, name='contact'),
path('admin_login/', views.login, name='login'),
]