
import sys
import re

import slack

import MailParser

import config
import defaultConverter
import missedLalacall

text = sys.stdin.read()

conf=config.get_config()
# print( text )
mail=MailParser.MailParser(text)

# print( mail.get_attr_data() )

converter= defaultConverter.defaultConverter()
if mail.from_address=='missed_call_service@eonet.ne.jp':
    converter= missedLalacall.missedLalacall()

msg=converter.convert(mail)

# slack channel
channel=conf["slack"]["default_channel"]
match=re.match(r'^slack\+(.*)@', mail.delivered_to)
if match:
    channel="#" + match.group(1)

print(msg)
print(channel)

slack_client = slack.WebClient(conf["slack"]["token"])

response = slack_client.chat_postMessage(
    channel=channel,  #'#random'
    text=msg)
print(response)