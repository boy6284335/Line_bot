# 架設伺服器
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('9g5bww1w0QOsb4n82HjQpoSiYvyLMSs3bYa0GrVkX6OwSKNG8jRhk0bPkdXsNGgMa97Lixr5Z4pr8x1pYt9n3OS2EDkqmL71wpSuQi3P35ttjAXmF4I7lp6dXEqf4MPbk8Fn7dHFu6NmlzcQ8gsIFgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('52d1cd2e77b5e3babcf14c4bd1640dfd')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    s = '你吃飯了嗎?'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=s))


if __name__ == "__main__":
    app.run()