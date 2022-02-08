# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot start point """

from importlib import import_module
from sys import argv

from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
from userbot import BOT_VER, LOGS, bot
from userbot.modules import ALL_MODULES

INVALID_PH = (
    "\nERROR: The Phone No. entered is INVALID"
    "\n Tip: Use Country Code along with number."
    "\n or check your phone number and try again !"
)

try:
    bot.start()
except PhoneNumberInvalidError:
    print(INVALID_PH)
    exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)


LOGS.info(f"⚡Kyura - Userbot⚡ ⚙️ V{BOT_VER} [TELAH DIAKTIFKAN KONTOLL!!!]")

except Exception as e: LOGS.info(str(e)) 

try: await bot(JoinChannelRequest("@kyuraProjects")) except BaseException: pass 

try: await bot(InviteToChannelRequest(int(BOTLOG_CHATID), [BOT_USERNAME])) except BaseException: pass 

try: await bot(JoinChannelRequest("@Kyurasupport")) except BaseException: pass


if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
