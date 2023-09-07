from DjTbot.core.listeners import Listener
from telegram.ext import Filters


# https://docs.python-telegram-bot.org/en/v12.2.0/


class TestListener(Listener):
    allowed_groups = ['*']

    def run(self, update, context):
        print(update)
        user_id = self.get_chat_id(update)
        context.bot.send_message(chat_id=user_id, text=f'{update}')
