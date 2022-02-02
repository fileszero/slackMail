from linebot import (
 LineBotApi, WebhookHandler
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import config

config = config.get_config()
ACCESS_TOKEN = config["LINE"]["token"]
SECRET = config["LINE"]["channel_secret"]

line_bot_api = LineBotApi(ACCESS_TOKEN)
sent=False
if("users" in config["LINE"]):
    users = config["LINE"]["users"]
    line_bot_api.multicast(users,TextSendMessage(text="Line Test Message to Multi users" ))
    sent=True

if("group" in config["LINE"]):
    group = config["LINE"]["group"]
    line_bot_api.push_message(group,TextSendMessage(text="Line Test Message to group" ))
    sent=True

if not sent:
    line_bot_api.broadcast(TextSendMessage(text='Hello World! broadcast'))