#!/bin/bash

user=`whoami`

if [ ! -d ~$user/.bin ]; then
	mkdir .bin
	echo "$PATH:~$user/.bin" >> ~$user/.profile
fi

# imgur tools
mv imgur.sh ~/.bin/imgur

# auto load user info
cat apinfo.conf >> ~$user/.profile
source ~$user/.profile 

# install python package
pip3 install line-bot-sdk

