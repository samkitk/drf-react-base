from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('team_list/', views.teamListView, name='team_list')
]