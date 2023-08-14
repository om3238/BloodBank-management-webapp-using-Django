from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.bloodbank_list, name='bloodbank_list'),
    path('add/', views.bloodbank_add, name='bloodbank_add'),
    path('update/<int:pk>/', views.bloodbank_update, name='bloodbank_update'),
    path('delete/<int:pk>/', views.bloodbank_delete, name='bloodbank_delete'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Define the logout URL
]
    