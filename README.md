# Identity

A micro-service to manage users and authentication

## Run locally

### Setup database

Create postgresql data directory: `mkdir datadir`

Note: 
After first start permissions have changed and I faced the following error when building.

    error checking context: 'can't stat '/home/user/workspace/identity/datadir''.

I solved it with `sudo chmod 750 datadir`

### Start

```shell
$ make up
```

## todo
  - [ ] rate limiter
  - [ ] migration

