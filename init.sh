##!/bin/bash

apt update
apt install nano
apt install -y tmux
clear 
ls

apt install -y cmake

apt install -y wget

apt install -y python

apt install -y python3-pip

pip install --upgrade pip
pip install cython
pip install numpy scipy
pip install scikit-learn
pip install pandas
pip install jupyterlab
pip install seaborn
pip install pmdarima

apt-get install -y gnupg curl
curl -fsSL https://pgp.mongodb.com/server-7.0.asc | \
   gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg \
   --dearmor

echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-7.0.list


apt-get update


apt-get install -y mongodb-org

#2
#106

apt install systemctl
systemctl start mongod

systemctl status mongod
pip install pymongo

apt install unzip
clear 

pip install pytelegrambotapi

cd createDB/
python3 initDB.py

cd ..