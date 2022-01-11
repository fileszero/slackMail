# -*- coding: utf-8 -*-

import slack

import config

config = config.get_config()
# https://api.slack.com/apps OAuth & Permissions
client = slack.WebClient(config["slack"]["token"])

response = client.chat_postMessage(
    channel='#random',  #'#random' private_test
    text="Hello world!")
print(response)
