# Vejovis Analyics REST API

# API Features
**-Login/Register Patient**

**-Record Patient Data**

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/Vejovis-Analytics/project2-diabetesapplication-api.git
$ cd project2-diabetesapplication-api
```
**Create a virtual environment to install dependencies in and activate it:**

```
python -m venv ~/env
```

**Activate virtual environment**

```
source ~/env/bin/activate
```


**Install dependencies from requirements.txt**

*Note: Virtual environment must be activated
the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `python -m venv ~/env`.
*

```
pip install -r requirements.txt
```


Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

You will have access to:
`/auth`
`/api`
`/admin`


## Additional Resources 

## Git

Use the below Git commands in the Windows Command Prompt or macOS Terminal.

**Configure default email and name**

*Note: This only needs to be done the first time you use Git on your machine*

```
git config --global user.email "your@email.com"
git config --global user.name "Your Name"
```

**Initialise a new Git repository**

```
git init
```

**Commit changes to Git**

```
git add .
git commit -am "Commit message"
```

**Set Git remote**

*Note: This only needs to be done once, the details are provided by GitHub after creating a new project*

```
git remote add origin <URL TO PROJECT>
git push -u origin master
```

**Push changes to GitHub**

```
git push origin
```

## Virtual Environments

**De-activate virtual environment**

```
deactivate
```

## Django Management Commands

**Create new Django project**

```
django-admin.py startproject profiles_project  .
```

**Create new Django app**

```
python manage.py startapp profiles_api
```

**Start Django development server**

```
python manage.py runserver 0.0.0.0:8000
```

**Create database migrations file**

```
python manage.py makemigrations
```

**Run migrations**

```
python manage.py migrate
```

**Create new superuser**

```
python manage.py createsuperuser
```

## Terminal / GitBash Commands

Change directory

```
cd /directory_name
```

Change to parent directory

```
cd ..
```