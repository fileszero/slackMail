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

