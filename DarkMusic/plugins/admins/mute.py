#
# Copyright (C) 2022 by TEAM-DARK-MUSIC@Github, < https://github.com/TEAM-DARK-MUSIC >.
#
# This file is part of < https://github.com/TEAM-DARK-MUSIC/DarkMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TEAM-DARK-MUSIC/DarkMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from DarkMusic import app
from DarkMusic.core.call import Dark
from DarkMusic.utils.database import is_muted, mute_on
from DarkMusic.utils.decorators import AdminRightsCheck

# Commands
MUTE_COMMAND = get_command("MUTE_COMMAND")


@app.on_message(
    filters.command(MUTE_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def mute_admin(cli, message: Message, _, chat_id):
    if not len(message.command) == 1 or message.reply_to_message:
        return await message.reply_text(_["general_2"])
    if await is_muted(chat_id):
        return await message.reply_text(_["admin_5"])
    await mute_on(chat_id)
    await Dark.mute_stream(chat_id)
    await message.reply_text(
        _["admin_6"].format(message.from_user.mention)
    )
