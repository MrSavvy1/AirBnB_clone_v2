#!/usr/bin/env bash
#setting up my web server for a web static deployment
sudo apt-get update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/shared/ /data/web_static/releases/test/
sudo echo "<html>
	<head>
	</head>
	<body>
		Holberton School
	</body>
<html>
	<head>
	</head>
	<body>
		Holberton School
	</body>
</html>
