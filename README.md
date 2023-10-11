# Build a REST API with FastAPI, PostgreSQL and SQLAlchemy
FastAPI is a Python framework and set of tools that allow developers to invoke commonly used functions using a REST interface. 

SQLAlchemy is a package that makes it easier for Python programs to communicate with databases. Most of the time, this library is used as an Object Relational Mapper (ORM) tool, which automatically converts function calls to SQL queries and translates Python classes to tables on relational databases.

Many web, mobile, geospatial, and analytics applications use PostgreSQL as their primary data storage or data warehouse.

## How to run the REST API
Get this project from Github
``` 
git clone https://github.com/DzmitryPihulski/PosgreSQL-FastAPI
 
```



### Setting up the database

* Install PostgreSQL and create your user and database

* Create your own .env file for env variables and add there 

``` 
POSTGRES_USERNAME = {YOUR_DATABASE_USER}
POSTGRES_PASSWORD = {YOUR_DATABASE_PASSWORD}
```

### Create a virtual environment
This can be done with 
``` 
python -m venv .venv
 ```

Once you’ve created a virtual environment, you may activate it.

On Windows, run:
``` 
.venv\Scripts\activate
```

On Unix or MacOS, run: 

```
source .venv/bin/activate
```



### Install the requirements 

``` 
pip install -r requirements.txt
```

## Run the API

``` 
uvicorn main:app 
```
