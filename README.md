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

### Start

```shell
$ make up
```

## todo
  - [ ] migration

