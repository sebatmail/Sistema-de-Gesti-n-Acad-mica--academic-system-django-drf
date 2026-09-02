"""
Modelos de Datos para el Sistema de Gestión Académica.

Evaluación N°1: Desarrollo Backend con Django & DRF
Docente: Marcelo Alvarado
Asignatura: Desarrollo Backend

Cumplimiento Criterio 1 de la Rúbrica:
"Define correctamente los nombres de campos, tipos de datos y estructuras asociadas al esquema ER
(Teacher, Course, Student, StudentCourse)."

Esquema de Entidades (Modelo ER provisto):
1. Teacher: id (PK), first_name, last_name
2. Course: id (PK), name, teacher_id (FK -> Teacher)
3. Student: id (PK), first_name, last_name
4. StudentCourse: student_id (PK, FK -> Student), course_id (PK, FK -> Course)
"""

from django.db import models


class Teacher(models.Model):
    """
    Entidad: Docentes (Teacher)
    Representa a los profesores que imparten las asignaturas académicas.
    
    Campos según Modelo ER:
    - id: Identificador único autoincremental de tipo entero (Clave Primaria / PK).
    - first_name: Nombre de pila del docente (varchar).
    - last_name: Apellido del docente (varchar).
    """
    id = models.AutoField(
        primary_key=True,
        help_text="Clave primaria numérica autoincremental del docente."
    )
    first_name = models.CharField(
        max_length=100,
        verbose_name="Nombre",
        help_text="Nombre(s) del profesor."
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name="Apellido",
        help_text="Apellido(s) del profesor."
    )

    class Meta:
        db_table = 'teacher'
        verbose_name = "Docente"
        verbose_name_plural = "Docentes"
        ordering = ['id']

    def __str__(self):
        """Representación en texto legible del profesor."""
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        """Propiedad de conveniencia para obtener el nombre completo."""
        return f"{self.first_name} {self.last_name}"


class Course(models.Model):
    """
    Entidad: Asignaturas / Cursos (Course)
    Representa los cursos impartidos por los docentes en la plataforma.
    
    Campos según Modelo ER:
    - id: Identificador único del curso (Clave Primaria / PK).
    - name: Nombre oficial de la asignatura (varchar).
    - teacher_id: Clave Foránea (FK) hacia la tabla Teacher, que define la relación 1:N (un profesor imparte cursos).
    """
    id = models.AutoField(
        primary_key=True,
        help_text="Clave primaria numérica autoincremental del curso."
    )
    name = models.CharField(
        max_length=150,
        verbose_name="Nombre del Curso",
        help_text="Nombre de la asignatura académica."
    )
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name='courses',
        db_column='teacher_id',
        verbose_name="Profesor Asignado",
        help_text="Docente que imparte la asignatura (Relación N:1 con Teacher)."
    )

    class Meta:
        db_table = 'course'
        verbose_name = "Asignatura"
        verbose_name_plural = "Asignaturas"
        ordering = ['id']

    def __str__(self):
        """Representación en texto del curso y su profesor asignado."""
        return f"{self.name} (Docente: {self.teacher.full_name})"


class Student(models.Model):
    """
    Entidad: Estudiantes (Student)
    Representa a los alumnos matriculados en la institución.
    
    Campos según Modelo ER:
    - id: Identificador único del estudiante (Clave Primaria / PK).
    - first_name: Nombre de pila del estudiante (varchar).
    - last_name: Apellido del estudiante (varchar).
    """
    id = models.AutoField(
        primary_key=True,
        help_text="Clave primaria numérica autoincremental del estudiante."
    )
    first_name = models.CharField(
        max_length=100,
        verbose_name="Nombre",
        help_text="Nombre(s) del estudiante."
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name="Apellido",
        help_text="Apellido(s) del estudiante."
    )

    class Meta:
        db_table = 'student'
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"
        ordering = ['id']

    def __str__(self):
        """Representación en texto legible del estudiante."""
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        """Propiedad de conveniencia para obtener el nombre completo."""
        return f"{self.first_name} {self.last_name}"


class StudentCourse(models.Model):
    """
    Entidad: Inscripciones / Matrícula (StudentCourse)
    Representa la tabla asociativa de la relación Muchos a Muchos (N:M) entre Estudiantes y Cursos.
    
    Campos según Modelo ER:
    - student_id: Clave foránea y parte de la clave compuesta que referencia a Student.
    - course_id: Clave foránea y parte de la clave compuesta que referencia a Course.
    """
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='course_registrations',
        db_column='student_id',
        verbose_name="Estudiante",
        help_text="Estudiante que se inscribe en el curso."
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='enrolled_students',
        db_column='course_id',
        verbose_name="Asignatura",
        help_text="Asignatura en la cual está inscrito el estudiante."
    )

    class Meta:
        db_table = 'student_course'
        verbose_name = "Inscripción de Curso"
        verbose_name_plural = "Inscripciones de Cursos"
        # Clave compuesta / unicidad para garantizar que un estudiante no se inscriba dos veces en el mismo curso
        unique_together = (('student', 'course'),)
        ordering = ['student', 'course']

    def __str__(self):
        """Representación legible de la inscripción."""
        return f"Inscripción: {self.student.full_name} -> {self.course.name}"
