# App de Recetas con Django

Proyecto evaluacion de portafolio que demuestra las principales características de Django para el desarrollo de aplicaciones web empresariales. Basado en el trabajo grupal M6_AE3_ABPRO.
<img width="1237" height="729" alt="index" src="https://github.com/user-attachments/assets/f9053edc-0a56-4097-9637-a88ce44b729e" />


---

## Descripción

Aplicación web desarrollada con Django que permite a los usuarios registrarse, iniciar sesión y crear recetas de cocina. Incluye un sistema de autenticación, formularios de contacto y un panel de administración personalizado.

---

## Características Implementadas

✅ Autenticación y autorización de usuarios  
✅ Registro e inicio de sesión  
✅ Creación de recetas por usuarios autenticados  
✅ Listado y detalle de recetas  
✅ Formulario de contacto  
✅ Panel de administración personalizado  
✅ Gestión de imágenes  
✅ Templates dinámicos con herencia  
✅ Base de datos relacional con ORM Django  

---

## Instalación

### 1. Crear entorno virtual

```bash
python -m venv myenv
```

### 2. Activar entorno virtual

**En Windows:**
```bash
myenv\Scripts\activate
```

**En macOS/Linux:**
```bash
source myenv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

O instalar manualmente:
```bash
pip install django==5.2.8 pillow==12.0.0
```

---

## Configuración Inicial

### 1. Realizar migraciones

```bash
python manage.py migrate
```

### 2. Crear superusuario (administrador)

```bash
python manage.py createsuperuser
```

Ingresa:
- Username: (tu nombre de usuario)
- Email: (tu correo)
- Password: (tu contraseña)

### 3. Cargar recetas iniciales **IMPORTANTE**

```bash
python manage.py shell
exec(open('recetas_app/scripts/cargar_recetas.py', encoding='utf-8').read())
exit()
```

**Si no ejecutas este script, la aplicación se inicia sin recetas.**

### 4. Realizar migraciones finales

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Ejecutar servidor

```bash
python manage.py runserver
```

La aplicación estará disponible en: **http://localhost:8000/**

### 6. Detener servidor

```bash
Ctrl + C
```

### 7. Desactivar entorno virtual

```bash
deactivate
```

---

## URLs Principales

| URL | Descripción |
|-----|-------------|
| http://localhost:8000/ | Página de inicio |
| http://localhost:8000/recetas/ | Listado de todas las recetas |
| http://localhost:8000/receta/<id>/ | Detalle de una receta |
| http://localhost:8000/contacto/ | Formulario de contacto |
| http://localhost:8000/registro/ | Registro de nuevos usuarios |
| http://localhost:8000/login/ | Inicio de sesión |
| http://localhost:8000/admin/ | Panel de administración |

---

## Estructura del Proyecto

```
recetas_proyecto/
├── recetas_app/
│   ├── migrations/          # Migraciones de BD
│   ├── scripts/
│   │   └── cargar_recetas.py    # Script para cargar datos iniciales
│   ├── static/
│   │   ├── css/
│   │   │   └── custom.css
│   │   └── images/
│   │       └── fondo.jpg
│   ├── templates/
│   │   ├── base.html
│   │   ├── inicio.html
│   │   ├── lista_recetas.html
│   │   ├── detalle_receta.html
│   │   ├── contacto.html
│   │   ├── confirmacion_contacto.html
│   │   ├── registro.html
│   │   ├── login.html
│   │   └── crear_receta.html
│   ├── admin.py             # Admin personalizado
│   ├── models.py            # Modelo Receta
│   ├── views.py             # Vistas
│   ├── forms.py             # Formularios
│   ├── urls.py              # Rutas
│   └── apps.py
├── recetas_proyecto/
│   ├── settings.py          # Configuración del proyecto
│   ├── urls.py              # URLs principales
│   ├── asgi.py
│   └── wsgi.py
├── media/                   # Imágenes de recetas
│   ├── carbonara.jpg
│   ├── ensalada.jpg
│   └── risotto.jpg
├── manage.py
├── requirements.txt         # Dependencias del proyecto
├── README.md                # Este archivo
├── pregunta_desarrollo.txt  # Preguntas de investigación
└── ejemplos             # Ejemplos de recetas para copiar
```

---

## Uso de la Aplicación

### 1. Registro de usuario

1. Haz clic en el botón **"Registro"** en la navbar
2. Completa el formulario con:
   - Username (nombre de usuario)
   - Email
   - Contraseña (dos veces)
3. Haz clic en **"Registrarse"**
4. Serás redirigido a la página de inicio como usuario autenticado

### 2. Iniciar sesión

1. Haz clic en **"Login"**
2. Ingresa tu username y contraseña
3. Haz clic en **"Ingresar"**

### 3. Crear una receta

1. Inicia sesión
2. Haz clic en **"+ Nueva Receta"** en la navbar
3. Completa o copia y pega desde recetas.txt
   - Nombre de la receta
   - Ingredientes (uno por línea o con saltos)
   - Instrucciones (paso a paso)
   - Imagen (opcional)
4. Haz clic en **"Guardar Receta"**

### 4. Contactar

1. Haz clic en **"Contacto"**
2. Completa el formulario
3. Envía tu mensaje
4. Recibirás confirmación

### 5. Panel de Administración

1. Ve a http://localhost:8000/admin/
2. Inicia sesión con el superusuario
3. Gestiona:
   - Usuarios
   - Recetas
   - Otros elementos

---

## Agregar Más Recetas

### Opción 1: A través del Admin Panel

1. Inicia sesión en http://localhost:8000/admin/
2. Ve a **Recetas**
3. Haz clic en **"Agregar Receta"**
4. Completa los campos
5. Haz clic en **"Guardar"**

### Opción 2: A través de la Aplicación

1. Inicia sesión en la aplicación
2. Haz clic en **"+ Nueva Receta"**
3. Completa el formulario
4. Guarda

---

## Dependencias

```
Django==5.2.8          # Framework web
Pillow==12.0.0         # Procesamiento de imágenes
asgiref==3.11.0        # ASGI
sqlparse==0.5.3        # Parser SQL
tzdata==2025.2         # Información de zonas horarias
```

Instala todas con:
```bash
pip install -r requirements.txt
```

---

## Requisitos Cumplidos (Evaluación de Portafolio)

✅ **Características de Django**  
- Investigación en `pregunta_desarrollo.txt`
- ORM, Admin, Autenticación nativa

✅ **Configuración del Proyecto**  
- Estructura profesional con settings.py
- Migraciones automáticas

✅ **Templates Dinámicos**  
- Herencia (base.html)
- Variables de contexto
- Condicionales y loops

✅ **Formularios**  
- Registro, Login, Contacto, Crear Recetas
- Validación automática

✅ **Autenticación y Autorización**  
- Sistema de usuarios completo
- Vistas protegidas con @login_required
- Solo usuarios pueden crear recetas

✅ **Admin Personalizado**  
- Filtros y búsqueda
- Asignación automática de autor
- Visualización mejorada

✅ **Documentación**  
- README.md (este archivo)
- Comentarios en código

✅ **GitHub**  
- Historial de commits
- .gitignore incluido
- Todos los archivos versionados

---

## Notas Importantes

- **Primera vez**: No olvides ejecutar `cargar_recetas.py` para que haya recetas iniciales
- **Admin**: Usa el superusuario creado con `createsuperuser`
- **Imágenes**: Deben estar en la carpeta `media/`
- **Templates**: Usan Bootstrap 5 para estilos
- **Base de datos**: SQLite (ideal para desarrollo)

---

## Solución de Problemas

### Error: "No hay recetas disponibles"
**Solución**: Ejecuta el script `cargar_recetas.py` (ver sección Configuración Inicial paso 3)

### Error: "No se encuentra la imagen"
**Solución**: Asegúrate de que las imágenes están en la carpeta `media/`

### Error: "No tienes permiso"
**Solución**: Inicia sesión o crea una cuenta

### Error: "Puerto 8000 en uso"
**Solución**: Usa otro puerto con `python manage.py runserver 8001`

---

## Recursos Adicionales

- [Documentación Django Oficial](https://docs.djangoproject.com/)
- [Tutorial Django](https://docs.djangoproject.com/en/5.2/intro/tutorial01/)
- [Django REST Framework](https://www.django-rest-framework.org/)

---

## Autor

Cecilia Ramos - 2025

## Licencia

Este proyecto es de código abierto bajo la licencia MIT.
