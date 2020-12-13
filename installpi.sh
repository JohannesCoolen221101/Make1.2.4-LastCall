sudo apt -y update
sudo apt install apache2 -y
sudo apt install mariadb-server mariadb-client -y
sudo mysql_secure_installation

sudo mysql -u root -p

CREATE USER 'user'@localhost IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON *.* TO 'user'@localhost IDENTIFIED BU 'password';
flush privileges;
exit;
sudo apt -y install wget php php-cgi php-mysqli php-pear php-mbstring php-gettext libapache2-mod-php php-common php-phpseclib php-mysql
wget https://files.phpmyadmin.net/phpMyAdmin/4.9.7/phpMyAdmin-4.9.7-all-languages.tar.gz
tar xvf phpMyAdmin-4.9.7-all-languages.tar.gz
sudo mv phpMyAdmin-*/ /usr/share/phpmyadmin
sudo mkdir -p /var/lib/phpmyadmin/tmp
sudo chown -R www-data:www-data /var/lib/phpmyadmin
sudo mkdir /etc/phpmyadmin/
sudo cp /usr/share/phpmyadmin/config.sample.inc.php  /usr/share/phpmyadmin/config.inc.php
sudo nano /usr/share/phpmyadmin/config.inc.php
