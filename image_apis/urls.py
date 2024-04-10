
from django.urls import path
from . import views

app_name = 'image_apis'
urlpatterns = [
    path('generate/', views.generate, name='generate'),
]
