
from django.urls import path
from . import views

app_name = 'image_apis'
urlpatterns = [
    path('generate/', views.generate, name='generate'),
    path('generate-ajax/', views.generate_ajax, name='generate-ajax'),
    path('decrease-tokens/', views.decrease_tokens, name='decrease-tokens'),
    path('invalid-access/', views.admin_restriction, name='invalid-access')
    # path('test/', views.test, name='test'),
]
