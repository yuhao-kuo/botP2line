#!/usr/bin/bash
#encoding:utf-8

from linebot import LineBotApi
from linebot.models import *
import os
import sys

line_uid = None
secret = None
token = None
imgur_uid = None

def _push_image_to_imgur(imagePath, uid):
    img_cmd = "./imgur {0} {1} 2>> {2}".format(imagePath, uid, '/tmp/del.log')
    stdout = os.popen(img_cmd)
    for d in stdout.readlines():
        return d.strip()
    return None

def _load_environment():
    global line_uid
    global secret
    global token
    global imgur_uid
    fp = open("./apinfo.conf", "r")
    s = fp.readline()
    while s:
        str_list = s.split('=')
        if len(str_list) >= 2:
            if str_list[0] == "channel_secret":
                global secret
                secret = str_list[1]
            if str_list[0] == "channel_access_token":
                global token
                token = str_list[1]
            if str_list[0] == "line_user_id":
                global line_uid
                line_uid = str_list[1]
            if str_list[0] == "imgur_user_id":
                global imgur_uid
                imgur_uid = str_list[1]
        s = fp.readline()
    fp.close()
    return (line_uid, secret, token, imgur_uid)

def LINE_TransmitText(mess):
    user_id, channel_secret, channel_access_token, imgur_user_id = _load_environment()
    if user_id is None:
        print('line user is None')
        sys.exit(1)
    if channel_secret is None:
        print('channel_access_token is None')
        sys.exit(1)
    if channel_access_token is None:
        print('user_id is None')
        sys.exit(1)
    line_bot_api = LineBotApi(channel_access_token)
    print("push message")
    line_bot_api.push_message(user_id, TextSendMessage(text=mess))


def LINE_TransmitImage(img_path):
    user_id, channel_secret, channel_access_token, imgur_user_id = _load_environment()
    if user_id is None:
        print('line user is None')
        sys.exit(1)
    if channel_secret is None:
        print('channel_access_token is None')
        sys.exit(1)
    if channel_access_token is None:
        print('user_id is None')
        sys.exit(1)
    if imgur_user_id is None:
        print('imgur_id is None')
        sys.exit(1)
    imgur_url = _push_image_to_imgur(img_path, imgur_user_id)
    if imgur_url is None:
        print(imgur_url)
        print('push to imgur failure')
        sys.exit(1)
    line_bot_api = LineBotApi(channel_access_token)
    print("push image")
    line_bot_api.push_message(user_id, ImageSendMessage(original_content_url=imgur_url, preview_image_url=imgur_url))

