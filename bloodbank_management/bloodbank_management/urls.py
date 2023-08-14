from django.contrib import admin
from django.urls import path, include
from .views import donor_form_view
from . import views 
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('bloodbank/', include('bloodbank.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/',views.signup_view, name='signup_view'),
    path('',views.dash,name='dash'),
    path('donor-form/', donor_form_view, name='donor-form'),
    path('logout/', views.dash, name='logout'),
]
