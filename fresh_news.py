#!/usr/bin/env python

import psycopg2

query_1 = (" create view view_1 as select articles.title,count(*) as views "
           "from articles inner join log on log.path "
           "like concat('%',articles.slug,'%') and log.status like '%200%' "
           "group by articles.title order by views desc limit 3 ")
view_1 = ("select * from view_1")

query_2 = ("create view view_2 as select authors.name,count(log.path) "
           "as views from log,authors inner join articles on "
           "articles.author=authors.id where log.path like "
           "concat('/art%',articles.slug) group by authors.name "
           "order by views desc")
view_2 = ("select * from view_2")

query_3 = ("create view view_3 as select * from ( select err1.day, "
           "round((cast(100*err2.total as numeric)/ cast(err1.total "
           "as numeric)), 3) as per_err from (select date(time) as day, "
           "count(*) as total from log group by day) as err1 "
           "inner join (select date(time) as day, count(*) as total "
           "from log where status != '200 OK' group by day ) as err2 "
           "on err1.day = err2.day) as final_err order by per_err desc")
view_3 = ("select * from view_3 where per_err > 1.0")


def connection(dbname="news"):
    try:
        db = psycopg2.connect("dbname={}".format(dbname))
        cur = db.cursor()
        return db, cur
    except Exception:
        print("Can't connect to the database")


def result_set(query, view):
    db, cur = connection()
    cur.execute(query)
    cur.execute(view)
    print_result(cur.fetchall())
    db.close()


def err_result(errQuery, view):
    db, cur = connection()
    cur.execute(errQuery)
    cur.execute(view)
    print_resulterr(cur.fetchall())
    db.close()


def print_result(result):
    id = 0
    for i in result:
        id += 1
        print(str(id)+"."+str(i[0])+" - "+str(i[1])+" views")


def print_resulterr(result):
    for i in result:
        print(str(i[0])+" - "+str(i[1])+"%")


if __name__ == "__main__":
    print("\n The 3 most popular articles of all time are:\n")
    result_set(query_1, view_1)
    print("\n The most popular article authors of all time are:\n")
    result_set(query_2, view_2)
    print("\n Days with more than 1% of request that lead to an error:\n")
    err_result(query_3, view_3)
