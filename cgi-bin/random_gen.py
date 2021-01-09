#!/bin/py
import random
import datetime

print("Content-type:text/html\n")
print("<!DOCTYPE html>")
print("<html>")
print("<head>")
print('    <link rel="stylesheet" type="text/css" href="../style/style.css">')
print("<title>Random Number Generator</title>")
print("</head>")
print("<body>")
print('<div id="content">')
print("<h2>Random Number Generator</h2>")

print("Current date-time: {}".format(datetime.datetime.now().replace(microsecond=0)))

print("<br><h3>10 random numbers:</h3>")

for i in range(1, 11):
        print('<p align="center">Random #{} : {}</p>'.format(i, random.randrange(1, 100)))

print('<p><a href="/">Home</a></p>')
print('</div>')
print('</body>')
print('</html>')