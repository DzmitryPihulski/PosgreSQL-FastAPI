# Build a REST API with FastAPI, PostgreSQL and SQLAlchemy
FastAPI is a Python framework and set of tools that allow developers to invoke commonly used functions using a REST interface. 

SQLAlchemy is a package that makes it easier for Python programs to communicate with databases. Most of the time, this library is used as an Object Relational Mapper (ORM) tool, which automatically converts function calls to SQL queries and translates Python classes to tables on relational databases.

Many web, mobile, geospatial, and analytics applications use PostgreSQL as their primary data storage or data warehouse.
## ROUTES TO IMPLEMENT
| METHOD | ROUTE | FUNCTIONALITY |                                  
| ------- | ----- | ------------- |
| *POST* | ```/adduser``` | _Register new user_| 
| *POST* | ```/additem``` |_Add new item_|
| *PUT* | ```/item/{item_id}``` | _Update an item_|
| *PUT* | ```/user/{user_id}``` | _Update a user_|
| *DELETE* | ```/item/{item_id}``` | _Delete/Remove an item_ |
| *DELETE* | ```/user/{user_id}``` | _Delete/Remove a user_ |
| *GET* | ```/items``` | _List all users_|
| *GET* | ```/users``` | _List all users_|
| *GET* | ```/item/{item_id}``` | _Get item_|
| *GET* | ```/user_items/{user_id}``` | _Get user's items_|

## Database structure

Table Users: &emsp;&emsp;&emsp; &emsp; &emsp; &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;Table Items:<br>
id : Integer, Primary key &emsp; &emsp; <------|&emsp;&ensp; id : Integer, Primary key<br> 
username : Char(25), Unique      &emsp;&emsp; &emsp; |-&emsp; user_id : Integer, ForeignKey('Users.id')<br>
email : Char(25), Unique&emsp;&emsp;&emsp;&emsp; &emsp; &emsp;&emsp;  description : VarChar()<br>
password : Char(25), Notnull    &emsp;&emsp;&emsp; &emsp;&emsp;  name : Char(255), Notnull<br>

We have items from Items table that belong to the specific users from Users table.
## How to run the REST API
Get this project from Github
``` 
git clone https://github.com/DzmitryPihulski/
 
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