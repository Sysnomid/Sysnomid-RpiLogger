from app import *
from flask_sqlalchemy import SQLAlchemy
import mysql.connector


db = mysql.connector.connect (
	host="localhost",
	user="root",
	passwd="Daft&punk4",
	database="pytemp"
)

cursor = db.cursor()

