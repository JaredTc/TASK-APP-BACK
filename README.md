# 🌟 TaskWave Backend

[![Python](https://img.shields.io/badge/Python-3.8-blue?logo=python)](https://www.python.org/)  
[![Django](https://img.shields.io/badge/Django-4.2-green?logo=django)](https://www.djangoproject.com/)  
**TaskWave Backend** es una API REST desarrollada con **Django y Django REST Framework**, enfocada en la gestión de usuarios y tareas.  

Actualmente incluye:  

- Login y registro de usuarios (username o email)  
- CRUD de usuarios  
- Envío de email de bienvenida  
- CRUD de tareas  
- Autenticación con JWT  

Próximamente se añadirán más funcionalidades.  

---
## 📁 Estructura del proyecto
```bash
taskwave-backend/
 ├─ core/                  # Lógica principal: usuarios, tareas, emails
 │   ├─ users/
 │   ├─ tasks/
 │   └─ templates/emails/
 ├─ config/                # Settings, urls
 ├─ manage.py
 ├─.env
 └─ requirements.txt
```


## ⚙️ Instalación

```bash
# Clonar el repositorio
git clone https://github.com/tuusuario/taskwave-backend.git
cd taskwave-backend

# Crear y activar entorno virtual
python -m venv .venv
.venv\Scripts\activate   # Windows
source .venv/bin/activate # Linux/macOS

# Instalar dependencias
pip install -r requirements.txt

# Migraciones
python manage.py makemigrations
python manage.py migrate

# Crear superusuario (opcional)
python manage.py createsuperuser

# Ejecutar servidor
python manage.py runserver

