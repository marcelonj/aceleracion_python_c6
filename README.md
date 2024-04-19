# Blog Aceleración Django
Este proyecto surge como el proyecto final del curso *Programa de Aceleración en Python* dictado por la academia CIMNE IBER y está destinado a demostrar los conocimientos que fueron adquiridos por los alumnos en el mismo.
## Requisitos
Los requisitos solicitados fueron los siguientes:
### Obligatorios
- Debe estar desarrollado con Django. 
- Debe permitir operaciones CRUD con los artículos. 
- Debe permitir operaciones CRUD con los comentarios. 
- Debe permitir filtrar los artículos por categorías y palabras clave. 
- Debe permitir subir imágenes para los artículos. 
- Debe soportar el formato enriquecido para los artículos con TinyMCE. 
- Debe estar documentado en el archivo README.md. 
- Debe tener un archivo requirements.txt con las dependencias del proyecto. 
### Opcionales
- Debe tener un sistema de autenticación de usuarios.
- Debe tener un sistema de registro de usuarios.
## Instalación
> [!NOTE]
> Previamente se debe tener instalado Python 3.12.2 y se debe tener creada una base de datos MySQL

Para correr el proyecto de forma local hay que seguir los siguientes pasos:
1. Clonar el repositorio

```
git clone https://github.com/marcelonj/aceleracion_python_c6.git
```

2. Crear un entorno virtual

```
python -m venv venv
```

3. Activar el entorno virtual

```
./venv/Scripts/activate
```

4. Instalar las librerias del archivo [requirements.txt](requirements.txt)

```
pip install -r requirements. txt
```

5. Crear y configurar un archivo .env con las variables de entorno siguiendo el ejemplo dado en [.env.example](.env.example)

6. Correr las migraciones

```
python ./blog/manage.py migrate
```

7. Correr el servidor

```
python ./blog/manage.py runserver
```

8. Acceder a la dirección que suministro el comando anterior

## Proceso de desarrollo
### Tecnologías utilizadas
- Python
- Django
- Librerias varias de Django (detalladas en [requirements.txt](requirements.txt))
- Bootstrap

### Etapas
**Primera etapa**

En la primera etapa realicé toda la configuración necesaria para poder comenzar a desarrollar el proyecto. Entre las mismas se encontraron la creación del entorno virtual y la instalación de las librerias necesarias, detalladas en la documentación brindada por los profesores.
Además configuré los detalles más pertinentes del archivo de configuración settings.py y creé la base de datos necesaria para correr el proyecto y el usuario que permitió conectar con la misma.

**Segunda etapa**

Posteriormente desarrolle los modelos necesarios para la aplicación de blog propiamente dicha, siguiendo nuevamente los liniamientos suministrados en la documentación previamente mencionada.
También desarrolle las clases necesarias para poder acceder a la administración de los modelos desde la vista */admin*.

**Tercera etapa**

Creación de vistas