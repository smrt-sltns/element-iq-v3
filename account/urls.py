
from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'account'
urlpatterns = [
    
    # path("accounts/", include("django.contrib.auth.urls")),
    path('sign-up/', views.register, name='sign-up'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
