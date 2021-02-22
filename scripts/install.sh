#! /bin/bash
sudo rm -rf /etc/$PME_BACKERY;
sudo rm -rf /opt/$PME_BACKERY;

sudo mkdir /etc/$PME_BACKERY;
sudo mkdir /opt/$PME_BACKERY;

# Chave SSH
# sudo mkdir /opt/$PME_BACKERY/.key;
# ssh-keygen -t rsa -b 4096 -N "" -C "$PME_BACKERY_EMAIL" -f ./static/$PME_BACKERY;
# sudo cp ./static/$PME_BACKERY /opt/$PME_BACKERY/.key;
# sudo chown $USER:$USER /opt/$PME_BACKERY/.key/$PME_BACKERY;

sudo cp -r ./ /opt/$PME_BACKERY;
sudo cp ./static/configs.json /etc/$PME_BACKERY/;

echo 'Run: python3 /opt/'$PME_BACKERY'/main.py'