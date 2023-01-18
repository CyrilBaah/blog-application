# Blog Application
This is a blog application made Python(Django), HTML, and CSS.

#  How to set up locally

1. Clone the project.
```sh
$ git clone https://github.com/CyrilBaah/blog-application.git
```
2. Change the directory
```sh
$ cd blog-application
```
3. Install required packages
4. Run
```sh
$ pip install -r requirements.txt
```
5. Start the application
```sh
$ python manage.py runserver
```

# Export SqliteDB to JSON
```sh
$ python manage.py dumpdata --indent=2 --output=blogapp.json
```

# Load the data into the new database (PostgreDB)
```sh
$ python manage.py loaddata blogapp.json
```
