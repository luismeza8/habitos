from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('crear_habito/', views.crear_habito, name='crear_habito'),
    path('borrar_habito/<int:pk>', views.borrar_habito, name='borrar_habito'),
    path('editar_habito/<int:pk>', views.editar_habito, name='editar_habito'),
    path('alternar_dia/<int:pk>/', views.alternar_dia, name='alternar_dia'),
    path('habit/<int:habit_id>/graph/', views.grafica_habito, name='grafica_habito'),
]