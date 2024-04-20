mkdir ~/mycerts
cd ~/mycerts
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout mysecret.key -out mycert.crt

mv mysecret.key /etc/ssl/private
cp mycert.crt /etc/ssl/certs


# nano /etc/apache/sites-available/default-ssl.conf

a2enmod ssl 
a2enmod headers 
a2ensite default-ssl.conf
apache2ctl configtest