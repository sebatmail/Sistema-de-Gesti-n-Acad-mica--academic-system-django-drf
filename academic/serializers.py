"""
Serializadores de Django REST Framework (DRF).

Evaluación N°1: Desarrollo Backend con Django & DRF
Docente: Marcelo Alvarado
Asignatura: Desarrollo Backend

Cumplimiento Criterio 6 de la Rúbrica:
"Crea los serializadores de DRF (serializers.py) para mapear adecuadamente las entidades requeridas."

Los serializadores permiten convertir instancias de modelos ORM y estructuras de datos nativas (diccionarios/listas)
en representaciones JSON para ser consumidas por las vistas web y clientes API REST.
"""

from rest_framework import serializers
from academic.models import Teacher, Course, Student, StudentCourse


class TeacherSerializer(serializers.ModelSerializer):
    """
    Serializador para la entidad Docente (Teacher).
    Mapea los campos id, first_name, last_name e incluye el campo calculado full_name.
    """
    full_name = serializers.SerializerMethodField(
        help_text="Nombre completo concatenado del docente."
    )

    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'full_name']
        read_only_fields = ['id', 'full_name']

    def get_full_name(self, obj):
        """Retorna el nombre completo tanto si obj es una instancia de Modelo como si es un diccionario."""
        if isinstance(obj, dict):
            return f"{obj.get('first_name', '')} {obj.get('last_name', '')}".strip()
        return f"{obj.first_name} {obj.last_name}".strip()


class CourseSerializer(serializers.ModelSerializer):
    """
    Serializador para la entidad Asignatura / Curso (Course).
    Mapea los campos del modelo ER:
    - id
    - name
    - teacher_id (Foreign Key hacia Teacher)
    - teacher_name: Campo extendido para presentar el nombre del docente asignado directamente en la interfaz.
    """
    teacher_id = serializers.IntegerField(
        source='teacher.id',
        read_only=True,
        help_text="Identificador único del docente asociado (Clave Foránea)."
    )
    teacher_name = serializers.SerializerMethodField(
        help_text="Nombre completo del profesor asignado al curso."
    )

    class Meta:
        model = Course
        fields = ['id', 'name', 'teacher_id', 'teacher_name']
        read_only_fields = ['id', 'teacher_id', 'teacher_name']

    def get_teacher_name(self, obj):
        """Obtiene el nombre del docente asignado para facilitar la visualización en courses.html."""
        if isinstance(obj, dict):
            return obj.get('teacher_name', 'Docente no asignado')
        if obj.teacher:
            return f"{obj.teacher.first_name} {obj.teacher.last_name}"
        return "Docente no asignado"

    def to_representation(self, instance):
        """Asegura compatibilidad tanto con instancias de modelos como con diccionarios en memoria."""
        if isinstance(instance, dict):
            return {
                'id': instance.get('id'),
                'name': instance.get('name'),
                'teacher_id': instance.get('teacher_id'),
                'teacher_name': instance.get('teacher_name', 'Docente no asignado'),
            }
        return super().to_representation(instance)


class StudentSerializer(serializers.ModelSerializer):
    """
    Serializador para la entidad Estudiante (Student).
    Mapea los campos id, first_name, last_name e incluye el campo calculado full_name.
    """
    full_name = serializers.SerializerMethodField(
        help_text="Nombre y apellido concatenados del estudiante."
    )

    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'full_name']
        read_only_fields = ['id', 'full_name']

    def get_full_name(self, obj):
        """Calcula el nombre completo del estudiante."""
        if isinstance(obj, dict):
            return f"{obj.get('first_name', '')} {obj.get('last_name', '')}".strip()
        return f"{obj.first_name} {obj.last_name}".strip()


class StudentCourseSerializer(serializers.ModelSerializer):
    """
    Serializador para la tabla asociativa de Inscripciones (StudentCourse).
    Mapea la relación estudiante-curso con información descriptiva de ambas entidades.
    """
    student_id = serializers.IntegerField(source='student.id', read_only=True)
    course_id = serializers.IntegerField(source='course.id', read_only=True)
    student_name = serializers.SerializerMethodField()
    course_name = serializers.SerializerMethodField()

    class Meta:
        model = StudentCourse
        fields = ['student_id', 'course_id', 'student_name', 'course_name']

    def get_student_name(self, obj):
        if isinstance(obj, dict):
            return obj.get('student_name', 'Desconocido')
        return obj.student.full_name if obj.student else 'Desconocido'

    def get_course_name(self, obj):
        if isinstance(obj, dict):
            return obj.get('course_name', 'Desconocido')
        return obj.course.name if obj.course else 'Desconocido'
