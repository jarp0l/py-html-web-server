#!/bin/py
from cgi import FieldStorage
from pyfiglet import Figlet
import random

import fonts

form = FieldStorage()
_name = form.getvalue('name')

fonts = fonts.fonts_dict
# colors = ['red', 'green', 'magenta', 'cyan', '#fff000', '#00ea0f']
colors = ['#ef0000', '#ffff00', '#00ffa9', '#1855ee']

print("Content-type:text/html; charset=UTF-8\n")
print("<!DOCTYPE html>")
print("<html>")
print("<head>")
print('    <link rel="stylesheet" type="text/css" href="../style/style.css">')
print("<title>Generate text figlets</title>")
print("</head>")
print("<body>")
print('<div id="content">')

print('<h2>Enter a text below for figlet:</h2>')
print('<form action="/cgi-bin/text_figlet.py" method="post">')
print('<input type="text" name="name" placeholder="Type a text here">')
print('<input type="submit" value="Submit">')
print('</form><br><br>')

font = random.choice(list(fonts.values()))
fig = Figlet(font=font)

# text = input("Enter text: ")
print("Current font:", font, "<br>")
text = _name
print("<pre>")
print(fig.renderText(text))
# print(fig.renderText(text))
print("</pre>")

# print('<button id="demo" onclick="myFunction()">Click me to change my text color.</button>')

# print('<button id="reset" onclick="resetMyFunction()">Reset</button>')

# print('<script>')
# print('function myFunction() {')
# print(f' document.getElementById("demo").style.color = "{random.choice(colors)}";')
# print('}')
# # print('</script>')

# # print('<script>')
# print('function resetMyFunction() {')
# print(' document.getElementById("demo").style.color = "";')
# print('}')
# print('</script>')

# print('<script>')
# print('function confirmation(){')
# print('alert("Please wait...;")')
# print('}')
# print('</script>')

print('<p><a href="/">Home</a></p>')
print('</div>')
print('</body>')
print('</html>')