# coding:utf-8
import MailParser
import re
import sys

# Google people API
# https://developers.google.com/people/quickstart/python
#   Desktop app
#   Download Client Configuration


class missedLalacall:
    def convert(self,mail: MailParser.MailParser ):
        body=mail.body
        tels=re.findall(r'[-\d]{10,}',body)
        print( tels )

if __name__ == "__main__":

    text = sys.stdin.read()

    mail = MailParser.MailParser(text)
    lalacall=missedLalacall()
    lalacall.convert(mail)
