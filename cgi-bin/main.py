#!/usr/bin/env python3

import cgi

HTML_ROOT = """
    <!DOCTYPE html>

    <html>
	    <head>
		    <title> Site </title>
		    <meta charset="utf-8"/>
		    <link rel="stylesheet" type="text/css" href="../styles/style.css"/>
    	</head>

	    <body>

		    <div id="main">
                {}
		    </div>

	    </body>
    </html>
"""
NAV_BAR = """
    <ul id="nav">
		<li>
			<a href="#">Заповнити табель</a>
		</li>
		<li>
			<a href="#">Дані про нарахування</a>
		</li>
		<li>
			<a>Таблиці</a>
			<ul>
				<li><a href="/cgi-bin/tables.py?table=employee">Співробітники</a></li>
				<li><a href="/cgi-bin/tables.py?table=post">Посади</a></li>
				<li><a href="/cgi-bin/tables.py?table=resume">Табелі</a></li>
			</ul>
		</li>
	</ul>
"""
GREETING_IMAGE = """
    <img src="../img/salary.png" width="900px" style="margin: 20px 5px; box-shadow: 2px 2px 10px #CCC;">
"""

form = cgi.FieldStorage()

print("Content-type: text/html\n")
print(HTML_ROOT.format(NAV_BAR + GREETING_IMAGE))



