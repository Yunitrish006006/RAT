#!/bin/bash
sudo nano /lib/systemd/system/rat.service
#[Unit]
#Description=rat the discord bot   
#After=network.target
#[Service]
#ExecStart=/usr/bin/python3 rat.py
#WorkingDirectory=/var/www/html/bot
#StandardOutput=inherit
#StandardError=inherit
#Restart=always
#User=root
#log can switch between append & file
#StandardOutput=append:/var/www/html/database/bot.log
#StandardError=append:/var/www/html/database/bot.log
#[Install]
#WantedBy=multi-user.target
sudo chmod 644 /lib/systemd/system/rat.service
sudo systemctl daemon-reload
sudo systemctl start rat.service
sudo systemctl stop rat.service
sudo systemctl enable rat.service
sudo systemctl status rat.service | tail -f /var/www/html/database/bot.log