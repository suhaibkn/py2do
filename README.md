# Py2Do
A Python-Flask-Vue based single-page Todo app

---

This project is written in Python3 and might not work in Python2

### Requirements
The following python modules should be installed  
  
click==7.1.1  
Flask==1.1.1  
Flask-SQLAlchemy==2.4.1  
itsdangerous==1.1.0  
Jinja2==2.11.1  
MarkupSafe==1.1.1  
SQLAlchemy==1.3.15  
Werkzeug==1.0.0  
  
These can be installed by importing the `./requirements.txt` file

### Installation
1. Create a new virtualenv
2. Activate this venv and install the required modules by `pip install -r requirements.txt`
3. Change configuration variables in `./config.py` file
4. Change the `SQLALCHEMY_DATABASE_URI` string to point to your database file
> (venv) $ `python`  
> \>\>\> from app import db, Todo  
> \>\>\> db.create_all()    
  
5. And finally `python app.py` to run the app  
6. The app will run at `http://127.0.0.1:5000/`


### Todos
1. Auto create `db.sqlite` file and migrate table


### Contributions
I created this project as a tutorial for Python-Flask-Vue integrations. Don't mind tweaking this code as required.  
All suggestions and feedback are welcomed. Feel free to send a PR if figured out any bug.  

suhaibkn
