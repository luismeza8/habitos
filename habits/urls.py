from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('crear_habito/', views.crear_habito, name='crear_habito'),
]
