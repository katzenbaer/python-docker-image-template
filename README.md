# Python Docker Image Template

## Build
This project uses Docker. Run `./build.sh` to build the docker image.

## Configure
Edit the `env.list` file to provide your environment variables you want exposed to the Python app.

## Run from IntelliJ
1. Run `Create Image` Docker configuration.
2. Add a Remote Python SDK with the created Docker image and configure Project SDK.
3. Run `main` configuration.

## Run from Shell
Run the docker image with `./run.sh`. This will also bind mount the `assets` directory to the docker container.

## Installing new packages
1. Add the new package to `Pipfile`
2. Run `pipenv lock` in a shell session with a Python interpreter with the `pipenv` package installed. 
