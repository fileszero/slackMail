## Postfix
### /etc/postfix/main.cf

```
alias_maps = hash:/etc/aliases, regexp:/etc/aliases.regex
```

### /etc/aliases
```
slack: "|(cd /path/to/script/slackMail; LC_CTYPE='C.UTF-8' /usr/local/bin/python3.8 dispatch.py)"
```
### /etc/aliases.regex
```
/^slack\+(.*)(@example.com)?$/ "|(cd /path/to/script/slackMail; LC_CTYPE='C.UTF-8' /usr/local/bin/python3.8 dispatch.py)"
```
### update alias
$> newaliases

## Slack post
### install nkf
sudo apt install nkf

wget -q -O - https://www8.cao.go.jp/chosei/shukujitsu/syukujitsu.csv | nkf | grep -e "^20[12]" > /home/<username>/var/holidays.csv