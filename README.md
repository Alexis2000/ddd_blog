# A minimalistic blog API in Domain Driven Design (a study project)
some existing features: 
- layered architecture
- domain model pattern
- repository pattern
- unit of work pattern
- event driven architecture

coming soon:
- dependency injection

## Building the containers

```sh
make build
make up
# or
make all # builds, brings containers up, runs tests
```

## API health check:
http://0.0.0.0:5005/healthcheck

## Makefile

There are more useful commands in the makefile, have a look and try them out.