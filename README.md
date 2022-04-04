# Connecting your Flask app with heroku postgres database

Follow this instruction to connect with Heroku Postgres.

### 1. Create virtual env for you project
```{bash}
python -m venv env
```

### 2. Install following packages
Note: psycopg2-binary for mac os users, psycopg2 for windows
```{bash}
pip install alembic==1.7.7
pip install Flask==2.1.0
pip install Flask-Migrate==2.6.0
pip install Flask-SQLAlchemy==2.5.1
pip install gunicorn==20.1.0
pip install psycopg2-binary==2.9.3
```
### 3. Create your project structure
```
.
├── app
│   ├── main.py
│   └── templates
│       └── your html files
├── Procfile
├── requirements.txt
└── wsgi.py
```

### 4. Database configuration params
In you main app file add db configuration that points to sqlite db
(just for the development process)
```{python}
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
```
### 5. Initialise database
Having Flask-Migrate installed and configured similar as in main.py you can create a migration repository with the following command
```{bash}
flask db init
```
This will add a migrations folder to your application. The contents of this folder need to be added to version control along with your other source files.
You can then generate an initial migration:
```{bash}
flask db migrate -m "Initial migration."
flask db upgrade
```
For more details on how Flask-Migrate extension works, check the [documentation](https://flask-migrate.readthedocs.io/en/latest/)
### 6. Install Heroku CLI
For mac users use the command below
```{bash}
brew tap heroku/brew && brew install heroku
```
For  more specific installation guidelines refer to [heroku](https://devcenter.heroku.com/articles/heroku-cli#install-the-heroku-cli)

### 7. Create a named app and postgres database
First you need to login to heroku, then create a named app and add postgresql database to your app
```{bash}
heroku login
heroku apps:create example-name
heroku addons:add heroku-postgresql:example-name
```

### 8. Connect your app with heroku postgres
You can access your database using environment variables.<br>
NEVER push you sensitive information like full direct link to your db to your repository.<br>
Get your database URL using environment variables<br>
To use flask_sqlalchemy to connect with your db you need to replace postgres with postgresql
```{python}
import os

DATABASE_URL = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL.replace("postgres", "postgresql")
```
DATABASE_URL is already existing in your heroku app, however you need to set up this variable on your local machine if you want to be able to run your code locally.
You can find DATABASE_URL in heroku postgres settings -> database credentials
```{bash}
export DATABASE_URL="postgres://user_name:password@host:Port/Database"
```

If you need to declare environment variables for your project purpose you can do it using the following command
```{bash}
heroku config:set YOUR_VARIABLE=value
```
### 9. Procfile
Heroku apps include a Procfile that specifies the commands that are executed by the app on startup.
Procfile format is process type: command
A Heroku app’s web process type is special: it’s the only process type that can receive external HTTP traffic from Heroku’s routers.
In this example the only process required to be defined is a web process.
```
web: gunicorn wsgi:app
```

### 10. Deploy!!!
Now you are ready to deploy your app to heroku.
First push all your changes to git
```
git add .
git commit -m "commiting my app"
git push origin your_branch
```
Now deploy your app
```
heroku git:remote -a example-name
git push heroku your_branch
```

To get last 200 lines from logs (in case sth breaks during deployment)
```
heroku logs -n 200
```