
from django.urls import path
from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.index, name='home'),
    path('contact/',views.contactPage,name='contact')
]
