# -*- coding: utf-8 -*-

import sys

import slack

import config

config = config.get_config()
# https://api.slack.com/apps OAuth & Permissions
client = slack.WebClient(config["slack"]["token"])

ch = sys.argv[1]
mag = " ".join(sys.argv[2:])
response = client.chat_postMessage(
    channel=ch,  #'#random'
    text=mag,
    username='Slack Post',
    icon_emoji=':postbox:')
print(response)
