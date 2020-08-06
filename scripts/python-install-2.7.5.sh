#!/usr/bin/env bash

cd /tmp

# Install dependencies
aptitude -y install build-essential python-pip libmysqlclient-dev libadns1-dev \
 python-dev libreadline-dev libgdbm-dev zlib1g-dev libsqlite3-dev \
 libssl-dev libbz2-dev libncurses5-dev libdb-dev 

echo '--------------------------------------------------------------------------------1'
# Download latest version
wget http://python.org/ftp/python/2.7.5/Python-2.7.5.tar.xz
unxz -c Python*xz | tar xpf -

echo '--------------------------------------------------------------------------------2'
# compile
cd Python*
./configure  --prefix=/opt/python2.7.5 --enable-shared
sudo make

echo '--------------------------------------------------------------------------------3'
# install
sudo make install
echo "/opt/python2.7.5/lib" >  /etc/ld.so.conf.d/libpython2.7.conf
ldconfig

echo '--------------------------------------------------------------------------------4'
# test
/opt/python2.7.5/bin/python -c "print('Ok')" 

echo '--------------------------------------------------------------------------------5'
# Upgrade pip virtualenv
easy_install pip
pip -v install --upgrade distribute==0.7.3
pip -v install --upgrade virtualenv==1.9.1

echo '--------------------------------------------------------------------------------6'
# Create an user
adduser user_app --home /opt/user_app
su user_app
virtualenv --no-site-packages --verbose -p /opt/python2.7.5/bin/python $HOME

echo '--------------------------------------------------------------------------------7'
# test again
suso user_app
cd 
source bin/activate
python -c "import sys; print sys.version"
