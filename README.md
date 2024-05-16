# Ventas-Django
Sistema de ventas para django


//iniciar variable de entorno
## 0.- Crea Servicio autoarranque 
vi /root/Ventas-Django/service.sh
vi /lib/systemd/system/venta_django.service
sudo systemctl restart venta_django.service
sudo systemctl status venta_django.service
systemctl daemon-reload
-------
[Unit]
Description=My test service
After=multi-user.target
[Service]
User=root
WorkingDirectory=/root/Ventas-Django
ExecStart=bash /root/Ventas-Django/service.sh
[Install]
WantedBy=multi-user.target
-------

## 1.- Iniciar variable de entorno
```bash
# Para inciar el proyecto es necesario iniciar las variable de entorno.

#Para Linux UBUNTU
py --version
py -m venv env
source env/bin/activate



#Para Windows
python --version
python -m venv env

#Para python 3
python3 -m venv env
env\Scripts\activate.bat


#  En caso de tener porblemas de activacion en shell de Visual Studio correr:
\env\Scripts\Activate.ps1

```

## 2.- Instalacion del proyecto
```bash
# Es necesario instalar los requerimientos.
python -m pip freeze
pip freeze>requirements.txt 
pip3 install -r app\requirements\requirements.txt 
pip3 install --only-binary Pillow Pillow
pip3 install django-widget-tweaks 
pip3 install django-crum
pip3 install django-weasyprint


https://www.pornhub.com/view_video.php?viewkey=65ca8b5e116d5

#Para WeasyPrint en ubuntu
https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#installation
apt-get install pango1.0-tools #ubuntu
pip3 install WeasyPrint 
```

## 3.- Correr migraciones
```bash
# Antes de iniciar el proyecto se debe correr las migraciones.
python app/manage.py migrate
python app/manage.py makemigrations
python app/manage.py makemigrations erp homepage login reports user
```

## 4.- Iniciar proyecto
```bash
# Se debe correr manage.py por lo cual debe estar posicionado en la raiz del archivo.
python app/manage.py runserver
python app/manage.py runserver 82.165.208.140:8000
python app/manage.py runserver 192.168.1.85:8000

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


