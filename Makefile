docker_build:
	docker build -t samidarko/identity .
docker_push_latest:
	docker push samidarko/identity:latest
up:
	docker-compose up
