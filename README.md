# Log Analysis

### Project Overview:
In this project, the main operations to be done is to fetch results from a real-time database that gives information about a data. You have to connect to the database and get the information from the server and form into a report.

## Process to be followed:

 ### Softwares needed:
1. Python
2. Vagrant
3. VirtualBox
4. psycopg2

### Setting up the Project:

1. Firstly, install Vagrant and VirtualBox.
2. Now you have to add a box in the vagrant which is used to run the project in your repository.
3. You also need to download the data from below link:

	https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

4. Now extract this file and place it in your repository.

### Starting the Virtual Machine:

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
    
After performing the above operations, you need to perform some SQL queries on the data provided.
The following queries will give the actual results which are fetched from the database:

1. Create a view to fetch result of 3 most popular articles of all time:
   
   create view view_1 as select articles.title,count(*) as views from articles inner join log on log.path 
   like concat('%',articles.slug,'%') and log.status like '%200%' group by articles.title order by views desc limit 3;

2. Create a view to fetch result of most popular article authors of all time:
   
   create view view_2 as select authors.name,count(log.path) as views from log,authors inner join articles on
   articles.author=authors.id where log.path like concat('/art%',articles.slug) group by authors.name 
   order by views desc;
   
3. Create a view to fetch result of Days with more than 1% of request that lead to an error:
   
   create view view_3 as select * from ( select err1.day, round((cast(100*err2.total as numeric)/ cast(err1.total
   as numeric)), 3) as per_err from (select date(time) as day, count(*) as total from log group by day) as err1
   inner join (select date(time) as day, count(*) as total from log where status != '200 OK' group by day ) as err2
   on err1.day = err2.day) as final_err order by per_err desc;
	
 Now you get result of days with "per_err" more than 1%
	
### Run the Program :

Finally, after successful completion of the above process you need check everything in the right place and run the program by using the command:

$ python fresh_news.py
