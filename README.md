# Ventas-Django
Sistema de ventas para django


//iniciar variable de entorno


## Iniciar variable de entorno

```bash
# Para inciar el proyecto es necesario iniciar las variable de entorno.
py --version
py -m venv env
env\Scripts\activate.bat
```
//* En caso de tener porblemas de activacion en shell de Visual Studio correr:
\env\Scripts\Activate.ps1


//Instala Django
python -m pip install django 
py -m pip install Django
pip install --upgrade pip

//Instalar requerimientos del proyecto
python -m pip freeze
pip freeze>requirements.txt 
// instalar requirements desde carpeta raiz (VENTAS-DJANGO)
pip install -r \Ventas-Django\app\requirements.txt 


// Iniciar proyecto Django
django-admin startproject app
cd app
python manage.py runserver


//*
python -m pip install Pillow //imagenes



// Crea migracions a base de datos
python manage.py makemigrations
python manage.py migrate

// Corre servicio
python manage.py runserver

python ../manage.py startapp erp
python manage.py createsuperuser

python manage.py startapp homepage

inicia terminar django
ctrl+alt+r

admin.py 
Se dan de alta los modelos accesibles desde al administrador de Django

MODELO VISTA TEMPLATES
M= MODELO(BASE DE DATOS)
V= VISTA (FUNCIONES)
T= TEMPLATE(PANTALLAS)

urls.py 

views.py 
incluye las vistas 

//ORM -> Mapeo de objeto relacional
puede interectura con la base de datos a manera de objetos se puede hacer insercion consultas y eliminaciones 


## Run test.py

```bash
# Aqui se mete codigo que se necesita para procesar codigo de ayuda, no correra con el servidor.
python tests.py
```

**
