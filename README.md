# Overview
Purpose of this document is to go over Django Hendrix project

## Prerequisites

- Activate Virtual Enviornment
```sh 
source /path/env
```
- Install Django requirements
```sh
pip install -r requirements.txt
```

## Installation 
Install postgresql

** for Ubuntu 20.04 **
- Install Postgresql 
```sh
sudo apt-get -y install postgresql postgresql-contrib
```
- Set to version 12
```sh
sudo apt-get -y install postgresql-12
```
- Start Postgresql
```sh
sudo service postgresql start
```
- Check the status
```sh
sudo service postgresql status
```


### Seed Database

NOTE: Make sure database is created and migrations are ran already!

To run migration, use:

```sh
  python manage.py makemigrations && python manage.py migrate
```

Seed Command:

```sh
 python manage.py loaddata seed/0001_Liberty.json
```

This will seed all of your data into the database specified in your environment file

### Additional Info

[Database Diagram](https://dbdiagram.io/d/6250b13a2514c97903fb39de)



### Common Errors


#### Postgresql isn't running

```sh
django.db.utils.OperationalError: connection to server at "127.0.0.1", port 5432 failed: Connection refused
        Is the server running on that host and accepting TCP/IP connections?
```

Solution

```sh
sudo service postgresql start
```
