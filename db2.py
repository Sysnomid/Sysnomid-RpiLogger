from app import *
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import subprocess
import os
proc = subprocess.Popen('sudo heroku config:get DATABASE_URL -a sminfo', stdout=subprocess.PIPE, shell=True)
#change the input after -a to your heroku app details
db_url = proc.stdout.read().decode('utf-8').strip() + '?sslmode=require'

conn = psycopg2.connect(db_url)

cursor = conn.cursor()

