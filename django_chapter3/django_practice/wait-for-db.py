import os
import MySQLdb
from time import sleep
from pathlib import Path

os.chdir(Path(__file__).parent)

LIMIT = 120
DURATION = 3

def check_connection():
    conncetion = MySQLdb.connect(
        user=os.environ['MYSQL_USER'],
        passwd=os.environ['MYSQL_PASSWORD'],
        host=os.environ['MYSQL_HOST'],
        port=int(os.environ['MYSQL_PORT']),
        db=os.environ['MYSQL_DBNAME'],
    )
    return conncetion

if __name__ == "__main__":
    count = 0
    while count < LIMIT:
        try:
            conncetion = check_connection()
            conncetion.lose()
            print('Connect!')
            break
        except MySQLdb._exceptions.OperationalError as e:
            print(f"Waiting for MySQL...{count * DURATION}")
            count += 1
            sleep(DURATION)
            continue
        except Exception as e:
            print(f"Failed to connect MySQL. Error: {str(e)}")
            break
