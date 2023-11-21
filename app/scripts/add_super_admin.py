import argparse
import os
import bcrypt

import pymysql

conn = pymysql.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    db=os.getenv("DB_NAME")
)

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('username', type=str, help='Username of the SuperAdmin')
parser.add_argument('password', type=str, help='password of the SuperAdmin')

args = parser.parse_args()

cursor = conn.cursor()

SQL = "INSERT INTO user(username, password, is_superadmin) VALUES ('{username}', '{password}', 1)"

salt = bcrypt.gensalt()
password = bcrypt.hashpw(args.password.encode(), salt).decode('utf8')

cursor.execute(SQL.format(username=args.username, password=password))
conn.commit()
conn.close()
