# BoockerEasystem
Current and future market trends force entities to be increasingly competitive. Every entity that wishes to compete in the current market must consider the information and accessibility of it; as one of the most important assets. For this reason, it is necessary for the entity to have the appropriate Information Systems to quickly and efficiently supply information with additional value in a reservation and service system within the reach of its users. In most cases, entities distribute all their information systems in various applications, with the inefficiency and repetition of data that this entails. For this reason, a suitable option may be the acquisition of a Boocker Easystem system.

## Requisitos para despliegue local:
- Instancia de MySQL corriendo en el sistema
- Python 3 instalado (versión 3.7 > )
- Ambiente virtual (opcional, pero se recomienda su uso)

## Despliegue local

1. Clonar el repositorio
2. Activar el ambiente virtual
3. Instalación de dependencias Python, correr el comando ```pip install -r req.txt``` el cual se encargará de instalar todas las librerias necesarias para iniciar el proyecto
4. Configurar tu base de datos local en el archivo settings.py (/backend/melmac/settings.py) donde hay un apartado de las bases de datos donde tendras que hacer cambios en el elemento default incluyendo el usuario(USER), contraseña(PASSWORD) y puerto(PORT, si la bd esta corriendo en otro puerto que no sea el 5432).
5. Correr el comando ```python manage.py runserver``` donde se podra verificar que el proyecto esta corriendo correctamente y estara publicado en la ruta http://localhost:8000 por defecto.
