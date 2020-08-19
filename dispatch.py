
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

slack_opt_default={'channel':channel,'text':'slack hello text','as_user':False,'username':'Slack Mail','icon_emoji':':robot_face:'}
slack_opt= {**slack_opt_default, **msg}
print(slack_opt)
response = slack_client.chat_postMessage(
    channel=slack_opt.get('channel'),  #'#random'
    text=slack_opt.get('text'),
    as_user=slack_opt.get('as_user'),
    username=slack_opt.get('username'),
    icon_emoji=slack_opt.get('icon_emoji')
    )
print(response)