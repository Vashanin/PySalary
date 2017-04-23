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
			<a href="#">Главная</a>
		</li>
		<li>
			<a href="#">О нас</a>
			<ul>
				<li><a href="#">Продукты</a></li>
				<li><a href="#">Команда</a></li>
			</ul>
		</li>
		<li>
			<a href="#">Услуги</a>
			<ul>
				<li><a href="#">Услуга один</a></li>
				<li><a href="#">Услуга два</a></li>
				<li><a href="#">Услуга три</a></li>
				<li><a href="#">Услуга четыре</a></li>
			</ul>
		</li>
		<li>
			<a href="#"></a>
			<ul>
				<li><a href="#">Маленький продукт (первый)</a></li>
				<li><a href="#">Маленький продукт (второй)</a></li>
				<li><a href="#">Маленький продукт (третий)</a></li>
				<li><a href="#">Маленький продукт (четвертый)</a></li>
				<li><a href="#">Большой продукт (пятый)</a></li>
				<li><a href="#">Большой продукт (шестой)</a></li>
				<li><a href="#">Большой продукт (седьмой)</a></li>
		    	<li><a href="#">Большой продукт (восьмой)</a></li>
				<li><a href="#">Невообразимый продукт (девятый)</a></li>
				<li><a href="#">Невообразимый продукт (десятый)</a></li>
				<li><a href="#">Невообразимый продукт (одиннадцатый)</a></li>
		    </ul>
		</li>
		<li>
			<a href="#">Контакт</a>
			<ul>
				<li><a href="#">Часы работы</a></li>
				<li><a href="#">Местоположение</a></li>
			</ul>
	    </li>
	</ul>
"""
