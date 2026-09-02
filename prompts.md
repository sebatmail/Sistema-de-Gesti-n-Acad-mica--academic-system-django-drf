# Entregable de Inteligencia Artificial: Registro de Prompts

**Evaluación N°1: Desarrollo Backend con Django & DRF**  
**Asignatura:** Desarrollo Backend  
**Docente:** Marcelo Alvarado  
**Estudiante:** Sebastián Torres  

> [!NOTE]
> Este archivo cumple estrictamente con el **Requerimiento Técnico 5** y el **Criterio 8** de la rúbrica de evaluación.
> Para la relación completa de habilidades (skills) aplicadas y el repositorio de origen (`https://github.com/garri333/Skills.git`), consultar el archivo complementario [`prompts & skills.md`](file:///c:/Users/laboratorio8/Desktop/EVA%201%20BACKEND/prompts%20&%20skills.md).

---

## 1. Prompt 1: Generación de la Estructura de Datos Simulada en JSON

### Prompt Utilizado:
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

### Respuesta Generada por la IA:
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

## 2. Prompt 2: Diseño de Plantillas y Maquetación con HTML5 & Bootstrap 5.3 CDN

### Prompt Utilizado:
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

### Respuesta Generada por la IA:
*(Generación integral del marcado HTML con clases semánticas de Bootstrap 5.3, integración con CDN, tipografía moderna, estados de carga y feedback visual implementados en `templates/academic/base.html`, `templates/academic/courses.html` y `templates/academic/students.html`)*.

---

## 3. Prompt 3: Lógica Asíncrona con JavaScript `fetch()` para Enmascaramiento

### Prompt Utilizado:
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

### Respuesta Generada por la IA:
*(Generación de los scripts asíncronos en Vanilla JavaScript con `async/await`, control de excepciones con `try/catch`, inyección en el DOM e interactividad reactiva en tiempo real)*.
