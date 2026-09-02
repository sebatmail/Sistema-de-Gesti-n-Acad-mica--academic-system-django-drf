"""
Django settings for academic_project project.

Evaluación N°1: Desarrollo Backend con Django & DRF
Docente: Marcelo Alvarado
Asignatura: Desarrollo Backend

Configuración global del proyecto:
- Integración de Django REST Framework (DRF)
- Configuración de la aplicación 'academic'
- Rutas de plantillas (templates) para enmascaramiento de API con HTML/Bootstrap
- Parámetros de base de datos relacional SQLite
- Formateo y soporte en español
"""

from pathlib import Path
import os

# Ruta base del proyecto (apunta a la raíz del repositorio donde reside manage.py)
BASE_DIR = Path(__file__).resolve().parent.parent

# Clave secreta para propósitos de desarrollo (en producción debe mantenerse en variables de entorno)
SECRET_KEY = 'django-insecure-academic-backend-eva1-marcelo-alvarado-evaluation'

# Modo depuración activo para visualizar trazas y errores durante la fase de desarrollo
DEBUG = True

# Hosts permitidos para servir la aplicación localmente
ALLOWED_HOSTS = ['*']


# ==============================================================================
# DEFINICIÓN DE APLICACIONES INSTALADAS
# ==============================================================================
INSTALLED_APPS = [
    # Aplicaciones nativas del núcleo de Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Paquete externo: Django REST Framework (Criterio 5 de la rúbrica)
    'rest_framework',

    # Aplicación local del dominio académico (Criterio 1 de la rúbrica)
    'academic',
]

# ==============================================================================
# MIDDLEWARE
# ==============================================================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'academic_project.urls'

# ==============================================================================
# CONFIGURACIÓN DE PLANTILLAS (TEMPLATES)
# ==============================================================================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Directorio global de plantillas 'templates/' ubicado en la raíz del proyecto
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'academic_project.wsgi.application'


# ==============================================================================
# CONFIGURACIÓN DE BASE DE DATOS RELACIONAL (SQLite para Unidad 1)
# ==============================================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ==============================================================================
# VALIDACIÓN DE CONTRASEÑAS
# ==============================================================================
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# ==============================================================================
# INTERNACIONALIZACIÓN Y ZONA HORARIA
# ==============================================================================
LANGUAGE_CODE = 'es-cl'

TIME_ZONE = 'America/Santiago'

USE_I18N = True

USE_TZ = True


# ==============================================================================
# ARCHIVOS ESTÁTICOS (CSS, JavaScript, Imágenes)
# ==============================================================================
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
] if (BASE_DIR / 'static').exists() else []


# ==============================================================================
# CONFIGURACIÓN DE DJANGO REST FRAMEWORK (DRF)
# ==============================================================================
REST_FRAMEWORK = {
    # Renderizadores por defecto: JSON para consumo de frontend/APIs y Browsable API para pruebas en navegador
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    # Formato de fecha y hora estandarizado ISO 8601
    'DATETIME_FORMAT': '%Y-%m-%dT%H:%M:%SZ',
}

# Clave primaria por defecto para modelos
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
