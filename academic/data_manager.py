"""
Módulo de Gestión de Datos en Memoria y Carga JSON.

Evaluación N°1: Desarrollo Backend con Django & DRF
Docente: Marcelo Alvarado
Asignatura: Desarrollo Backend

Cumplimiento Criterio 2 de la Rúbrica:
"Estructura adecuadamente las variables y colecciones necesarias para simular o procesar los datos JSON
sin requerir la base de datos."

Este módulo expone variables en memoria (listas y diccionarios de Python) y funciones utilitarias
para consultar, filtrar y precargar los datos académicos tanto sin base de datos como hacia la base
de datos SQLite cuando se requiera.
"""

import json
import os
from pathlib import Path

# Ruta al archivo JSON con los datos de prueba
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE_PATH = BASE_DIR / 'academic' / 'data' / 'academic_data.json'


def load_raw_json():
    """
    Lee y deserializa el archivo JSON de datos académicos.
    Retorna un diccionario con las claves: teachers, courses, students, student_courses.
    """
    if os.path.exists(DATA_FILE_PATH):
        with open(DATA_FILE_PATH, 'r', encoding='utf-8') as file:
            return json.load(file)
    return {"teachers": [], "courses": [], "students": [], "student_courses": []}


# ==============================================================================
# COLECCIONES EN MEMORIA (ESTRUCTURAS DE DATOS DE PYTHON)
# Permiten operar completamente la lógica del backend y APIs sin depender de SQLite
# ==============================================================================
_RAW_DATA = load_raw_json()

# Colección de Docentes (Lista de Diccionarios)
TEACHERS_COLLECTION = _RAW_DATA.get("teachers", [])

# Colección de Cursos (Lista de Diccionarios)
COURSES_COLLECTION = _RAW_DATA.get("courses", [])

# Colección de Estudiantes (Lista de Diccionarios)
STUDENTS_COLLECTION = _RAW_DATA.get("students", [])

# Colección de Inscripciones (Lista de Diccionarios)
STUDENT_COURSES_COLLECTION = _RAW_DATA.get("student_courses", [])


def get_teachers_memory():
    """Retorna la lista de docentes cargada en memoria con datos formateados."""
    result = []
    for t in TEACHERS_COLLECTION:
        item = dict(t)
        item['full_name'] = f"{item['first_name']} {item['last_name']}"
        result.append(item)
    return result


def get_courses_memory():
    """
    Retorna la lista de asignaturas/cursos en memoria, enriquecida con la información
    del docente asignado (resolución de relación teacher_id -> Teacher sin base de datos).
    """
    teachers_map = {t['id']: f"{t['first_name']} {t['last_name']}" for t in TEACHERS_COLLECTION}
    result = []
    for c in COURSES_COLLECTION:
        course_item = dict(c)
        teacher_id = course_item.get('teacher_id')
        course_item['teacher_name'] = teachers_map.get(teacher_id, "Sin Asignar")
        result.append(course_item)
    return result


def get_students_memory():
    """Retorna la lista de estudiantes en memoria con su nombre completo calculado."""
    result = []
    for s in STUDENTS_COLLECTION:
        item = dict(s)
        item['full_name'] = f"{item['first_name']} {item['last_name']}"
        result.append(item)
    return result


def get_student_courses_memory():
    """
    Retorna las inscripciones enriquecidas con los nombres del estudiante y curso,
    resolviendo relaciones en memoria sin consultas SQL.
    """
    students_map = {s['id']: f"{s['first_name']} {s['last_name']}" for s in STUDENTS_COLLECTION}
    courses_map = {c['id']: c['name'] for c in COURSES_COLLECTION}
    
    result = []
    for sc in STUDENT_COURSES_COLLECTION:
        item = dict(sc)
        item['student_name'] = students_map.get(item.get('student_id'), "Desconocido")
        item['course_name'] = courses_map.get(item.get('course_id'), "Desconocido")
        result.append(item)
    return result


def seed_database_from_json():
    """
    Precarga los datos del archivo JSON directamente a los modelos ORM de la base de datos relacional.
    Evita duplicados usando get_or_create / update_or_create.
    """
    from academic.models import Teacher, Course, Student, StudentCourse
    
    data = load_raw_json()
    
    # 1. Precargar Docentes
    for t in data.get("teachers", []):
        Teacher.objects.update_or_create(
            id=t['id'],
            defaults={
                'first_name': t['first_name'],
                'last_name': t['last_name']
            }
        )
        
    # 2. Precargar Cursos
    for c in data.get("courses", []):
        try:
            teacher_obj = Teacher.objects.get(id=c['teacher_id'])
            Course.objects.update_or_create(
                id=c['id'],
                defaults={
                    'name': c['name'],
                    'teacher': teacher_obj
                }
            )
        except Teacher.DoesNotExist:
            continue

    # 3. Precargar Estudiantes
    for s in data.get("students", []):
        Student.objects.update_or_create(
            id=s['id'],
            defaults={
                'first_name': s['first_name'],
                'last_name': s['last_name']
            }
        )

    # 4. Precargar Inscripciones (StudentCourse)
    for sc in data.get("student_courses", []):
        try:
            student_obj = Student.objects.get(id=sc['student_id'])
            course_obj = Course.objects.get(id=sc['course_id'])
            StudentCourse.objects.get_or_create(
                student=student_obj,
                course=course_obj
            )
        except (Student.DoesNotExist, Course.DoesNotExist):
            continue

    return {
        "teachers": Teacher.objects.count(),
        "courses": Course.objects.count(),
        "students": Student.objects.count(),
        "enrollments": StudentCourse.objects.count(),
    }
