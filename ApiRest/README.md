# EV4 Backend - ApiRest

Backend API para gestión de equipos y planes de mantención.

Descripción
-----------
Proyecto Django REST Framework que expone modelos para:
- Empresas (`Company`)
- Equipos (`Equipment`)
- Técnicos (`Technician`)
- Planes de Mantención (`MaintenancePlan`)
- Ordenes de Trabajo (`WorkOrder`)

La API implementa autenticación por token y permisos por defecto que permiten
lectura pública y operaciones de escritura sólo a usuarios autenticados.

Requisitos
---------
- Python 3.11+ (el proyecto fue probado con Python 3.13)
- Django (>=5.2)
- djangorestframework
- djangorestframework-authtoken

Instalación rápida
-----------------
1. Crear y activar un entorno virtual (recomendado):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Instalar dependencias (ejemplo):

```powershell
pip install django djangorestframework djangorestframework-authtoken
```

Pasos para ejecutar la API
-------------------------
1. Aplicar migraciones:

```powershell
cd d:\\EV4_BACKEND\\ApiRest
python manage.py makemigrations
python manage.py migrate
```

2. Crear un usuario de prueba (interactivo) o mediante shell:

```powershell
python manage.py createsuperuser
# o usar el script proporcionado:
python manage.py shell -c "from django.contrib.auth import get_user_model; User=get_user_model(); User.objects.create_superuser('apitest','apitest@example.com','testpass')"
```

3. Iniciar servidor de desarrollo:

```powershell
python manage.py runserver
```

Autenticación
-------------
- La API expone un endpoint para obtener token: `POST /api-token-auth/` (envía `{"username":"...","password":"..."}` y devuelve `{"token":"..."}`).
- El header de autorización debe enviarse como: `Authorization: Token <token>`

Reglas de acceso
----------------
- Usuarios no autenticados: solo lectura (`GET`).
- Usuarios autenticados: pueden crear, modificar y eliminar (`POST`, `PUT`, `PATCH`, `DELETE`).

Ejemplos de endpoints
---------------------
- `GET /api/ping/` — endpoint de prueba que devuelve `{ "status": "ok", "message": "API is working" }`.
- `GET /api/companies/` — lista de empresas.
- `POST /api/companies/` — crear empresa (requiere autenticación). Ejemplo de body JSON:

```json
{ "name": "Acme", "address": "Street 1", "rut": "RUT-001" }
```

Notas adicionales
-----------------
- La API incluye la vista navegable de DRF disponible en `/api/`.
- Los modelos están registrados en el admin de Django (`/admin/`).
- Para producción revisar ajustes de `DEBUG`, `ALLOWED_HOSTS` y backend de base de datos.

Contacto
--------
Repositorio mantenido por el autor del proyecto.
