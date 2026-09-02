# Registro de Prompts & Skills - Evaluación N°1: Backend con Django & DRF

**Asignatura:** Desarrollo Backend  
**Docente:** Marcelo Alvarado  
**Estudiante:** Sebastián Torres  
**Ponderación:** 15% de la nota final  

---

## 1. Repositorio de Descarga de Skills

Todas las habilidades (skills) fueron descargadas directamente desde el repositorio oficial:
- **URL del Repositorio:** `https://github.com/garri333/Skills.git`
- **Rama:** `master`
- **Ubicación local en el proyecto:** `./Skills_Repo/Skills-master/`

---

## 2. Skills Utilizadas y su Aplicación en la EVA 1

A continuación se detalla la nómina de habilidades aplicadas para la resolución de cada requerimiento de la pauta de evaluación:

| Categoría | Habilidad (Skill) | Aplicación en la Evaluación N°1 |
| :--- | :--- | :--- |
| **03-backend-api** | `api-design` | Diseño de la arquitectura RESTful de los endpoints (`/api/courses/`, `/api/students/`, `/api/teachers/`, `/api/enrollments/`), estandarización de payloads JSON, uso adecuado de verbos HTTP y códigos de estado (`200 OK`, `400 Bad Request`, `404 Not Found`). |
| **02-frontend-design** | `frontend-design` | Maquetación limpia y semántica en HTML5 (`base.html`, `courses.html`, `students.html`), tarjetas de contenido con sombras sutiles, espaciado armónico y tipografía moderna. |
| **02-frontend-design** | `uiux-pro` | Experiencia de usuario en el "enmascaramiento": implementación de indicadores de carga (spinners de Bootstrap) mientras `fetch()` consulta la API, cajas de alerta ante fallos de conexión y estados vacíos (*empty states*). |
| **02-frontend-design** | `web-design-guidelines` | Implementación responsiva mediante Bootstrap 5.3 CDN, barra de navegación interactiva (*sticky navbar*), compatibilidad móvil y accesibilidad web. |
| **13-anthropic** | `theme-factory` | Definición de una paleta cromática profesional para la plataforma académica: tonos azul profundo (*navy/slate*) para la navegación, acentos cian/info para estudiantes y verde esmeralda para asignaturas activas. |
| **04-ai-agents** | `coding-agent` | Estructuración modular y desacoplada del cascarón frontend y backend en Django (`academic_project` y app `academic`). |
| **04-ai-agents** | `prompt-engineering` | Formulación precisa de prompts con roles, restricciones técnicas y formatos de salida estructurados para generar datos simulados y plantillas. |
| **05-devops-git** | `git-conventional-commits` | Estructura de control de versiones, configuración de `.gitignore` y guía de commits semánticos (`feat:`, `fix:`, `docs:`, `test:`). |
| **19-testing-quality** | `code-quality-audit` | Aseguramiento de código 100% comentado ("full comentado") según el Criterio 9, con explicaciones pedagógicas en cada función, modelo, vista y script JS. |
| **19-testing-quality** | `systematic-debugging` | Suite de 16 pruebas unitarias e integración en `academic/tests.py` para validar modelos, serializadores, vistas HTML y respuestas de la API sin errores de ejecución. |
| **21-productivity** | `codebase-health-reporter` | Generación de documentación técnica exhaustiva en `README.md`, matriz de trazabilidad con la rúbrica y balotario de defensa oral. |

---

## 3. Prompts Exactos y Respuestas de Inteligencia Artificial

Cumpliendo con la **Sección III.5** y el **Criterio 8** de la pauta de evaluación:

### Prompt 1: Generación de Datos de Prueba en Formato JSON
**Herramienta Utilizada:** Google Gemini 3.8 Flash (DeepMind) / Claude  
**Objetivo:** Generar un conjunto realista de datos simulados en formato JSON que cumpla fielmente con el modelo entidad-relación entregado (Teacher, Course, Student, StudentCourse).

#### Texto Exacto del Prompt:
```text
Actúa como un arquitecto de datos backend. Necesito que generes un archivo JSON estructurado de prueba llamado `academic_data.json` para una plataforma académica universitaria en Django.

El esquema debe respetar estrictamente el siguiente modelo ER:
1. teacher (id: int, first_name: str, last_name: str)
2. course (id: int, name: str, teacher_id: int - FK hacia teacher)
3. student (id: int, first_name: str, last_name: str)
4. student_course (student_id: int, course_id: int - FKs e inscripciones)

Requisitos:
- 5 docentes con nombres y apellidos chilenos/latinos realistas.
- Al menos 6 asignaturas tecnológicas actuales (Backend con Django, Bases de Datos, Microservicios, IA, Cloud, Algoritmos).
- Al menos 8 estudiantes inscritos.
- Al menos 12 relaciones en student_course que vinculen lógicamente a los estudiantes con los cursos.
- Formato JSON estrictamente válido, indentado a 2 espacios.
```

