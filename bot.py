import asyncio
from os import environ
from pyrogram import Client, filters, idle

API_ID = int(environ.get("API_ID","3369707"))
API_HASH = environ.get("API_HASH","aec1fd7abdfec322c426961a570ef336")
BOT_TOKEN = environ.get("BOT_TOKEN","5756617712:AAHh1iFVSwcreDWS3rUTsg4bVANfr9wLD78")
SESSION = environ.get("SESSION","BQCAQ1pZ6E9Xs7asjCGTJrv9agzwJVv4OPT_GwD_0oJ0OyjdmoFZAF0NeODOEJYmFkvL0Vuvhgnf60h6Z_Rmynmf6qS_8fX6aK77UY28IBtYDzzG4vnZlldbSVrQ4UWNR1wtFOjPsvmsb41wlGD16luZh_HlFhqRe4B_ckBJTeXUEGdopg7DpLMrJRJ1pQQPCWENittvs_xL38ybS0oZV6ZFcvoMu_1tZ0U44NMdKhKA-SIAYJIiOG7rMaT0TJJv8OxP-itYhLZDeKnnNZCBudYkUK-dY0czVhAODs2K9CPzaCGhJJ7wmA_ntWgdqvVqbzRUCFq25LkVBQlYA02AABWJQnZcZwA")
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
