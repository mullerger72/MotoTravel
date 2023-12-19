# Coderhouse-56060-Django

## Proyecto Django

Haremos un proyecto con el framework Django para certificar el curso.

## Entornos virtuales

Un entorno virtual en Python es una herramienta 
que te permite crear un espacio aislado donde puedes instalar 
y manejar las dependencias (bibliotecas y versiones de Python) 
específicas para un proyecto en particular, sin afectar al sistema global de Python.

`pip list` muestra las bibliotecas instaladas en el entorno virtual o global

¿Cómo crear un entorno virtual? (entorno aislado del global)

`python -m venv .venv`

¿Cómo activar el entorno virtual?
`.\.venv\Scripts\activate`  (Windows Powershell)
`source .venv/bin/activate` (Linux o Mac)

## Instalación Django

`pip install django`

## Comandos

- Creo una carpeta `project`
- `cd project`
- `django-admin startproject config .`
- `python manage.py runserver`
- `python manage.py startapp cliente`
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py createsuperuser`