import time

import psycopg2
from psycopg2.extras import RealDictCursor

from .config import settings


# Establish the database connection
while True:
    try:
        conn = psycopg2.connect(
            host=settings.database_hostname,
            port=settings.database_port,
            database=settings.database_name,
            user=settings.database_username,
            password=settings.database_password,
            cursor_factory=RealDictCursor
        )
        cursor = conn.cursor()
        break
    except Exception as error:
        print(f'Error: {error}')
        # If connection is not posible, waith 2 seconds and try it again
        time.sleep(2)
