aerich_upgrade:
	docker-compose run --rm web aerich upgrade
build:
	docker build -t samidarko/identity .
docker_push_latest:
	docker push samidarko/identity:latest
format:
	black app/*.py
up:
	docker-compose up