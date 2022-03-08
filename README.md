## Running postgreSQL in a container

    docker-compose up

## Accessing and manipulating database from python

    pip install requirements.txt
    python db_proxy.py


## PgAdmin web interface:

`docker-compose` also run pgAdmin in a container. To access it follow the steps below.

    http://localhost:5050
    Username: admin@test.com
    Password: admin


# Connecting to postgres server.

Create new server | Server config
:-------------------------:|:--------------------------------------------------:
![](./img/create_server.png)  |  ![](./img/pgadmin_server_config.png)
