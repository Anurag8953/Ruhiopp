import math
from config import SUPPORT_CHAT, OWNER_USERNAME
from pyrogram.types import InlineKeyboardButton
from DAXXMUSIC import app
from DAXXMUSIC.utils.formatters import time_to_seconds


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


def stream_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)
    if 0<badboy<=10:
        return "✄─·─·─·─·─·─·─·─·─·─"
    elif 10<badboy<=20:
        return "-ˋˏ✄─·─·─·─·─·─·─·─·─"
    elif 20<badboy<=30:
        return "-ˋˏ-ˋˏ✄─·─·─·─·─·─·─·─"
    elif 30<badboy<=40:
        return "-ˋˏ-ˋˏ-ˋˏ✄─·─·─·─·─·─·─"
    elif 40<badboy<=50:
        return "-ˋˏ-ˋˏ-ˋˏ-ˋˏ✄─·─·─·─·─·─"
    elif 50<badboy<=60:
        return "-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ✄─·─·─·─·─"
    elif 60<badboy<=70:
        return "-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ✄─·─·─·─"
    elif 70<badboy<=80:
        return "-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ✄─·─·─·─"
    elif 80<badboy<=90:
        return "-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ✄─·─·─"
    elif 90<badboy<=100:
        return "-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ✄─·"
    else:
        return "-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ-ˋˏ✄·"
    
    buttons = [
                [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="⛦", callback_data=f"add_playlist {videoid}"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
                 [
            InlineKeyboardButton(

                text="😈ᴏᴡɴᴇʀ😈",

                url=f"t.me/{OWNER_USRENAME}",

            ),
            InlineKeyboardButton(

                text="✨ ᴄʜᴀɴɴᴇʟ ✨",

                url=f"{SUPPORT_CHAT}",

            ),
                     ],
                     
        [
            InlineKeyboardButton(
                text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
                
    ]
    return buttons


def stream_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="⛦", callback_data=f"add_playlist {videoid}"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
                 [
            InlineKeyboardButton(

                text="😈ᴏᴡɴᴇʀ😈",

                url=f"t.me/{OWNER_USERNAME}",

            ),
            InlineKeyboardButton(

                text="✨ ᴄʜᴀɴɴᴇʟ ✨",

                url=f"{SUPPORT_CHAT}",

            ),
                 ],
                     
        [
            InlineKeyboardButton(
                text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"DAXXPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"DAXXPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons
