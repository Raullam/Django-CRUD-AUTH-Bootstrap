
# Django CRUD Auth SQLite Bootstrap

## English Description
This is a base/example of a web application built with Python using Django. It features user authentication, route protection, an integrated admin panel, and CRUD operations for tasks. The project uses SQLite as its database and Bootstrap for a modern interface. It is ideal as a starting point for projects that require user and task management with security and a clean design.

## Descripción en Español
Esto es una base/ejemplo de una aplicación web desarrollada con Python usando Django. Incluye autenticación de usuarios, protección de rutas, panel de administración integrado y operaciones CRUD sobre tareas. Utiliza SQLite como base de datos y Bootstrap para el diseño visual. Es ideal como punto de partida para proyectos que requieran gestión de usuarios y tareas con seguridad y una interfaz moderna.

## Features / Características
- User registration and authentication / Registro y autenticación de usuarios
- Route protection (only logged-in users can access tasks) / Protección de rutas (solo usuarios autenticados acceden a tareas)
- Admin panel for managing users and tasks / Panel de administración para gestionar usuarios y tareas
- CRUD operations for tasks (Create, Read, Update, Delete) / Operaciones CRUD para tareas (Crear, Leer, Actualizar, Eliminar)
- SQLite database / Base de datos SQLite
- Responsive UI with Bootstrap / Interfaz responsiva con Bootstrap

## Installation / Instalación
1. Clone the repository / Clona el repositorio:
   ```bash
   git clone https://github.com/Raullam/Django-CRUD-AUTH-SQLite-Bootstrap.git
   cd Django-CRUD-AUTH-SQLite-Bootstrap
   ```
2. Create and activate a virtual environment / Crea y activa un entorno virtual:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
3. Install dependencies / Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply migrations / Aplica las migraciones:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Create a superuser (for admin panel) / Crea un superusuario (para el panel de administración):
   ```bash
   python manage.py createsuperuser
   ```
6. Run the development server / Ejecuta el servidor de desarrollo:
   ```bash
   python manage.py runserver
   ```

## Usage / Uso
- Access the app at `http://127.0.0.1:8000/` / Accede a la app en `http://127.0.0.1:8000/`
- Register a new user or log in with an existing account / Regístrate o inicia sesión
- Manage your tasks (create, edit, complete, delete) / Gestiona tus tareas (crear, editar, completar, eliminar)
- Access the admin panel at `/admin` with your superuser credentials / Accede al panel de administración en `/admin` con tu superusuario

## Technologies / Tecnologías
- Python
- Django
- SQLite
- Bootstrap

## Screenshots / Capturas de pantalla
*Falta añadir imágenes, lo podeis visitar y ver aquí*

## License / Licencia
MIT

---

### Marketing Description (MKT)

Boost your productivity and learn Django with this ready-to-use CRUD application! Secure user management, beautiful Bootstrap design, and a powerful admin panel make it perfect for personal projects, learning, or as a foundation for your next big idea. Fork it, customize it, and launch your own web app in minutes!

¡Impulsa tu productividad y aprende Django con esta aplicación CRUD lista para usar! Gestión segura de usuarios, diseño atractivo con Bootstrap y un potente panel de administración la hacen perfecta para proyectos personales, aprendizaje o como base para tu próxima gran idea. ¡Haz un fork, personalízala y lanza tu propia web en minutos!
