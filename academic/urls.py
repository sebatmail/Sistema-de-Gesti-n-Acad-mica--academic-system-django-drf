"""
Configuración de URLs para la aplicación 'academic'.

Evaluación N°1: Desarrollo Backend con Django & DRF
Docente: Marcelo Alvarado
Asignatura: Desarrollo Backend

Define tanto las rutas de navegación web (HTML enmascarado) como los endpoints de la API REST.
"""

from django.urls import path
from academic import views

urlpatterns = [
    # --------------------------------------------------------------------------
    # VISTAS WEB (HTML que enmascaran la API de DRF)
    # --------------------------------------------------------------------------
    path('courses/', views.courses_view, name='courses_web'),
    path('students/', views.students_view, name='students_web'),

    # --------------------------------------------------------------------------
    # ENDPOINTS DE LA API REST (Django REST Framework)
    # --------------------------------------------------------------------------
    path('api/teachers/', views.TeacherListAPIView.as_view(), name='api_teachers'),
    path('api/courses/', views.CourseListAPIView.as_view(), name='api_courses'),
    path('api/students/', views.StudentListAPIView.as_view(), name='api_students'),
    path('api/enrollments/', views.StudentCourseListAPIView.as_view(), name='api_enrollments'),
    path('api/stats/', views.AcademicStatsAPIView.as_view(), name='api_stats'),
]
