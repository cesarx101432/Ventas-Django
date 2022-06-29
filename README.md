# Ventas-Django
Sistema de ventas para django


//iniciar variable de entorno


## 1.- Iniciar variable de entorno
```bash
# Para inciar el proyecto es necesario iniciar las variable de entorno.
py --version
py -m venv env
env\Scripts\activate.bat
#  En caso de tener porblemas de activacion en shell de Visual Studio correr:
\env\Scripts\Activate.ps1
```

## 2.- Instalacion del proyecto
```bash
# Es necesario instalar los requerimientos.
python -m pip freeze
pip freeze>requirements.txt 
pip install -r \Ventas-Django\app\requirements.txt 

```

## 3.- Correr migraciones
```bash
# Antes de iniciar el proyecto se debe correr las migraciones.
python manage.py makemigrations
python manage.py migrate
```

## 4.- Iniciar proyecto
```bash
# Se debe correr manage.py por lo cual debe estar posicionado en la raiz del archivo.
python manage.py runserver
```

## Creacion de Usuarios
```bash
# Creacion de Usuarios.
python manage.py createsuperuser
# Cambio de Password de Usuario.
python manage.py changepassword admin
# Usuario Admin del proyecto.
User:admin
Password:admin
```

## Run test.py

```bash
# Aqui se mete codigo que se necesita para procesar codigo de ayuda, no correra con el servidor.
python tests.py
```


//Instala Django
python -m pip install django 
py -m pip install Django
pip install --upgrade pip




// Iniciar proyecto Django
django-admin startproject app

// Iniciar de app
python ../manage.py startapp erp
python manage.py startapp homepage





inicia terminar django
ctrl+alt+r



MODELO VISTA TEMPLATES
M= MODELO(BASE DE DATOS)
V= VISTA (FUNCIONES)
T= TEMPLATE(PANTALLAS)

urls.py 

views.py 
incluye las vistas 

//ORM -> Mapeo de objeto relacional
puede interectura con la base de datos a manera de objetos se puede hacer insercion consultas y eliminaciones 


