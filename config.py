#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


import os

class Config(object):

    # Get a bot token from botfather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7754700986:AAHTWpyDJiU5HnYz94HgqzqKh7HOEtHC5Pw")


    # Get from my.telegram.org (or @UseTGXBot)
    APP_ID = int(os.environ.get("APP_ID", "23580732"))
    API_HASH = os.environ.get("API_HASH", "81ca3df48f25d954b2ebef5aec715a73")


    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1302460619").split())
    
