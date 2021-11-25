#!/bin/bash

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        echo "RUnning setup on linux-gnu"
elif [[ "$OSTYPE" == "darwin"* ]]; then
        echo "RUnning setup on MacOSX"
elif [[ "$OSTYPE" == "cygwin" ]]; then
        echo "RUnning setup on Poixor windows virtulisation"
elif [[ "$OSTYPE" == "msys" ]]; then
        echo "Running setup on Lightweight shell and GNU utilities compiled for Windows (part of MinGW)"
        echo "Cant run on this platform."
        exit
elif [[ "$OSTYPE" == "win32" ]]; then
        echo "RUnning setup on win32"
elif [[ "$OSTYPE" == "freebsd"* ]]; then
        echo "RUnning setup on FreeBSD"
else
        echo "RUnning setup on Unknown"
fi


if [ "$EUID" -ne 0 ]
  then echo "Please run as root."
  exit
fi

rootPass = "Pass"

mysql_package=mysql-server-8.0

echo "Starting setup."
apt install php-common libapache2-mod-php php-cli
echo "Done."
echo "Setting up MySQL Server 8.0"
apt-get update

# Setup mysql root password
debconf-set-selections <<< "mysql-server mysql-server/root_password password $rootPass"
debconf-set-selections <<< "mysql-server mysql-server/root_password_again password $rootPass"

# Install MySQL Server
apt-get install -y --force-yes $mysql_package

echo "Installed."

echo "Setting up mysql for external connections."
sed -i "s/bind-address.*/bind-address = 0.0.0.0/" /etc/mysql/mysql.conf.d/mysqld.cnf
echo "Done."

MYSQL=`which mysql`

echo "Granting perms to root acc."
Q1="GRANT ALL ON *.* TO 'root'@'%' IDENTIFIED BY '$1' WITH GRANT OPTION;"
Q2="FLUSH PRIVILEGES;"
SQL="${Q1}${Q2}"

$MYSQL -uroot -p$1 -e "$SQL"
echo "Done."

echo "Restarting mysql service."
service mysql restart
echo "Done."

echo "Setting up sql tables."
SQL = (cat "./src/setup_users.sql")
$MYSQL -uroot -p$1 -e "$SQL"
echo "Done."


echo "Finished Setup server running and binded on all local/public ips."

service mysql status