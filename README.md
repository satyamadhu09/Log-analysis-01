				****** LOG ANALYSIS *****
Project Overview:
In this project, the main operations to be done is to fetch results from a real-time database that gives information about a data. You have to connect to the database and get the information from the server and form into a report.

Process to be followed:

Softwares needed:
---- Python
---- Vagrant
---- VirtualBox
---- psycopg2

Setting up the Project:

1. Firstly, install Vagrant and VirtualBox.
2. Now you have to add a box in the vagrant which is used to run the project in your repository.
3. You also need to download the data from below link:

	https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

4. Now extract this file and place it in your repository.

Starting the Virtual Machine:

1. From your repository, launch the Vagrant Virtual Machine by using the commands:

$ vagrant up

2. Now we need to log in using:

$ vagrant ssh

Set up the database:

The database includes the tables:
1. authors table  --- information about article authors
2. articles table --- information about articles
3. log table      --- information about log of each user

Now you have to do the following:

1. Load the data file in database by using command:
	
	psql -d news -f newsdata.sql

2. Upon loading,
    - \c  - connect to the database "news".
    - \dt - to check tables in database.
    - \q  - to disconnect the database.

Run the Program :

Finally, after successful completion of the above process you need check everything in the right place and run the program by using the command:

$ python fresh_news.py
