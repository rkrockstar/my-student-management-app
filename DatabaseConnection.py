import os
import psycopg2
import urlparse

DATABASE_URL = 'my-student-management-app:us-west1:my-student-management-app'

url = urlparse.urlparse(os.environ["DATABASE_URL"])

conn = psycopg2.connect(
        database=url.path[1:],
        user="postgres",
        password="Bunny999$",
        host="104.196.232.212",
        port="5432"
)
