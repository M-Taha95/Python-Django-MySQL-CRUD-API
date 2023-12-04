# Python-Django-MySQL-CRUD-API
# install the necessary modules needed for our Django project.


First,  install the Django module.

>> pip install django

To create rest APIs we need to install Django rest framework.

>> pip install djangorestframework

By default, the Django project comes with a security that blocks requests coming from different domains. To disable this, install Django CORS headers module.

>> pip install django-cors-headers

Now create the Django project.

Open the command prompt in the desired folder and type the command.
>> __init__.py file is just an empty file that indicates that the given folder is a Python project or a Python module.

>>  asgi.py is the entry point for the asgi compatible webservers.
>> A project may have multiple apps.

For example, you can have one app which acts like a blog, or may be another app which acts like a survey form.

Currently this project does not have any app.

Lets create one app to implement our api methods.

To create an app, we need to type this command.

>> python manage.py startapp <the name of the app>



Next,  register the app and the required modules in settings.py file.

In the installed apps section, add Rest framework, cors header, and the newly created app.


We need to add the cors headers in middle ware section as well.

We will also add instructions to enable all domains to access the APIs.

This is not recommended in production. Instead, just add only those domains that need to be whitelisted.

>> wsgi.py is the entry point for the wsgi compatible web servers.

>> urls.py file contains all the url declarations needed for this project.

>> settings.py file contains all the settings or configurations needed for the project.

>> manage.py is a command line utility that helps interact with the Django project.

 

 simply run the project and see how it looks in the browser using the below command.

>> python manage.py runserver

The app is now running in the port 8000.

>> django-admin start project <name of the project>

 take a look at some of the important files in the project.
create the models needed for our app.

We need two models.

One to store department details and another one to store employee details.

The department model will have two fields. One to store an autoincremented Department ID, and another one to store a Department Name.


The employee model will have five fields.

Employee ID, Employee name, Department, Date of joining, and photo file name which stores the uploaded profile picture file name.


the MySQL database.

To connect to MySQL from our Python Django app, we need to install the database adapter.

>> pip install pymysql

Add the database details in settings.py file.

write the command to make migrations files for our models.

>> python manage.py makemigrations <app name>


After executing this, we can see a migration file that tells us what changes to the database will be made.
Once it looks fine, we can execute the command to push these changes to the database.

>> python manage.py migrate <app name>



 create serializers for our models.

Serializers basically help to convert the complex types or model instances into native Python data types that can then be easily rendered into json or xml or other content types.

They also help in deserialization which is nothing but converting the passed data back to complex types.




