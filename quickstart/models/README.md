## Models

Models in Django contain the essential fields and behaviours of the data being stored.
These perform CRUD operations on the resources stored in the SQLite database in Django. 
When needing to update a model's properties, name, or anything that would affect the SQLite database,
run the following commands in the terminal to 'migrate' these changes into the SQLite database. 
These commands are also useful when creating a new model.

`python manage.py makemigrations`

and then:

`python manage.py migrate`

To keep the files related to models concise, each model will be organized into its respective porespy module file.
For example, all porespy.generators models will be found inside the ./generators.py. 
This design pattern was chosen as this allows future developers to continue working with an organized file structure,
and that all the files are separated into their own files as opposed to having 1 large file.
