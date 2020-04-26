# pi.sysnomid.com

These are the website files for my Raspberry Pi Temp Logger.
This project takes the temperature from my Raspi via python3 and the gpiozero module, inserts the data via the psycopg2 module with a free PostgreSql db from Heroku every 15 minutes, and then accesses the data via Flask and displays it in a table. I was contemplating on where to store the data, and I first used mysql.connector and mysql-server for that storage. MySQL worked fine, but I wanted a more modern and better updated db, sure the dataset is pretty basic, but that could change over time, and I wanted a database that had those features to use. I then decided on using PostgreSQL for that logging.

The code for the Raspberry Pi is stored in a another folder called "pi-side" in the repo.

At first I couldn't send all my files to a public git repo, because the files had database credentials and ip addreses in plain-text python strings, eventually I found some worksarounds about this, and I now have the database creds sent from a heroku-cli command, so if they change nothing will happen.


-Things I want to add
 
 Graphs and other interative diagrams
  More info and datasets to show over time
  Better integraion with Flask-SQLAlchemy
  Better integration with Docker
  
 -Possible Features
 
 -A move to Django, or Node.js?
  -Move to a NoSQL db?
  

![Sminfo.me Logo](https://i.imgur.com/QqAPb6N.png)


