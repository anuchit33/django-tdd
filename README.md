# django-tdd
----
### 1. install Docker and Docker-compose
- https://docs.docker.com/install/linux/docker-ce/ubuntu/
- https://docs.docker.com/compose/install/

### 2. Run Docker-compose
```
$ cd django-tdd
$ cp web/web/config-kel.py web/web/config.py
$ docker-compose -f "docker-compose.yml" up -d --build
```

### 3. Run robot framework 
```
$ cd django-tdd
$ virtualenv -p python3 env
$ source env/bin/activate
$ pip install -r requirements.txt
$ robot e2e/users.robot
```
