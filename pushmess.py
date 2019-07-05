#!/usr/bin/bash
#encoding:utf-8

from linebot import LineBotApi
from linebot.models import *
import os
import sys

def _push_image_to_imgur(imagePath):
    img_cmd = "imgur {0} 2>> {1}".format(imagePath, '/tmp/del.log')
    stdout = os.popen(img_cmd)
    for d in stdout.readlines():
        return d.strip()
    return None

def LINE_TransmitText(mess):
    user_id = os.getenv('line_user_id', None)
    if user_id is None:
        print('line user is None')
        sys.exit(1)
    channel_secret = os.getenv('channel_secret', None)
    if channel_secret is None:
        print('channel_access_token is None')
        sys.exit(1)
    channel_access_token = os.getenv('channel_access_token', None)
    if channel_access_token is None:
        print('user_id is None')
        sys.exit(1)
    line_bot_api = LineBotApi(channel_access_token)
    print("push message")
    line_bot_api.push_message(user_id, TextSendMessage(text=mess))


def LINE_TransmitImage(img_path):
    user_id = os.getenv('line_user_id', None)
    if user_id is None:
        print('line user is None')
        sys.exit(1)
    channel_secret = os.getenv('channel_secret', None)
    if channel_secret is None:
        print('channel_access_token is None')
        sys.exit(1)
    channel_access_token = os.getenv('channel_access_token', None)
    if channel_access_token is None:
        print('user_id is None')
        sys.exit(1)
    imgur_url = _push_image_to_imgur(img_path)
    if imgur_url is None:
        print('push to imgur failure')
        sys.exit(1)
    line_bot_api = LineBotApi(channel_access_token)
    print("push image")
    line_bot_api.push_message(user_id, ImageSendMessage(original_content_url=imgur_url, preview_image_url=imgur_url))

