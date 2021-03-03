# coding:utf-8
import re
import sys

import MailParser
import googlePeople

# Google people API
# https://developers.google.com/people/quickstart/python
#   Desktop app
#   Download Client Configuration


class defaultConverter:
    def convert(self,mail: MailParser.MailParser ):
        if mail.subject:
            body=f"`{mail.subject}`\n"
        body +=mail.body
        result={'text':body,'username':mail.from_address}
        return result

if __name__ == "__main__":
    path='./sampledata/gsggsgsg.eml'
    # path='./sampledata/GREEN_DOG_Fix.eml'
    # path=sys.argv[1]
    with open(path) as f:
        text=f.read()
    # text = sys.stdin.read()

    mail = MailParser.MailParser(text)
    converter=defaultConverter()
    msg=converter.convert(mail)
    print(msg["text"])
