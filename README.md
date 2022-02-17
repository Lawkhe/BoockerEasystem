# BoockerEasystem
Current and future market trends force entities to be increasingly competitive. Every entity that wishes to compete in the current market must consider the information and accessibility of it; as one of the most important assets. For this reason, it is necessary for the entity to have the appropriate Information Systems to quickly and efficiently supply information with additional value in a reservation and service system within the reach of its users. In most cases, entities distribute all their information systems in various applications, with the inefficiency and repetition of data that this entails. For this reason, a suitable option may be the acquisition of a Boocker Easystem system.

## Requirements for local deployment:
- MySQL instance running on the system
- Python 3 installed (versión 3.7 > )
- Virtual environment (optional, but its use is recommended)

## Despliegue local

1. Clone the repository
2. Activate the virtual environment
3. Installing Python dependencies, run the command ```pip install -r req.txt``` which will be responsible for installing all the necessary libraries to start the project
4. Set up your local database in file settings.py (/backend/melmac/settings.py) where there is a section of the databases where you will have to make changes in the default element including the USER, PASSWORD y PORT (if the db is running on a port other than 5432).
5. run the command ```python manage.py runserver``` where you can verify that the project is running correctly and will be published in the route http://localhost:8000 default
