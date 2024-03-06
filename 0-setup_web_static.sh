#!/usr/bin/env bash
#  Bash script that sets up your web servers for the deployment of web_static

# Install Nginx if it not already installed
sudo apt-get update
sudo apt-get -y install nginx

# Create the folders if not exists
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

# Create a fake HTML
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link,If the symbolic link already exists, it should be deleted and recreated
sudo rm -rf /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration
replacement="server_name _;\n\tlocation \/hbnb_static \{ \n\talias \/data\/web_static\/current\/;\n\t\}"
sudo sed -i "s/server_name _;/$replacement/" /etc/nginx/sites-enabled/default



sudo service nginx restart
