####################################################################################
Proyecto: Sistema de gestión Depto de Capacitación Bomberos de Vicente López
Curso Python Coderhouse comisión 50215
Autora: María Agustina López León
Fecha: 20/03/2024
Versión: 1.0
####################################################################################

Objetivo:
El objetivo del proyecto es permitir la gestión de cursos, instructores, integrantes del cuerpo activo (que serían los alumnos) y cartelera de novedades del Departamento de Capacitación de Bomberos Vicente López a usuarios registrados y atenticados.

Los usuarios sin autenticar en el sistema pueden:
- Registrarse
- Visualizar la página "Nuestra historia"
- Visualizar la página "Contacto"

Los usuarios registrados pueden:
- Visualizar la página Inicio
- Visualizar la página de cursos
- Agregar Cursos
- Editar Cursos
- Eliminar Cursos
- Visualizar la página de Profesores
- Agregar Profesores
- Editar Profesores
- Eliminar Profesores
- Visualizar la página de Cuerpo Activo
- Agregar integrantes del Cuerpo Activo
- Editar integrantes del Cuerpo Activo
- Eliminar integrantes del Cuerpo Activo
- Visualizar la página de Cartelera de novedades
- Crear una novedad y visualizarla en la página de Cartelera
- Editar una novedad de la página de Cartelera
- Eliminar una novedad de la página de Cartelera
- Visualizar la página "Nuestra Historia"
- Visualizar la página de "Contacto"
- Visualizar la página "Sobre mi" en donde hay una breve descripción de la autora del proyecto
- Editar el perfil
- Cambiar la contraseña del perfil
- Editar el avatar del perfil
- Cerrar Sesión

####################################################################################
Pruebas Realizadas
Ver el archivo "Unit Test - Sistema de Gestión Depto de Capacitación Bomberos Vicente López" dentro de este mismo repositorio


Usuarios para Pruebas:
Usuario= admin
Password= 12345

Usuario_test= Alan
Password= Barcelona2025!

####################################################################################
Tecnología utilizada:
Front End
- HTML5
- CSS3
- Bootstrap 
- JavaScript

Back end
- Python 3.12.2
- Django 4.2.5


Modelos usados:
- Curso: Este modelo tiene los campos Id, Nombre de curso, Tipo (si es una capacitación interna o de la Federación), Mes (el mes en el que se dictó o dictará) y Año. Aquí se almacenan todos los cursos gestionados por el Departamento de Capacitación.
- Cuerpo: Hace referencia al Cuerpo Activo del Cuartel que toma los cursos, o sea los alumnos. Los campos que lo componen son Nombre, Apellido, Jerarquía, Email y legajo (que es el número de identificación no solo adentro de la institución sino también dentro del Consejo Nacional)
- Profesor: En este modelo se encuentran los intructores que dictan los cursos. Los campos que lo componen son: Nombre, Apellido, Email, Jerarquía y Cuartel
- Cartelera: En este modelo se almacenan las novedades que el Depto de Capacitación quiere transmitir al Cuerpo Activo. Los campos que lo componen son Título, Subtítulo, Autor y Novedad.

####################################################################################

Video demostración del proyecto >> https://youtu.be/u-naJRiTb74

