#!/usr/bin/env bash

# Load secrets from .env file
set -o allexport
source ../.env
set +o allexport

set -x # Print commands with verbosity info

# Required arguments
PG_VERSION=13.15
HOST_PORT=5432
CONTAINER_PORT=5432

CONTAINER_NAME=pg-docker

# Be sure that we do not have a container with the same name currently running on the local machine
docker stop "${CONTAINER_NAME}"

# Start docker container with PostgreSQL $PG_VERSION
# Start the container as a daemon and remove it when the main process is stopped
# Map the host port to the container port
# Set postgres password
# Mount local volume for the container
docker run \
	--name "${CONTAINER_NAME}" \
	--rm -d \
	-p "${HOST_PORT}":"${CONTAINER_PORT}" \
	-e POSTGRES_PASSWORD="${PG_PASSWORD}" \
	-v "${PWD}"/.pg-data:/var/lib/postgresql/data \
	postgres:"${PG_VERSION}"

# Test if we have connectivity to local postgresql
nc -z -v 127.0.0.1 "${HOST_PORT}" || ( echo "Unable to connect to database check above commands and exit codes" && exit 2 )

set +x

exit 0
