#!/usr/bin/env python3

import os, time
from dotenv import load_dotenv
import psycopg2
from flask import Flask

app = Flask(__name__)

# Main router (act as a Flask application)
@app.route("/")
def main():
    dotenv_location = "../.env"

    # Load environment variables and exit if they are missing
    ( PG_HOST, PG_DATABASE, PG_USER, PG_PASSWORD, PG_PORT ) = load_env_vars(dotenv_location)

    # Create connection to the database
    try:
        pg_connector = pg_connection(pg_host=PG_HOST, pg_db=PG_DATABASE, pg_user=PG_USER, pg_pass=PG_PASSWORD, pg_port=PG_PORT)
    except:
        return f"Unable to create connection to {PG_HOST}:{PG_PORT} for database: {PG_DATABASE} with user: {PG_USER} and password: <hidden>"

    # Create cursor for DB connections
    cursor = pg_connector.cursor()

    try:
        # Get postgres version from database
        #cursor.execute("SELECT VERSION()")
        cursor.execute("SELECT VERSION()")
        result = cursor.fetchone()

        if result:
            return f"{result}"
        else:
            return "Unable to fetch version from database"
    except:
        return f"Unable to execute query to fetch data from {PG_DATABASE}"

def load_env_vars(dotenv_path: str) -> list:
    # Load environment variable from .env file in root folder if exists
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)

    PG_HOST = os.getenv('PG_HOST')
    PG_DATABASE = os.getenv('PG_DATABASE')
    PG_USER = os.getenv('PG_USER')
    PG_PASSWORD = os.getenv('PG_PASSWORD')
    PG_PORT = os.getenv('PG_PORT')

    return (PG_HOST, PG_DATABASE, PG_USER, PG_PASSWORD, PG_PORT)

def pg_connection(pg_host:str, pg_db: str, pg_user: str, pg_pass: str, pg_port: int) -> object:
    # Try to connect to the databse
    try:
        connector = psycopg2.connect(
            host = pg_host,
            database = pg_db,
            user = pg_user,
            password = pg_pass,
            port = pg_port
        )
    except:
        raise Exception(f"Unable to connect to {PG_HOST}:{PG_PORT} with user: {PG_USER} and password: <hidden> for database: {PG_DATABASE}")
        return None

    return connector

# Act as a script
if __name__ == "__main__":
    print(main())
