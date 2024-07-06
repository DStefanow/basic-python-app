### Build and run scripts before docker compose

$ docker build . -t simple-python-app:1.0
$ docker run -d --rm -p 5000:5000 \
	-e FLASK_RUN_HOST=0.0.0.0 \
	-e PG_HOST=172.17.0.3 \
	-e PG_DATABASE=postgres \
	-e PG_USER=postgres \
	-e PG_PASSWORD=<hidden> \
	-e PG_PORT=5432 \
	simple-python-app:1.0
