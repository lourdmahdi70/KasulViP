from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("APP_ID",
"11888980")
APP_HASH = os.environ.get("APP_HASH", "a041669ed71104ef5a6e00234b3bd2f6")
BOT_USERNAME = os.environ.get("BOT_USERNAME", "Music_Spider_BBot")
session = os.environ.get("TERMUX", "AgBGOJB4nkUw5_ytZC4I0gUiz383LrfDo_4j-HI2-e4LJFU2OC-ajk4EtASWoAMJwmxKo805sGDlpjyOySQD8meH3YyfQyWuPPD8MegfJabGxG-wmHYt_tUHJKNBqavS8NIB1MzKa33dl8bMzkOx4ujTHqQh5bXmwsYopZM3KYQLag9neoWB-IJ-bqp-0AMMbfPy-HIX3N0zRXZrk0NrNl0IFjyQyRFh-FB8igoEFQsRXIVTyPU3jXQUMnJkTX_-_nHGtYQc49ZCctzgQDKTIbyqaeAr_C1tLJ8uz-omnAqyi-mn2cBYtIX2PFStLwhBvCpQXcF0Ou4_jithFAdWAIqmAAAAAUACQ44A")
SESSION = os.environ.get("TERMUX")
token = os.environ.get("TOKEN", "5449841253:AAEkKQL-oreIvz-TkVxUgVbANvqoBAZs20E")
fifthon = TelegramClient(StringSession(session), APP_ID, APP_HASH)
bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)
ispay = ['yes']
ispay2 = ['yes']
bot.start()
