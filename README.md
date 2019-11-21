# HOUSES CATALOG
This project was generated with Python 3.7 and Django 2.2

The main app is **houses**

## How to run this app
1. Create a virtualenviroment with Python 3.7 and Django 2.2 (optional if you already have instaled in your PC this)
2. Clone the repository (if you create venv clone inside it and activate venv)
3. Install postgres and create the database (ex. housesdb) to store the data
4. Set the conection parameters in houses_catalog/houses/settings.py in the part of
`DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'NAMEDB',
        'USER': 'USERDB',
        'PASSWORD': 'PASSWORDDB',
        'HOST': 'HOSTDB'
    }
}`
5. Run the command `python manage.py migrate` to generate the tables in the database
6. Run `python manage.py runserver` and test the application, it should work correctly xD
7. If you want to send email from the application, uncomment the `#EMAIL CONFIG` part from houses_catalog/houses/settings.py and set your own emailconfigurations

by: Luis Antonio Feregrino

