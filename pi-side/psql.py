import os
import psycopg2
from gpiozero import CPUTemperature
import urllib.parse as urlparse
import subprocess

cpu = CPUTemperature()
print(cpu.temperature)
vartemp=cpu.temperature
val=str(vartemp)

proc = subprocess.Popen('heroku config:get DATABASE_URL -a sminfo', stdout=subprocess.PIPE, shell=True)
db_url = proc.stdout.read().decode('utf-8').strip() + '?sslmode=require'

conn = psycopg2.connect(db_url)



sql=("INSERT INTO pitemp(TEMP) VALUES (%s, %s);",[vartemp])
cursor = conn.cursor()

cursor.execute("INSERT INTO pitemp(TEMP) VALUES (%s);",[vartemp])


conn.commit()
