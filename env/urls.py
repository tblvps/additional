from django.urls import path
from . import views

urlpatterns = [
    path('env/', views.save_env, name='save_env'),
    path('success/', views.success, name='success'),
]
