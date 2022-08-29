# coding:utf-8
import re
import sys

import MailParser

# Google people API
# https://developers.google.com/people/quickstart/python
#   Desktop app
#   Download Client Configuration


class JCBDebitNoticeConverter:

    def convert(self,mail: MailParser.MailParser ):
        src=mail.body
        subject="JCB"
        if mail.subject:
            body=f"`{mail.subject}`\n"

        lines=[x.strip() for x in src.splitlines()]

        for line in lines:
            if re.search(r'【ご利用', line):
                # print(line, end="")
                body +=line+"\n"
                if re.search(r'金額', line) or re.search(r'ご利用先', line) :
                    line =  re.sub('【.*】','',line).strip()
                    subject += " " + line
        body=f"`{subject}`\n" + body

        result={'text':body,'username':mail.from_address}
        return result

if __name__ == "__main__":
    path='./sampledata/mufgdebit.eml'
    # path='./sampledata/GREEN_DOG_Fix.eml'
    # path=sys.argv[1]
    with open(path) as f:
        text=f.read()
    # text = sys.stdin.read()

    mail = MailParser.MailParser(text)
    converter=JCBDebitNoticeConverter()
    msg=converter.convert(mail)
    print(msg["text"])
