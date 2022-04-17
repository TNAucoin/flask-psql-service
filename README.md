# Docker Config
BUILD: 
```commandline
docker-compose -f docker/docker-compose.yml build
```

RUN:

```commandline
docker-compose -f docker/docker-compose.yml up
```

Migrations:

_Once the containers are running you have to start a remote process in the flask service to run db migrations_

Start remote container shell:
```commandline
docker exec -it <container-id> sh
```
Run Flask migrations:
```commandline
poetry run flask db init
poetry run flask db migrate
poetry run flask db upgrade
```

> Service on: 127.0.0.1:8888/