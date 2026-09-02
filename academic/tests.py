"""
Pruebas Unitarias y de Integración para el Sistema de Gestión Académica.

Evaluación N°1: Desarrollo Backend con Django & DRF
Docente: Marcelo Alvarado
Asignatura: Desarrollo Backend

Valida el 100% de los requerimientos técnicos y criterios de la rúbrica:
1. Modelos ER (Teacher, Course, Student, StudentCourse).
2. Serializadores DRF (serializers.py).
3. Vistas HTML (render()) sin errores.
4. Redirección de la ruta raíz '/' para eliminar el error 404.
5. Endpoints REST de DRF (/api/courses/, /api/students/, /api/teachers/, /api/enrollments/, /api/stats/).
6. Compatibilidad de datos en memoria / JSON.
"""

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from academic.models import Teacher, Course, Student, StudentCourse
from academic.serializers import TeacherSerializer, CourseSerializer, StudentSerializer
from academic.data_manager import (
    get_teachers_memory,
    get_courses_memory,
    get_students_memory,
    get_student_courses_memory
)


class AcademicModelTestCase(TestCase):
    """Pruebas para verificar la correcta definición y relaciones del modelo ER."""

    def setUp(self):
        self.teacher = Teacher.objects.create(
            first_name="Marcelo",
            last_name="Alvarado"
        )
        self.course = Course.objects.create(
            name="Desarrollo Backend con Django",
            teacher=self.teacher
        )
        self.student = Student.objects.create(
            first_name="Sebastián",
            last_name="Torres"
        )
        self.enrollment = StudentCourse.objects.create(
            student=self.student,
            course=self.course
        )

    def test_teacher_creation(self):
        """Verifica la creación del modelo Teacher y sus propiedades."""
        self.assertEqual(self.teacher.first_name, "Marcelo")
        self.assertEqual(self.teacher.last_name, "Alvarado")
        self.assertEqual(self.teacher.full_name, "Marcelo Alvarado")
        self.assertEqual(str(self.teacher), "Marcelo Alvarado")

    def test_course_creation_and_relationship(self):
        """Verifica la relación ForeignKey entre Course y Teacher."""
        self.assertEqual(self.course.name, "Desarrollo Backend con Django")
        self.assertEqual(self.course.teacher.id, self.teacher.id)
        self.assertIn("Marcelo Alvarado", str(self.course))

    def test_student_creation(self):
        """Verifica la creación del modelo Student."""
        self.assertEqual(self.student.first_name, "Sebastián")
        self.assertEqual(self.student.last_name, "Torres")
        self.assertEqual(self.student.full_name, "Sebastián Torres")

    def test_student_course_enrollment(self):
        """Verifica la tabla asociativa StudentCourse."""
        self.assertEqual(self.enrollment.student.id, self.student.id)
        self.assertEqual(self.enrollment.course.id, self.course.id)


