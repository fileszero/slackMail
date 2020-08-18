# coding:utf-8
import re
import sys

import MailParser
import googlePeople

# Google people API
# https://developers.google.com/people/quickstart/python
#   Desktop app
#   Download Client Configuration


class missedLalacall:
    def convert(self,mail: MailParser.MailParser ):
        body=mail.body
        tels=re.findall(r'[-\d]{10,}',body)
        print( tels ,mail.from_address)
        people=googlePeople.GooglePeople()

        for s in tels:
            tel:str=s
            tel=tel.replace('-','')
            tel = '`' + tel[0:3] + '-' + tel[3:7] + '-' + tel[7:] + '`'
            #  find contact name
            contact = people.getContactByPhoneNumber(tel)
            if contact:
                name="/".join(map(lambda name: name.get("displayName"),contact.get("names")))
                tel += '  [' + name + ']'
            body = body.replace(s, tel)

        return body

if __name__ == "__main__":

    text = sys.stdin.read()

    mail = MailParser.MailParser(text)
    converter=missedLalacall()
    msg=converter.convert(mail)
    print(msg)
