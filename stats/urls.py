from django.urls import path
from . import views

urlpatterns = [
    path('', views.team_list, name='team_list'),
    path('teams/', views.team_list, name='team_list'),
    path('teams/<int:pk>', views.team_detail, name="team_detail")
]