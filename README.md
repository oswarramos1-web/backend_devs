# Eficia Backend -- API REST con Django + DRF + MySQL + Docker

Backend del sistema **Eficia**, un SaaS modular orientado a
contabilidad, provisiones, seguridad social, conceptos parametrizables y
nómina electrónica.\
Arquitectura moderna basada en **Django REST Framework, JWT, MySQL y
Docker**.\
Sin HTML/CSS --- API pura lista para conectar con cualquier frontend
(React, Vue, Next, Flutter, etc.).

## Características principales

### API REST 100% desacoplada

-   Autenticación con **JWT (access/refresh tokens)**\
-   Arquitectura de **multiempresa mediante middleware**\
-   Base modular:
    -   Empresas\
    -   Usuarios\
    -   Conceptos\
    -   Contabilidad (PUC)\
    -   Nómina (estructura inicial)\
-   Conexión a MySQL usando **variables de entorno**\
-   Configuración modular del entorno:
    -   `base.py`\
    -   `local.py`\
    -   `production.py`
-   **Swagger / Redoc** con `drf-yasg`
-   Proyecto listo para despliegue en **Hostinger, DigitalOcean, AWS o
    Render**
-   **Docker Compose** para levantar todo el stack localmente

## Tecnologías utilizadas

-   Python **3.11**
-   Django **4+**
-   Django REST Framework\
-   Django SimpleJWT\
-   MySQL **8**\
-   Docker + Docker Compose\
-   drf-yasg (Swagger)\
-   CORS Headers

## Estructura del proyecto

    eficia_backend/
    │
    ├── docker/
    ├── docs/
    ├── src/
    │   ├── manage.py
    │   ├── eficia_api/
    │   │   ├── settings/
    │   │   │   ├── base.py
    │   │   │   ├── local.py
    │   │   │   └── production.py
    │   │   ├── urls.py
    │   │   ├── asgi.py
    │   │   └── wsgi.py
    │   │
    │   └── apps/
    │       ├── core/
    │       │   └── middleware.py
    │       ├── empresas/
    │       ├── usuarios/
    │       ├── conceptos/
    │       ├── contabilidad/
    │       └── nomina/
    │
    ├── .env.example
    ├── docker-compose.yml
    ├── Dockerfile
    ├── requirements.txt
    └── README.md

## Requisitos previos

-   Docker y Docker Compose instalados\
-   Python 3.11 (solo si deseas ejecutar fuera de Docker)\
-   MySQL si trabajas manualmente (no recomendado)

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/tuusuario/eficia_backend.git
cd eficia_backend
```

### 2. Crear archivo `.env`

Basado en `.env.example`:

```bash
cp .env.example .env
```

Editar los valores según necesidad.

### 3. Levantar el proyecto con Docker

```bash
docker compose up --build
```

Para correr en segundo plano:

```bash
docker compose up -d --build
```

### 4. Crear superusuario

```bash
docker compose exec web python src/manage.py createsuperuser
```

### 5. Acceso a la API

**API Base:**\
http://localhost:8000/api/v1/

**Swagger Docs:**\
http://localhost:8000/docs/

**Login JWT:**\
POST → `/api/v1/auth/login/`

Body:

```json
{
    "username": "admin",
    "password": "123456"
}
```

## Multiempresa -- Header requerido

    X-Empresa: 901.999.888-1

## Deployment (Producción)

### Hostinger / VPS / Nube

Usar:

-   Dockerfile + `production.py`
-   Docker
-   Reverse proxy: **Nginx o Traefik**
-   Certificado SSL (**Let's Encrypt**)

Configurar en `.env`:

    DEBUG=False
    DJANGO_ALLOWED_HOSTS=tu_dominio.com

## Próximos pasos (Roadmap)

-   Implementar modelo personalizado de usuario (`AUTH_USER_MODEL`)\
-   Roles y permisos por empresa\
-   Motor de cálculo de provisiones\
-   Módulo contable + PUC completo\
-   Cálculo de nómina Q1 y Q2\
-   Nómina Electrónica (DIAN)\
-   GitHub Actions (CI/CD)\
-   Pruebas unitarias para cada módulo

## Contribuciones

Proyecto en desarrollo privado con fines educativos y comerciales.

## Licencia

Proyecto privado --- todos los derechos reservados.
