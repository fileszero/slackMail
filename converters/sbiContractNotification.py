# coding:utf-8
import re
import sys
import os

if __name__ == "__main__":
    sys.path.append(os.path.abspath(".."))

import MailParser


class sbiContractNotification:
    def convert(self,mail: MailParser.MailParser ):
        src=mail.body
        lines=[x.strip() for x in src.splitlines()]
        prev=""
        skip=0
        body=""
        event_time=""
        stock_info=""
        trade=""
        vol=""
        price=""

        for idx,line in enumerate(lines):
            if skip>0:
                skip-=1
                continue

            if line =="約定日時":
                event_time = lines[idx+1]
                skip=1
            elif line=="注文番号":
                skip=1
            elif line=="銘柄":
                stock_info = lines[idx+1] + "/" + lines[idx+2]
                skip=2
            elif line.startswith("株数:"):
                vol = line.replace("株数:","")
            elif line.startswith("価格:"):
                price = line.replace("価格:","")
            elif line.endswith("買") or line.endswith("売") :
                trade = line

        body=f"{trade}\n{price}円 * {vol}株\n{stock_info}\n{event_time}"

        result={'text':body,'icon_emoji':':money_with_wings:','username':'SBI Alert'}
        return result

if __name__ == "__main__":

    text = sys.stdin.read()

    mail = MailParser.MailParser(text)
    converter=sbiContractNotification()
    msg=converter.convert(mail)
    print(msg)
