import os

import time
import psycopg2
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        max_retries = 10
        retry_delay = 5

        db_params = {
            "host": os.getenv("POSTGRES_HOST"),
            "user": os.getenv("POSTGRES_USER"),
            "password": os.getenv("POSTGRES_PASSWORD"),
            "database": os.getenv("POSTGRES_DB"),
        }

        for _ in range(max_retries):
            try:
                conn = psycopg2.connect(**db_params)
                conn.close()
                print("Database is available")
                return
            except psycopg2.OperationalError:
                print("Database is not available. Retrying...")
                time.sleep(retry_delay)

        print("Unable to connect to the database")
