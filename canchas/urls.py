from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('new-turno/<int:id>/', views.newturno, name='new-turno'),
    path('delete-turno/<int:id>/', views.deleteturno, name='delete-turno'),
    path('update-turno/<int:id>/', views.updateturno, name='update-turno'),
    path('new-cancha/', views.newcancha, name='new-cancha'),
    path('delete-cancha/<int:id>/', views.deletecancha, name='delete-cancha')
]