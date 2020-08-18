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
        body=mail.body

        return body

if __name__ == "__main__":

    text = sys.stdin.read()

    mail = MailParser.MailParser(text)
    converter=defaultConverter()
    msg=converter.convert(mail)
    print(msg)
