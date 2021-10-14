
import sys
import re
import os
import select

import slack

import MailParser

import config
from converters import defaultConverter
from converters import missedLalacall
from converters import sbiContractNotification

def dispatch( email_file=''):
    # read mail contents
    if os.path.exists(str(email_file)):
        # DEBUG
        with open(email_file) as f:
            text = f.read()
    else:
        text = sys.stdin.read()


    conf=config.get_config()
    # print( text )
    mail=MailParser.MailParser(text)

    # print( mail.get_attr_data() )

    converter= defaultConverter.defaultConverter()
    # custom converters
    if mail.from_address=='missed_call_service@eonet.ne.jp':
        converter= missedLalacall.missedLalacall()
    if mail.from_address=='alert_master@sbisec.co.jp' and ("約定通知" in mail.subject):
        converter= sbiContractNotification.sbiContractNotification()

    msg=converter.convert(mail)

    # slack channel
    channel=conf["slack"]["default_channel"]
    match=re.match(r'^slack\+(.*)@', mail.delivered_to)
    if match:
        channel= match.group(1)

    print(msg)
    print(channel)

    slack_client = slack.WebClient(conf["slack"]["token"])

    # message params
    slack_opt_default={'channel':channel,'text':'slack hello text','as_user':False,'username':'Slack Mail','icon_emoji':':robot_face:'}
    slack_opt= {**slack_opt_default, **msg}
    print(slack_opt)

    # post message
    response = slack_client.chat_postMessage(
        channel=slack_opt.get('channel'),  #'#random'
        text=slack_opt.get('text'),
        as_user=slack_opt.get('as_user'),
        username=slack_opt.get('username'),
        icon_emoji=slack_opt.get('icon_emoji')
        )
    print(response)

input_file=""
if sys.argv[1:2]:
    input_file=sys.argv[1]

dispatch(input_file)
# dispatch(os.path.join(os.path.dirname(__file__),"sampledata","lalacall.eml"))
