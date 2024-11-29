
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('profile/', views.profile, name='profile'),
    path("i18n/", include("django.conf.urls.i18n")),
]
