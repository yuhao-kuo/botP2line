#!/usr/bin/python
#encoding=utf-8

import pushmess
import time

pushmess.LINE_TransmitText('hello message is a test !!!')
time.sleep(2)
pushmess.LINE_TransmitImage('kaus.png')
