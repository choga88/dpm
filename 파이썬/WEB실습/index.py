#!/usr/bin/env python

# -*- coding:utf-8 -*-
import cgi
import cgitb
import webbrowser
import MySQLdb
cgitb.enable()

form = cgi.FieldStorage()

if __name__=="__main__":

        html_head = """
        <html>
                <head>
                        <title>HELLO WORLD</title>
                </head>
        """

        html_body = """
                <body>
                        <b>Hello world~~~~</b><br>
                        <b>My name is choga88</b><br>
                </body>
        </html>
        """
        html_space =""" <br> """
        print "Content-type: text/html; charset=utf-8\n\n"
        print html_head
        print html_body
        db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="cho123",  # your password
                     db="class")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
        cur = db.cursor()

# Use all the SQL you like
        cur.execute("select * from student")

# print all the first cell of all the rows
        for row in cur.fetchall():
                print row[0],"|",row[1],"|",row[2],"|",row[3],"|",row[4]
                print html_space

	db.close()