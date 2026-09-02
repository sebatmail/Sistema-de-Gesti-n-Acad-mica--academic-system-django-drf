"""
Vistas del Sistema de Gestión Académica (Web & API REST).

Evaluación N°1: Desarrollo Backend con Django & DRF
Docente: Marcelo Alvarado
Asignatura: Desarrollo Backend

Cumplimiento de Criterios:
- Criterio 3: Implementa de forma correcta las vistas (views.py) que renderizan las plantillas HTML (render()) sin errores.
- Criterio 7: Construye la interfaz web funcional que "enmascara" la API de DRF mediante vistas HTML estilizadas.
- Requerimiento 3 y Criterio 2: Configura endpoints API en DRF que retornan datos almacenados/cargados en memoria o archivo JSON.
"""

from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Modelos ORM
from academic.models import Teacher, Course, Student, StudentCourse

# Serializadores DRF
from academic.serializers import (
    TeacherSerializer,
    CourseSerializer,
    StudentSerializer,
    StudentCourseSerializer
)

# Módulo de datos en memoria y JSON (para soporte sin base de datos)
from academic.data_manager import (
    get_teachers_memory,
    get_courses_memory,
    get_students_memory,
    get_student_courses_memory
)


# ==============================================================================
# VISTAS DE RENDERIZADO HTML ("ENMASCARAMIENTO" DE ENDPOINTS)
# El usuario interactúa con estas vistas HTML mientras JavaScript consume la API REST
# ==============================================================================

@require_GET
def home_redirect_view(request):
    """
    Vista para la ruta raíz '/'.
    Redirige automáticamente al listado de Cursos para eliminar el error 404
    cuando se visita la URL base del servidor.
    """
    return redirect('courses_web')


@require_GET
def courses_view(request):
    """
    Renderiza la plantilla HTML de cursos (courses.html).
    Enmascara el endpoint /api/courses/. La página se entrega con el cascarón visual
    y un script asíncrono fetch() puebla dinámicamente la tabla con los cursos y sus docentes.
    """
    context = {
        'page_title': 'Gestión de Cursos y Asignaturas',
        'active_menu': 'courses',
    }
    return render(request, 'academic/courses.html', context)


@require_GET
def students_view(request):
    """
    Renderiza la plantilla HTML de estudiantes (students.html).
    Enmascara el endpoint /api/students/. La página se carga rápidamente y mediante
    JavaScript asíncrono fetch() renderiza los estudiantes en el navegador.
    """
    context = {
        'page_title': 'Listado de Estudiantes',
        'active_menu': 'students',
    }
    return render(request, 'academic/students.html', context)


