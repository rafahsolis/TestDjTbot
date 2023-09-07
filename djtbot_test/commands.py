from DjTbot.commands import Command


# Todo: Create a content creator class to remove content creation logic from commands
class TestCommand(Command):
    command = ['test']
    allowed_groups = ['*']
    help_text = 'Test command'
    usage = '/cc text'

    def run(self, update, context):
        text = ' '.join(context.args)
        user_id = self.get_chat_id(update)
        context.bot.send_message(chat_id=user_id, text=f'Text\n{text}')
        context.bot.send_message(chat_id=user_id, text=f'Update\n{update}')