#### Respuesta Generada por la IA:
```json
{
  "teachers": [
    { "id": 1, "first_name": "Marcelo", "last_name": "Alvarado" },
    { "id": 2, "first_name": "Carolina", "last_name": "Herrera" },
    { "id": 3, "first_name": "Roberto", "last_name": "Gómez" },
    { "id": 4, "first_name": "Andrea", "last_name": "Valenzuela" },
    { "id": 5, "first_name": "Felipe", "last_name": "Soto" }
  ],
  "courses": [
    { "id": 1, "name": "Desarrollo Backend con Django & DRF", "teacher_id": 1 },
    { "id": 2, "name": "Modelamiento y Arquitectura de Bases de Datos", "teacher_id": 2 },
    { "id": 3, "name": "Arquitectura de Software y Microservicios", "teacher_id": 3 },
    { "id": 4, "name": "Inteligencia Artificial y Machine Learning Aplicado", "teacher_id": 4 },
    { "id": 5, "name": "Computación en la Nube y DevOps", "teacher_id": 5 },
    { "id": 6, "name": "Programación Avanzada y Algoritmos en Python", "teacher_id": 1 }
  ],
  "students": [
    { "id": 1, "first_name": "Sebastián", "last_name": "Torres" },
    { "id": 2, "first_name": "Sofía", "last_name": "Contreras" },
    { "id": 3, "first_name": "Benjamín", "last_name": "Muñoz" },
    { "id": 4, "first_name": "Valentina", "last_name": "Rojas" },
    { "id": 5, "first_name": "Lucas", "last_name": "Morales" },
    { "id": 6, "first_name": "Camila", "last_name": "Silva" },
    { "id": 7, "first_name": "Joaquín", "last_name": "Castro" },
    { "id": 8, "first_name": "Martina", "last_name": "Araya" }
  ],
  "student_courses": [
    { "student_id": 1, "course_id": 1 },
    { "student_id": 1, "course_id": 3 },
    { "student_id": 2, "course_id": 1 },
    { "student_id": 2, "course_id": 4 },
    { "student_id": 3, "course_id": 2 },
    { "student_id": 3, "course_id": 5 },
    { "student_id": 4, "course_id": 1 },
    { "student_id": 4, "course_id": 6 },
    { "student_id": 5, "course_id": 3 },
    { "student_id": 6, "course_id": 4 },
    { "student_id": 7, "course_id": 5 },
    { "student_id": 8, "course_id": 1 }
  ]
}
```

---

### Prompt 2: Diseño de Plantillas HTML y Maquetación con Bootstrap 5.3 CDN
**Herramienta Utilizada:** Google Gemini 3.8 Flash / Copilot  
**Objetivo:** Crear la plantilla maestra `base.html` y las vistas `courses.html` y `students.html` para cumplir con el enmascaramiento visual de la API.

#### Texto Exacto del Prompt:
```text
Actúa como un Diseñador Frontend UI/UX experto. Necesito la estructura HTML5 completa para las plantillas de una aplicación Django (`templates/academic/`):
1. `base.html`:
   - Enlazar Bootstrap 5.3 CDN (CSS y JS Bundle).
   - Enlazar Bootstrap Icons CDN.
   - Barra de navegación moderna en color oscuro con enlaces a 'Asignaturas y Cursos' (`/courses/`) y 'Estudiantes' (`/students/`), y menú desplegable para probar los endpoints de la API.
   - Bloques Django: `{% block title %}`, `{% block content %}`, `{% block scripts %}`.
   - Pie de página institucional.
2. `courses.html` (extiende base.html):
   - Muestra el listado de Cursos y su Profesor Asignado.
   - Debe contener un spinner de carga (`<div id="loading-spinner">`), caja de error oculta (`<div id="error-box">`), y la tabla responsive `#courses-table` con columnas: ID, Asignatura, ID Docente, Profesor Asignado, Estado.
   - Botón de recarga y contador badge.
3. `students.html` (extiende base.html):
   - Muestra el listado de Estudiantes.
   - Debe incluir un campo de búsqueda en tiempo real (`<input id="search-student-input">`) que filtre dinámicamente.
   - Tabla `#students-table` con columnas: ID, Nombre, Apellido, Nombre Completo, Condición.

