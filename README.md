## Daily planner
### Description 
This is the backend part of the Daily planner Application.

Web daily planner which contains some mini-applications for easy planning your day.

Project Daily planner:
* To-do List
* Calendar
* Weather
* News

### Development guide
Docker is a tool designed to make it easier to create, deploy, and run applications using containers. Containers allow
the developer to package the application with all the necessary parts, and deploy it as a single package.
Thanks to the container, the application will run on any Linux machine, regardless of any configurable parameters.

##### First start
To start the application, you first need to create an image of the application and run all the components described in
the docker-compose.yml file. Then you need to migrate the database and run the application.

### Tools
#### Containerized development tools
- [Docker](https://docs.docker.com/get-docker/)
- [docker-compose](https://docs.docker.com/compose/install/)
### Attention
> ⚠️ Migrations are not run automatically.
### Commands
### Via `docker-compose`

- ##### First docker start
```shell
$ docker-compose build
$ docker-compose up --no-start
$ docker-compose run --rm web python backend/manage.py migrate
$ docker-compose up
```

- ##### Build, migrate, make migrations, run commands
> You don't have to run migration commands, if no model changes were performed.
```shell
$ docker-compose build
$ docker-compose run web python backend/manage.py migrate
$ docker-compose run web python backend/manage.py makemigrations
$ docker-compose up
```
- ##### Create/run migration
```shell
$ docker-compose run --rm web python backend/manage.py makemigrations
or
$ docker-compose run --rm web python backend/manage.py migrate
```
For stop containers:
```shell
$ docker-compose stop
```