# ==============================================================================
# ENDPOINTS DE LA API REST (DJANGO REST FRAMEWORK)
# Proveen datos JSON asíncronos para consumo del frontend y clientes externos
# Cuentan con soporte híbrido: Base de Datos Relacional o Colecciones JSON en memoria
# ==============================================================================

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt, name='dispatch')
class TeacherListAPIView(APIView):
    """
    Endpoint: /api/teachers/
    Métodos: GET, POST
    Descripción: Retorna la lista completa de docentes o registra un nuevo docente.
    """
    def get(self, request, *args, **kwargs):
        # Soporte para forzar fuente en memoria con query param '?source=json'
        source = request.GET.get('source', '').lower()
        
        try:
            # Si existen registros en la base de datos relacional y no se forzó JSON puro
            if source != 'json' and Teacher.objects.exists():
                teachers = Teacher.objects.all()
                serializer = TeacherSerializer(teachers, many=True)
                return Response({
                    "success": True,
                    "count": len(serializer.data),
                    "source": "database_sqlite",
                    "data": serializer.data
                }, status=status.HTTP_200_OK)
        except Exception:
            # Fallback seguro a memoria en caso de no haber aplicado migraciones aún
            pass

        # Si no hay registros en la base de datos, se procesa la colección en memoria/JSON
        memory_data = get_teachers_memory()
        serializer = TeacherSerializer(memory_data, many=True)
        return Response({
            "success": True,
            "count": len(serializer.data),
            "source": "json_in_memory",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """Permite registrar un nuevo docente a través de la API REST."""
        first_name = request.data.get('first_name', '').strip()
        last_name = request.data.get('last_name', '').strip()
        if not first_name or not last_name:
            return Response({
                "success": False,
                "message": "Se requiere el nombre y apellido del docente."
            }, status=status.HTTP_400_BAD_REQUEST)
        
        teacher = Teacher.objects.create(first_name=first_name, last_name=last_name)
        serializer = TeacherSerializer(teacher)
        return Response({
            "success": True,
            "message": "Docente registrado con éxito.",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)


@method_decorator(csrf_exempt, name='dispatch')
class CourseListAPIView(APIView):
    """
    Endpoint: /api/courses/
    Métodos: GET, POST
    Descripción: Retorna la lista de asignaturas o registra una nueva asignatura con su docente asignado.
    """
    def get(self, request, *args, **kwargs):
        source = request.GET.get('source', '').lower()

        try:
            if source != 'json' and Course.objects.exists():
                # Optimización select_related para traer la relación docente en una sola consulta SQL
                courses = Course.objects.select_related('teacher').all()
                serializer = CourseSerializer(courses, many=True)
                return Response({
                    "success": True,
                    "count": len(serializer.data),
                    "source": "database_sqlite",
                    "data": serializer.data
                }, status=status.HTTP_200_OK)
        except Exception:
            pass

        # Procesamiento desde colecciones estructuradas JSON sin requerir base de datos
        memory_data = get_courses_memory()
        serializer = CourseSerializer(memory_data, many=True)
        return Response({
            "success": True,
            "count": len(serializer.data),
            "source": "json_in_memory",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """Permite crear una nueva asignatura vinculada a un docente existente."""
        name = request.data.get('name', '').strip()
        teacher_id = request.data.get('teacher_id')
        if not name or not teacher_id:
            return Response({
                "success": False,
                "message": "Se requiere el nombre del curso y el ID del docente asignado."
            }, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            teacher = Teacher.objects.get(id=teacher_id)
            course = Course.objects.create(name=name, teacher=teacher)
            serializer = CourseSerializer(course)
            return Response({
                "success": True,
                "message": "Asignatura creada con éxito.",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        except Teacher.DoesNotExist:
            return Response({
                "success": False,
                "message": f"No se encontró un docente registrado con ID {teacher_id}."
            }, status=status.HTTP_404_NOT_FOUND)


@method_decorator(csrf_exempt, name='dispatch')
class StudentListAPIView(APIView):
    """
    Endpoint: /api/students/
    Métodos: GET, POST
    Descripción: Retorna la lista de estudiantes o matricula a un nuevo estudiante.
    """
    def get(self, request, *args, **kwargs):
        source = request.GET.get('source', '').lower()

        try:
            if source != 'json' and Student.objects.exists():
                students = Student.objects.all()
                serializer = StudentSerializer(students, many=True)
                return Response({
                    "success": True,
                    "count": len(serializer.data),
                    "source": "database_sqlite",
                    "data": serializer.data
                }, status=status.HTTP_200_OK)
        except Exception:
            pass

        memory_data = get_students_memory()
        serializer = StudentSerializer(memory_data, many=True)
        return Response({
            "success": True,
            "count": len(serializer.data),
            "source": "json_in_memory",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """Permite matricular a un nuevo estudiante en la plataforma."""
        first_name = request.data.get('first_name', '').strip()
        last_name = request.data.get('last_name', '').strip()
        if not first_name or not last_name:
            return Response({
                "success": False,
                "message": "Debe proporcionar tanto el nombre como el apellido del estudiante."
            }, status=status.HTTP_400_BAD_REQUEST)
        
        student = Student.objects.create(first_name=first_name, last_name=last_name)
        serializer = StudentSerializer(student)
        return Response({
            "success": True,
            "message": "Estudiante matriculado con éxito.",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)


class StudentCourseListAPIView(APIView):
    """
    Endpoint: /api/enrollments/ (o /api/student-courses/)
    Método: GET
    Descripción: Retorna el detalle de inscripciones de estudiantes en los cursos.
    """
    def get(self, request, *args, **kwargs):
        source = request.GET.get('source', '').lower()

        try:
            if source != 'json' and StudentCourse.objects.exists():
                enrollments = StudentCourse.objects.select_related('student', 'course').all()
                serializer = StudentCourseSerializer(enrollments, many=True)
                return Response({
                    "success": True,
                    "count": len(serializer.data),
                    "source": "database_sqlite",
                    "data": serializer.data
                }, status=status.HTTP_200_OK)
        except Exception:
            pass

        memory_data = get_student_courses_memory()
        serializer = StudentCourseSerializer(memory_data, many=True)
        return Response({
            "success": True,
            "count": len(serializer.data),
            "source": "json_in_memory",
            "data": serializer.data
        }, status=status.HTTP_200_OK)


class AcademicStatsAPIView(APIView):
    """
    Endpoint: /api/stats/
    Método: GET
    Descripción: Retorna métricas generales para los contadores y paneles del dashboard.
    """
    def get(self, request, *args, **kwargs):
        try:
            teachers_count = Teacher.objects.count() if Teacher.objects.exists() else len(get_teachers_memory())
            courses_count = Course.objects.count() if Course.objects.exists() else len(get_courses_memory())
            students_count = Student.objects.count() if Student.objects.exists() else len(get_students_memory())
            enrollments_count = StudentCourse.objects.count() if StudentCourse.objects.exists() else len(get_student_courses_memory())
        except Exception:
            teachers_count = len(get_teachers_memory())
            courses_count = len(get_courses_memory())
            students_count = len(get_students_memory())
            enrollments_count = len(get_student_courses_memory())

        return Response({
            "success": True,
            "stats": {
                "teachers_count": teachers_count,
                "courses_count": courses_count,
                "students_count": students_count,
                "enrollments_count": enrollments_count,
            }
        }, status=status.HTTP_200_OK)