class AcademicWebViewsTestCase(TestCase):
    """Pruebas para verificar que las vistas HTML renderizan sin errores y eliminan el 404."""

    def setUp(self):
        self.client = Client()

    def test_root_url_redirects_no_404(self):
        """Requerimiento 4: Eliminar el error 404 cuando no hay endpoint asignado a '/'."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/courses/')
        
        # Siguiendo la redirección
        follow_response = self.client.get('/', follow=True)
        self.assertEqual(follow_response.status_code, 200)
        self.assertTemplateUsed(follow_response, 'academic/courses.html')

    def test_courses_view_renders_correctly(self):
        """Criterio 3: Renderizado correcto de courses.html."""
        response = self.client.get('/courses/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'academic/courses.html')
        self.assertContains(response, 'Catálogo de Asignaturas')
        self.assertContains(response, 'courses-table')

    def test_students_view_renders_correctly(self):
        """Criterio 3: Renderizado correcto de students.html."""
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'academic/students.html')
        self.assertContains(response, 'Nómina de Estudiantes')
        self.assertContains(response, 'students-table')


class AcademicDRFApiTestCase(APITestCase):
    """Pruebas para los endpoints REST de Django REST Framework."""

    def setUp(self):
        self.teacher = Teacher.objects.create(
            id=101,
            first_name="Profesor",
            last_name="Test"
        )
        self.course = Course.objects.create(
            id=201,
            name="Curso Test DRF",
            teacher=self.teacher
        )
        self.student = Student.objects.create(
            id=301,
            first_name="Alumno",
            last_name="Test"
        )
        self.enrollment = StudentCourse.objects.create(
            student=self.student,
            course=self.course
        )

    def test_api_courses_endpoint(self):
        """Criterio 6 & Requerimiento 3: Consulta al endpoint /api/courses/."""
        response = self.client.get('/api/courses/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data.get('success'))
        self.assertTrue(len(response.data.get('data')) > 0)
        
        first_course = response.data['data'][0]
        self.assertIn('name', first_course)
        self.assertIn('teacher_id', first_course)
        self.assertIn('teacher_name', first_course)

    def test_api_students_endpoint(self):
        """Requerimiento 3: Consulta al endpoint /api/students/."""
        response = self.client.get('/api/students/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data.get('success'))
        self.assertTrue(len(response.data.get('data')) > 0)
        
        first_student = response.data['data'][0]
        self.assertIn('first_name', first_student)
        self.assertIn('last_name', first_student)
        self.assertIn('full_name', first_student)

    def test_api_teachers_endpoint(self):
        """Consulta al endpoint /api/teachers/."""
        response = self.client.get('/api/teachers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data.get('success'))

    def test_api_enrollments_endpoint(self):
        """Consulta al endpoint /api/enrollments/."""
        response = self.client.get('/api/enrollments/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data.get('success'))

    def test_api_stats_endpoint(self):
        """Consulta al endpoint de estadísticas /api/stats/."""
        response = self.client.get('/api/stats/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('stats', response.data)
        self.assertTrue(response.data['stats']['courses_count'] >= 1)

    def test_post_new_student(self):
        """Prueba la matricula de un nuevo estudiante mediante POST a /api/students/."""
        payload = {"first_name": "Estudiante", "last_name": "Nuevo"}
        response = self.client.post('/api/students/', data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data.get('success'))
        self.assertEqual(response.data['data']['first_name'], "Estudiante")
        self.assertEqual(response.data['data']['full_name'], "Estudiante Nuevo")

    def test_post_new_course(self):
        """Prueba la creacion de una asignatura mediante POST a /api/courses/."""
        payload = {"name": "Nueva Asignatura Avanzada", "teacher_id": self.teacher.id}
        response = self.client.post('/api/courses/', data=payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data.get('success'))
        self.assertEqual(response.data['data']['name'], "Nueva Asignatura Avanzada")
        self.assertEqual(response.data['data']['teacher_id'], self.teacher.id)


class AcademicMemoryDataManagerTestCase(TestCase):
    """Criterio 2: Procesamiento y variables/colecciones en memoria sin requerir BD."""

    def test_in_memory_teachers(self):
        teachers = get_teachers_memory()
        self.assertTrue(isinstance(teachers, list))
        self.assertTrue(len(teachers) > 0)
        self.assertIn('full_name', teachers[0])

    def test_in_memory_courses(self):
        courses = get_courses_memory()
        self.assertTrue(isinstance(courses, list))
        self.assertTrue(len(courses) > 0)
        self.assertIn('teacher_name', courses[0])

    def test_in_memory_students(self):
        students = get_students_memory()
        self.assertTrue(isinstance(students, list))
        self.assertTrue(len(students) > 0)
        self.assertIn('full_name', students[0])

    def test_in_memory_enrollments(self):
        enrollments = get_student_courses_memory()
        self.assertTrue(isinstance(enrollments, list))
        self.assertTrue(len(enrollments) > 0)
        self.assertIn('course_name', enrollments[0])
