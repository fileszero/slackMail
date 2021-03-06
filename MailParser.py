# coding:utf-8

import sys
import email
from email.header import decode_header

class MailParser:
    """
    メールファイルのパスを受け取り、それを解析するクラス
    """

    def __init__(self, mail_src: str):
        self.email_message = email.message_from_string(mail_src)
        self.subject = None
        self.to_address = None
        self.cc_address = None
        self.from_address = None
        self.x_original_to = None              #X-Original-To:
        self.delivered_to = None # Delivered-To
        self.body = ""
        # 添付ファイル関連の情報
        # {name: file_name, data: data}
        self.attach_file_list = []
        # emlの解釈
        self._parse()

    def get_attr_data(self):
        """
        メールデータの取得
        """
        files=",".join([ x["name"] for x in self.attach_file_list])
        result = f"""\
FROM: {self.from_address}
TO: {self.to_address}
CC: {self.cc_address}
X-Original-To: {self.x_original_to}
Delivered-To: {self.delivered_to}
-----------------------
BODY:
{self.body}
-----------------------
ATTACH_FILE_NAME:
{files}
"""
        return result

    def _parse(self):
        """
        メールファイルの解析
        __init__内で呼び出している
        """
        self.subject = self._get_decoded_header("Subject")
        self.to_address = self._get_decoded_header("To")
        self.cc_address = self._get_decoded_header("Cc")
        self.from_address = self._get_decoded_header("From")
        self.x_original_to = self._get_decoded_header("X-Original-To")
        self.delivered_to = self._get_decoded_header("Delivered-To")

        # メッセージ本文部分の処理
        for part in self.email_message.walk():
            # ContentTypeがmultipartの場合は実際のコンテンツはさらに
            # 中のpartにあるので読み飛ばす
            if part.get_content_maintype() == 'multipart':
                continue
            # ファイル名の取得
            attach_fname = part.get_filename()
            # ファイル名がない場合は本文のはず
            if not attach_fname:
                charset = str(part.get_content_charset())
                if part.get('Content-Type').startswith('text/plain'):
                    if charset:
                        self.body += part.get_payload(decode=True).decode(charset, errors="replace")
                    else:
                        self.body += part.get_payload(decode=True)
            else:
                # ファイル名があるならそれは添付ファイルなので
                # データを取得する
                self.attach_file_list.append({
                    "name": attach_fname,
                    "data": part.get_payload(decode=True)
                })

    def _get_decoded_header(self, key_name):
        """
        ヘッダーオブジェクトからデコード済の結果を取得する
        """
        ret = ""

        # 該当項目がないkeyは空文字を戻す
        raw_obj = self.email_message.get(key_name)
        if raw_obj is None:
            return ""
        # デコードした結果をunicodeにする
        for fragment, encoding in decode_header(raw_obj):
            if not hasattr(fragment, "decode"):
                ret += fragment
                continue
            # encodeがなければとりあえずUTF-8でデコードする
            if encoding:
                ret += fragment.decode(encoding)
            else:
                ret += fragment.decode("UTF-8")
        return ret

if __name__ == "__main__":

    text = sys.stdin.read()

    result = MailParser(text).get_attr_data()
    print(result)