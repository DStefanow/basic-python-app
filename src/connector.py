#!/usr/bin/env python3

import os, time
from dotenv import load_dotenv
import psycopg2

# Load environment variable from .env file in root folder
load_dotenv("../.env")

PG_HOST = os.getenv('PG_HOST')
PG_DATABASE = os.getenv('PG_DATABASE')
PG_USER = os.getenv('PG_USER')
PG_PASSWORD = os.getenv('PG_PASSWORD')
PG_PORT = os.getenv('PG_PORT')

def pg_connection(pg_host:str, pg_db: str, pg_user: str, pg_pass: str, pg_port: int):
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

    return connector
   
if __name__ == "__main__":
    # Create connection to the database
    pg_connector = pg_connection(pg_host=PG_HOST, pg_db=PG_DATABASE, pg_user=PG_USER, pg_pass=PG_PASSWORD, pg_port=PG_PORT)

    # Create cursor for DB connections
    cursor = pg_connector.cursor()

    while True:
        try:
            # Get postgres version from database
            cursor.execute("SELECT VERSION()")
            result = cursor.fetchone()

            if result:
                print(result)
            else:
                print("Unable to fetch version from database")

            time.sleep(10)
        except KeyboardInterrupt:
            print("User interupt, exiting from main program")
            exit(0)
        except:
            print(f"Unable to execute query to fetch data from {PG_DATABASE}")
