# Identity

A micro-service to manage users and authentication

## Run locally

### Setup .env variables

```shell
$ cp .env.dist .env
```

Edit accordingly to change the SECRET value. DATABASE_URL should work out the box.

### Setup database

Create postgresql data directory: `mkdir .docker-cache/datadir`

Database is automatically created the first time postgres starts with `db-initialize.sql`

Note: need to build the container to run the database migration.

### Build container

```shell
$ make docker_build
```

### Migrate database schema

```shell
$ make aerich_upgrade
```

### Start

```shell
$ make up
```

## todo
  - [ ] logger

