from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('users/password-change/', 
     auth_views.PasswordChangeView.as_view(template_name="users/password_change.html"),
     name="password_change"),
    
    path('users/password-change-done/',
     auth_views.PasswordChangeDoneView.as_view(template_name="users/password_change_done.html"),
     name="password_change_done"),

]
