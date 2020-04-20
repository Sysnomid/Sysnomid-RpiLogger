# pi.sminfo.me

These are the website files for my Raspberry Pi Temp Logger.
This project takes the temperature from my Raspi via python3 and the gpiozero module, inserts the data via the psycopg2 module with a free PostgreSql db from Heroku, and then accesses the data via Flask and displays it in a table. I was contemplating on where to store the data, and I first used mysql.connector and mysql-server for that storage. MySQL worked fine, but I wanted a more modern and better updated db, sure the dataset is pretty basic, but that could change over time, and I wanted a database that had those features to use. I then decided on using Postgre for that logging.
-Things I want to add
  Graphs and other interative diagrams
  More info and datasets to show over time
  Better integraion with Flask-SQLAlchemy
  Better integration with Docker
  
 -Possible Features
  -A move to Django?
  -Move to a NoSQL db?
  

![Sminfo.me Logo](https://i.imgur.com/QqAPb6N.png)


