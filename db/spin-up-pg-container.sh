#!/usr/bin/env bash

# Load secrets from .env file
set -o allexport
source ../.env
set +o allexport

set -x # Print commands with verbosity info

# Required arguments
PG_VERSION=13.15

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
	-p "${PG_PORT}":"${PG_PORT}" \
	-e POSTGRES_PASSWORD="${PG_PASSWORD}" \
	-e POSTGRES_USER="${PG_USER}" \
	-h "${PG_HOST}" \
	-v "${PWD}"/.pg-data:/var/lib/postgresql/data \
	postgres:"${PG_VERSION}"

# Test if we have connectivity to local postgresql
nc -z -v "${PG_HOST}" "${PG_PORT}" || ( echo "Unable to connect to database check above commands and exit codes" && exit 2 )

set +x

exit 0
