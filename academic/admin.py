"""
Configuración del Panel de Administración de Django.

Evaluación N°1: Desarrollo Backend con Django & DRF
Docente: Marcelo Alvarado
Asignatura: Desarrollo Backend

Registra los modelos Teacher, Course, Student y StudentCourse en el Django Admin
con interfaces personalizadas, filtros y columnas de búsqueda.
"""

from django.contrib import admin
from academic.models import Teacher, Course, Student, StudentCourse


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'full_name')
    search_fields = ('first_name', 'last_name')
    ordering = ('id',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'teacher', 'get_teacher_name')
    search_fields = ('name', 'teacher__first_name', 'teacher__last_name')
    list_filter = ('teacher',)
    ordering = ('id',)

    def get_teacher_name(self, obj):
        return obj.teacher.full_name if obj.teacher else "Sin asignar"
    get_teacher_name.short_description = "Profesor Asignado"


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'full_name')
    search_fields = ('first_name', 'last_name')
    ordering = ('id',)


@admin.register(StudentCourse)
class StudentCourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'course')
    list_filter = ('course',)
    search_fields = ('student__first_name', 'student__last_name', 'course__name')
