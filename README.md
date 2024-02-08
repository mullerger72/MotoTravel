# Descripcion del Proyecto.
 Bitácora:

 Bitácora es una App que permite al Usuario registrar unos pocos datos en su perfil y, a partir de allí, llevar un registro detallado de los
 viajes realizados en moto.

 Le permite al usuario registrar cada viaje realizado, in cluyendo las etapas que comprende cada viaje, detallado fecha, ciudades conectadas y km
 recorridos en cada etapa y viaje, como así también una descripción o comentario de los datos más relevantes de cada etapa realizada.

 La información registrada en la App es compartida con los todos los usuarios de la App.

# Como Descargar, instalar y Ejecutar la App "Bitácora" desde Visual Studio Code

 Iniciar Visual Studio Code
 Ir a "Terminal"/"nueva termina"

# Para descargar el proyecto que contiene la App "Bitácora"

En el caso que se requiera, ejecutar:
 `git remote add origin https://github.com/mullerger72/MotoTravel.git`

Modeverse a una carpeta vacía y ejecutar:
 `git clone https://github.com/mullerger72/MotoTravel.git`

# Para abrir el proyecto que contiene la App "Bitácora"

Abrir la Carpeta "MotoTravel"

# Para configurar VSC

Crear en el entorno virtual:
 `python -m venv .venv` (Windows)
 `python3 -m venv .venv` (Linux o Mac)

Luego activar el entorno virtual:
 `.\.venv\Scripts\activate`  (Windows Powershell)
 `source .venv/bin/activate` (Linux o Mac)

A continuación se deben instalar los requerimientos con:
 `pip install -r requirements.txt`

# Django
# Instalación Django
De ser necesario, ejecutar:
 `pip install django`

# Para ejecutar la App "Bitácora"
Debe moverse al path "project" y ejecutar:
 `python manage.py runserver`

Por último, desde un navegador, ingresar a:
http://127.0.0.1:8000/
