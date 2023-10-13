# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from config import FORCE_SUB_CHANNEL, FORCE_SUB_GROUP
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if not FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="📞ʜᴇʟᴘ", callback_data="help"),
                InlineKeyboardButton(text="❌ᴄᴀɴᴄᴇʟ", callback_data="close"),
            ],
        ]
        return buttons
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="📞ʜᴇʟᴘ", callback_data="help"),
                InlineKeyboardButton(text="❌ᴄᴀɴᴄᴇʟ", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ 𝟷", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="📞ʜᴇʟᴘ", callback_data="help"),
                InlineKeyboardButton(text="❌ᴄʟᴏsᴇ", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="Help", callback_data="help"),
            ],
            [
                InlineKeyboardButton(text="✨ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 𝟷✨", url=client.invitelink),
                InlineKeyboardButton(text="✨ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 𝟸✨", url=client.invitelink2),
            ],
            [InlineKeyboardButton(text="❌ᴄʟᴏsᴇ", callback_data="close")],
        ]
        return buttons


def fsub_button(client, message):
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="✨ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 𝟸✨", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="🔄 ʀᴇsᴛᴀʀᴛ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="✨ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 𝟷✨", url=client.invitelink),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="🔄 ʀᴇsᴛᴀʀᴛ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="✨ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 𝟷✨", url=client.invitelink),
                InlineKeyboardButton(text="✨ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ 𝟸✨", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="🔄 ʀᴇsᴛᴀʀᴛ ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
