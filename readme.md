
## Postfix
### Pyhotn
 sudo -u postfix pip3.8 install --upgrade -r requirements.txt
### /etc/postfix/main.cf

```
alias_maps = hash:/etc/aliases, regexp:/etc/aliases.regex


allow_mail_to_commands = alias,forward,include
```

危険化も？

default_privs


### /etc/aliases
```
slack: "|(cd /path/to/script/slackMail; LC_CTYPE='C.UTF-8' /usr/local/bin/python3.8 dispatch.py)"
withdrawal: "|(cd /path/to/script/slackMail; LC_CTYPE='C.UTF-8' /usr/local/bin/python3.8 dispatch.py)"
```
https://teratail.com/questions/248753
### /etc/aliases.regex
```
/^slack\+(.*)(@example.com)?$/ "|(cd /path/to/script/slackMail; LC_CTYPE='C.UTF-8' /usr/local/bin/python3.8 dispatch.py)"
```
### update alias
> newaliases

### /etc/postfix/access

postmap /etc/postfix/access

### /etc/postfix/access.regex

sudo postmap /etc/postfix/access.regex

↑不要かも
### restart postfix
sudo systemctl restart postfix

## Slack post
### install nkf
sudo apt install nkf

wget -q -O - https://www8.cao.go.jp/chosei/shukujitsu/syukujitsu.csv | nkf | grep -e "^20[12]" > /home/<username>/var/holidays.csv

## TEST
sudo LC_CTYPE='C.UTF-8' /usr/local/bin/python3.8 linetest.py
sudo LC_CTYPE='C.UTF-8' /usr/local/bin/python3.8 slacktest.py

sudo -u postfix LC_CTYPE='C.UTF-8' /usr/local/bin/python3.8 linetest.py