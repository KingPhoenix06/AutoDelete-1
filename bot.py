import asyncio
from os import environ
from pyrogram import Client, filters, idle

API_ID = int(environ.get("API_ID","3369707"))
API_HASH = environ.get("API_HASH","aec1fd7abdfec322c426961a570ef336")
BOT_TOKEN = environ.get("BOT_TOKEN","5756617712:AAFoOcwTm8SmBkNQEBk79CqXROTMwQGv8II")
SESSION = environ.get("SESSION","BQByDjHneo7z7A3PGQzlnBqJT8Flfh_CAjPvpHaCrZAZld_Kb1C6abM3K65Nsy0w19Ax9DhfkpOmRxSS0R0lEZGaoWIcdCYwnUBIUxhGNo_v-FdZarQjuNsR9K1rQmzXSn9hoNDJG9Sp7ILZW6Nn3ncUvU3c5KK41uPGuENKDGzoHZ5y7lPV0QE7VtWYWt9nW5sfopv2m9dICSX2ikzWPRFGJqO35LdHnzeqSNAJd8UxqEtDS5KnjKEhoab-ugKZV1A-KLC115WVLAY6lF_8KUFPzaqIIG-b_-tu7zvNhbEdYEe58lScCgk34UMOhUP8yrEgrcH7ZJPUbpiPfh6YZJzRQnZcZwA")
TIME = int(environ.get("TIME","300"))
GROUPS = []
for grp in environ.get("GROUPS",'-1001805750891').split():
    GROUPS.append(int(grp))
ADMINS = []
for usr in environ.get("ADMINS",'1115053159').split():
    ADMINS.append(int(usr))

START_MSG = "<b>Hai {},\nI'm a simple bot to delete group messages after a specific time</b>"


User = Client(name="user-account",
              session_string=SESSION,
              api_id=API_ID,
              api_hash=API_HASH,
              workers=300
              )


Bot = Client(name="auto-delete",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=300
             )


@Bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(START_MSG.format(message.from_user.mention))

@User.on_message(filters.chat(GROUPS))
async def delete(user, message):
    try:
       if message.from_user.id in ADMINS:
          return
       else:
          await asyncio.sleep(TIME)
          await Bot.delete_messages(message.chat.id, message.id)
    except Exception as e:
       print(e)
       
User.start()
print("User Started!")
Bot.start()
print("Bot Started!")

idle()

User.stop()
print("User Stopped!")
Bot.stop()
print("Bot Stopped!")
