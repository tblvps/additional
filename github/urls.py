from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list_repos, name='list_repos'),
    path('create/', views.create_repo, name='create_repo'),
    path('delete/', views.delete_repo, name='delete_repo'),
]

