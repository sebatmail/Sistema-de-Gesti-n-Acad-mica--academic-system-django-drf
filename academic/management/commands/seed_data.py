"""
Comando personalizado de gestión de Django: seed_data

Permite precargar los datos de prueba desde academic/data/academic_data.json
hacia la base de datos relacional SQLite de forma sencilla:
python manage.py seed_data
"""

from django.core.management.base import BaseCommand
from academic.data_manager import seed_database_from_json


class Command(BaseCommand):
    help = "Precarga los datos ficticios desde el archivo JSON a la base de datos relacional."

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE("Iniciando precarga de datos académicos desde JSON..."))
        results = seed_database_from_json()
        self.stdout.write(
            self.style.SUCCESS(
                f"Precarga exitosa:\n"
                f" - {results['teachers']} Docentes registrados\n"
                f" - {results['courses']} Cursos registrados\n"
                f" - {results['students']} Estudiantes registrados\n"
                f" - {results['enrollments']} Inscripciones registradas"
            )
        )
