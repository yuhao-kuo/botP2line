#!/bin/bash

if [ ! -d ~/bin 2> /dev/null 2> /dev/null ]; then
	mkdir ~/bin
	echo 'export PATH="$PATH:~/bin"' >> ~/.profile
fi

# imgur tools
if [ ! -f "~/bin/imgur" 2> /dev/null ] && [ -f ./imgur.sh 2> /dev/null ]; then
	mv imgur.sh ~/bin/imgur
fi

# auto load user info
cat apinfo.conf >> ~/.profile

# install python package
pip3 install line-bot-sdk

