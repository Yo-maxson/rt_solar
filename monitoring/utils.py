from django.conf import settings
from datetime import datetime
import psycopg2


def get_file():
    file_name = str(datetime.now()) + '.csv'
    query = "SELECT * FROM monitoring_vulnerability;"
    db_host = settings.DATABASES['default']['HOST']
    db_name = settings.DATABASES['default']['NAME']
    db_user = settings.DATABASES['default']['USER']
    db_pass = settings.DATABASES['default']['PASSWORD']

    with open(f'{settings.BASE_DIR}/media/{file_name}', 'w') as csv_file:
        con = psycopg2.connect(f'host={db_host} dbname={db_name} user={db_user} password={db_pass}')
        cur = con.cursor()
        cur.copy_expert(query, csv_file, size=100)
        con.close()

    return file_name


