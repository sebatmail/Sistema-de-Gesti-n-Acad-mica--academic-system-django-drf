"""
URL configuration for academic_project project.

Evaluación N°1: Desarrollo Backend con Django & DRF
Docente: Marcelo Alvarado
Asignatura: Desarrollo Backend

Requerimiento Técnico 4:
"Eliminar el 'error 404' cuando no hay un endpoint asignado a la ruta '/' (vacia)."
Se incluye redirección desde '/' hacia '/courses/' garantizando acceso inmediato sin errores.
"""

from django.contrib import admin
from django.urls import path, include
from academic.views import home_redirect_view

urlpatterns = [
    # Ruta raíz '/': Redirige directamente al listado de cursos para evitar el error 404
    path('', home_redirect_view, name='home_root'),

    # Panel de administración de Django
    path('admin/', admin.site.urls),

    # Inclusión de todas las rutas web y de API de la aplicación académica
    path('', include('academic.urls')),
]
