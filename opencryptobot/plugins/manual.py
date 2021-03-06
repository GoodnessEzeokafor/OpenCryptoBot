import opencryptobot.emoji as emo

from telegram import ParseMode
from opencryptobot.plugin import OpenCryptoPlugin, Category


class Manual(OpenCryptoPlugin):

    def get_cmd(self):
        return "man"

    def get_cmd_alt(self):
        return ["manual"]

    @OpenCryptoPlugin.save_data
    @OpenCryptoPlugin.send_typing
    def get_action(self, bot, update, args):
        if not args:
            update.message.reply_text(
                text=f"Usage:\n{self.get_usage()}",
                parse_mode=ParseMode.MARKDOWN)
            return

        msg = None
        cmd = args[0].lower()
        cmd = cmd[1:] if cmd.startswith("/") else cmd

        for p in self.tgb.plugins:
            if p.get_cmd().lower() == cmd:
                msg = p.get_usage() if p.get_usage() else str()

        if not msg:
            update.message.reply_text(
                text=f"{emo.INFO} No details for command `{cmd}` available",
                parse_mode=ParseMode.MARKDOWN)
            return

        update.message.reply_text(
            text=msg,
            parse_mode=ParseMode.MARKDOWN,
            disable_web_page_preview=True)

    def get_usage(self):
        return f"`/{self.get_cmd()} <command>`"

    def get_description(self):
        return "Show how to use a command"

    def get_category(self):
        return Category.BOT