Todo debe estar estilizado profesionalmente y completamente comentado.
```

#### Respuesta Generada por la IA:
*(La IA generó el código completo HTML5 con componentes de Bootstrap 5.3, badges interactivos, alertas de error dinámicas y estructura semántica que fue integrada directamente en `templates/academic/base.html`, `templates/academic/courses.html` y `templates/academic/students.html`)*.

---

### Prompt 3: Implementación de Peticiones Asíncronas con JavaScript `fetch()`
**Herramienta Utilizada:** Google Gemini 3.8 Flash  
**Objetivo:** Desarrollar el script de JavaScript Vanilla que consuma asíncronamente los endpoints `/api/courses/` y `/api/students/` para poblar el DOM sin recargar la página ("enmascaramiento").

#### Texto Exacto del Prompt:
```text
Actúa como desarrollador frontend especialista en JavaScript asíncrono.
Escribe el código JavaScript Vanilla para las plantillas `courses.html` y `students.html` de Django que cumpla con el requerimiento de 'enmascaramiento de endpoints REST'.

Requisitos funcionales:
1. Usar la API estándar `fetch()` con `async/await`.
2. Consumir `/api/courses/` y `/api/students/`.
3. Manejo de estados de interfaz:
   - Mostrar el spinner mientras la promesa de fetch está pendiente.
   - Ocultar el spinner al recibir la respuesta.
   - Si la respuesta es HTTP 200, deserializar JSON (`await response.json()`) y construir las filas `<tr>` e inyectarlas dinámicamente en el `<tbody>`.
   - Si hay un error de red o HTTP, capturarlo con try/catch, ocultar la tabla y mostrar una alerta descriptiva en `#error-box`.
4. En `students.html`, agregar un event listener 'input' al buscador para filtrar reactivamente en el cliente sin realizar peticiones extra al servidor.
5. Código 100% comentado línea por línea con fines pedagógicos para la evaluación.
```

#### Respuesta Generada por la IA:
*(La IA proveyó las funciones `loadCoursesAsync()` y `loadStudentsAsync()`, con manejo robusto de `try/catch/finally`, creación dinámica de elementos del DOM mediante `document.createElement('tr')`, template literals y sanitización de campos, tal como se encuentra implementado en el bloque `{% block scripts %}` de ambas plantillas)*.

---

### Prompt 4: Arquitectura Híbrida de Serializadores y Soporte sin Base de Datos
**Herramienta Utilizada:** Google Gemini 3.8 Flash  
**Objetivo:** Diseñar los serializadores DRF y las vistas de forma tal que cumplan con el Criterio 2 ("Estructura adecuadamente las variables y colecciones necesarias para simular o procesar los datos JSON sin requerir la base de datos") y con el Criterio 1 y 6 (Modelos ORM y ModelSerializer).

#### Texto Exacto del Prompt:
```text
Actúa como desarrollador Django & DRF Senior. En la pauta de evaluación se exigen dos indicadores complementarios:
1. Definir correctamente los modelos de datos acordes al modelo ER (Teacher, Course, Student, StudentCourse).
2. Estructurar variables y colecciones necesarias para simular o procesar los datos JSON sin requerir la base de datos.
3. Serializadores de DRF para mapear adecuadamente las entidades.

¿Cómo podemos estructurar `serializers.py`, `data_manager.py` y `views.py` para que los endpoints de DRF funcionen tanto si se migra y usa la base de datos relacional SQLite, como si se consumen directamente las colecciones en memoria desde `academic_data.json`?

Entrega el código de los serializadores con `SerializerMethodField` para calcular nombres completos y nombres de docentes asignados, y la lógica en las vistas de APIView con fallback automático.
```

#### Respuesta Generada por la IA:
*(La IA proporcionó la arquitectura implementada en `academic/serializers.py`, `academic/data_manager.py` y `academic/views.py`, donde `CourseSerializer` calcula `teacher_name` tanto desde una instancia ORM como desde un diccionario de Python, y las vistas `APIView` consultan la base de datos relacional si existen registros, o devuelven de forma transparente las colecciones procesadas en memoria si la base de datos no está migrada o se solicita mediante `?source=json`)*.

---

## 4. Conclusión sobre el Uso de Inteligencia Artificial

El uso guiado de Inteligencia Artificial, asistido por las pautas y mejores prácticas de las **Skills** descargadas de `https://github.com/garri333/Skills.git`, permitió:
1. Acelerar el desarrollo cumpliendo rigurosamente el tiempo asignado de 90 minutos.
2. Garantizar la total ausencia de errores de sintaxis o de ejecución (16/16 pruebas superadas).
3. Desarrollar una interfaz de usuario estilizada con Bootstrap 5.3 que cumple con altos estándares de usabilidad (UI/UX).
4. Mantener una documentación limpia y estructurada para la defensa técnica.
