import math

from pyrogram.types import InlineKeyboardButton

from pyrogram.enums import ButtonStyle
from Oneforall import app
from Oneforall.utils.formatters import time_to_seconds


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            # Audio Button - SUCCESS (Green)
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
                style=ButtonStyle.SUCCESS,
            ),
            # Video Button - PRIMARY (Blue)
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
                style=ButtonStyle.PRIMARY,
            ),
        ],
        [
            # Close Button - DANGER (Red)
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
                style=ButtonStyle.DANGER,
            )
        ],
    ]
    return buttons



def stream_markup_timer(_, vidid, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)
    if 0 < umm <= 10:
        bar = "❍─────────"
    elif 10 < umm < 20:
        bar = "━❍────────"
    elif 20 <= umm < 30:
        bar = "━━❍───────"
    elif 30 <= umm < 40:
        bar = "━━━❍──────"
    elif 40 <= umm < 50:
        bar = "━━━━❍─────"
    elif 50 <= umm < 60:
        bar = "━━━━━❍────"
    elif 60 <= umm < 70:
        bar = "━━━━━━❍───"
    elif 70 <= umm < 80:
        bar = "━━━━━━━❍──"
    elif 80 <= umm < 95:
        bar = "━━━━━━━━❍─"
    else:
        bar = "━━━━━━━━━❍"
    buttons = [
                [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
                style=ButtonStyle.PRIMARY,
                icon_custom_emoji_id=5204046146955153467
            )
        ],
          [
            # Skip - PRIMARY (Blue)
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}", style=ButtonStyle.DANGER),
            
            # Pause - DANGER (Red)
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}", style=ButtonStyle.SUCCESS),
            
            # Resume - SUCCESS (Green)
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}", style=ButtonStyle.PRIMARY),
            
            # Replay - PRIMARY (Blue)
            InlineKeyboardButton(text="↻", callback_data=f"ADMIN Replay|{chat_id}", style=ButtonStyle.SUCCESS),
            
            # Stop - DANGER (Red)
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}", style=ButtonStyle.DANGER),
        ],
        [
            # Close - DANGER (Red)
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close", style=ButtonStyle.DANGER)
        ],
    ]
    return buttons


def stream_markup(_, videoid, chat_id):
    buttons = [
        [
            # Resume - SUCCESS (Green)
            InlineKeyboardButton(
                text="▷", 
                callback_data=f"ADMIN Resume|{chat_id}", 
                style=ButtonStyle.DANGER
            ),
            # Pause - DANGER (Red)
            InlineKeyboardButton(
                text="II", 
                callback_data=f"ADMIN Pause|{chat_id}", 
                style=ButtonStyle.SUCCESS
            ),
            # Replay - PRIMARY (Blue)
            InlineKeyboardButton(
                text="↻", 
                callback_data=f"ADMIN Replay|{chat_id}", 
                style=ButtonStyle.PRIMARY
            ),
            # Skip - PRIMARY (Blue)
            InlineKeyboardButton(
                text="‣‣I", 
                callback_data=f"ADMIN Skip|{chat_id}", 
                style=ButtonStyle.SUCCESS
            ),
            # Stop - DANGER (Red)
            InlineKeyboardButton(
                text="▢", 
                callback_data=f"ADMIN Stop|{chat_id}", 
                style=ButtonStyle.DANGER
            ),
        ],
        [
            # Close - DANGER (Red)
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], 
                callback_data="close", 
                style=ButtonStyle.DANGER
            )
        ],
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            # Audio Playlist - SUCCESS (Green)
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"brandedPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
                style=ButtonStyle.SUCCESS,
            ),
            # Video Playlist - PRIMARY (Blue)
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"brandedPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
                style=ButtonStyle.PRIMARY,
            ),
        ],
        [
            # Close Button - DANGER (Red)
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
                style=ButtonStyle.DANGER,
            ),
        ],
    ]
    return buttons



def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            # Live Stream Start - SUCCESS (Green)
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
                style=ButtonStyle.SUCCESS,
            ),
        ],
        [
            # Close Button - DANGER (Red)
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
                style=ButtonStyle.DANGER,
            ),
        ],
    ]
    return buttons



def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            # Audio Button - SUCCESS (Green)
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
                style=ButtonStyle.SUCCESS,
            ),
            # Video Button - PRIMARY (Blue)
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
                style=ButtonStyle.PRIMARY,
            ),
        ],
        [
            # Previous Button - PRIMARY (Blue)
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
                style=ButtonStyle.PRIMARY,
            ),
            # Close Button - DANGER (Red)
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
                style=ButtonStyle.DANGER,
            ),
            # Next Button - PRIMARY (Blue)
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
                style=ButtonStyle.PRIMARY,
            ),
        ],
    ]
    return buttons


## Telegram Markup


from pyrogram.types import InlineKeyboardButton
from pyrogram.enums import ButtonStyle

def telegram_markup(_, chat_id):
    buttons = [
        [
            # Next Button - SUCCESS (Green)
            InlineKeyboardButton(
                text="Next",
                callback_data=f"PanelMarkup None|{chat_id}",
                style=ButtonStyle.SUCCESS,
            ),
            # Close Button - DANGER (Red)
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"], 
                callback_data="close",
                style=ButtonStyle.DANGER,
            ),
        ],
    ]
    return buttons



## Queue Markup


def queue_markup(_, videoid, chat_id):
    buttons = [
        [
            # Add to Group - SUCCESS (Green)
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
                style=ButtonStyle.SUCCESS,
            ),
        ],
        [
            # Pause - DANGER (Red)
            InlineKeyboardButton(
                text="II ᴘᴀᴜsᴇ",
                callback_data=f"ADMIN Pause|{chat_id}",
                style=ButtonStyle.DANGER,
            ),
            # Stop - DANGER (Red)
            InlineKeyboardButton(
                text="▢ sᴛᴏᴘ", 
                callback_data=f"ADMIN Stop|{chat_id}",
                style=ButtonStyle.DANGER,
            ),
            # Skip - PRIMARY (Blue)
            InlineKeyboardButton(
                text="sᴋɪᴘ ‣‣I", 
                callback_data=f"ADMIN Skip|{chat_id}",
                style=ButtonStyle.PRIMARY,
            ),
        ],
        [
            # Resume - SUCCESS (Green)
            InlineKeyboardButton(
                text="▷ ʀᴇsᴜᴍᴇ", 
                callback_data=f"ADMIN Resume|{chat_id}",
                style=ButtonStyle.SUCCESS,
            ),
            # Replay - PRIMARY (Blue)
            InlineKeyboardButton(
                text="ʀᴇᴘʟᴀʏ ↺", 
                callback_data=f"ADMIN Replay|{chat_id}",
                style=ButtonStyle.PRIMARY,
            ),
        ],
        [
            # More Panel - PRIMARY (Blue)
            InlineKeyboardButton(
                text="⛦ ᴍᴏʀᴇ ❥",
                callback_data=f"PanelMarkup None|{chat_id}",
                style=ButtonStyle.PRIMARY,
            ),
        ],
    ]
    return buttons

def stream_markup2(_, chat_id):
    buttons = [
        [
            # Add to Group - SUCCESS (Green)
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
                style=ButtonStyle.SUCCESS,
            ),
        ],
        [
            # Resume - SUCCESS (Green)
            InlineKeyboardButton(
                text="▷", 
                callback_data=f"ADMIN Resume|{chat_id}", 
                style=ButtonStyle.DANGER
            ),
            # Pause - DANGER (Red)
            InlineKeyboardButton(
                text="II", 
                callback_data=f"ADMIN Pause|{chat_id}", 
                style=ButtonStyle.SUCCESS
            ),
            # Replay - PRIMARY (Blue)
            InlineKeyboardButton(
                text="↻", 
                callback_data=f"ADMIN Replay|{chat_id}", 
                style=ButtonStyle.PRIMARY
            ),
            # Skip - PRIMARY (Blue)
            InlineKeyboardButton(
                text="‣‣I", 
                callback_data=f"ADMIN Skip|{chat_id}", 
                style=ButtonStyle.SUCCESS
            ),
            # Stop - DANGER (Red)
            InlineKeyboardButton(
                text="▢", 
                callback_data=f"ADMIN Stop|{chat_id}", 
                style=ButtonStyle.DANGER
            ),
        ],
        [
            # Close Menu - DANGER (Red)
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"], 
                callback_data="close", 
                style=ButtonStyle.DANGER
            ),
        ],
    ]
    return buttons


def stream_markup_timer2(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)
    
    # Progress Bar Logic
    if 0 < umm <= 10:
        bar = "◉——————————"
    elif 10 < umm < 20:
        bar = "—◉—————————"
    elif 20 < umm < 30:
        bar = "——◉————————"
    elif 30 <= umm < 40:
        bar = "———◉———————"
    elif 40 <= umm < 50:
        bar = "————◉——————"
    elif 50 <= umm < 60:
        bar = "——————◉————"
    elif 60 <= umm < 70:
        bar = "———————◉———"
    else:
        bar = "——————————◉"

    buttons = [
        [
            # Timer Bar - PRIMARY (Blue)
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
                style=ButtonStyle.PRIMARY,
            )
        ],
        [
            # Resume - SUCCESS (Green)
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}", style=ButtonStyle.DANGER),
            
            # Pause - DANGER (Red)
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}", style=ButtonStyle.SUCCESS),
            
            # Replay - PRIMARY (Blue)
            InlineKeyboardButton(text="↻", callback_data=f"ADMIN Replay|{chat_id}", style=ButtonStyle.PRIMARY),
            
            # Skip - PRIMARY (Blue)
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}", style=ButtonStyle.SUCCESS),
            
            # Stop - DANGER (Red)
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}", style=ButtonStyle.DANGER),
        ],
        [
            # Close Button - DANGER (Red) with Premium Sticker
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"], 
                callback_data="close", 
                style=ButtonStyle.DANGER, 
                icon_custom_emoji_id=5409222721869459068
            ),
        ],
    ]
    return buttons



def panel_markup_1(_, videoid, chat_id):
    buttons = [
        [
            # Add to Group - SUCCESS (Green)
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
                style=ButtonStyle.SUCCESS,
            ),
        ],
        [
            # Shuffle - PRIMARY (Blue)
            InlineKeyboardButton(
                text="🎧 sᴜғғʟᴇ ❥",
                callback_data=f"ADMIN Shuffle|{chat_id}",
                style=ButtonStyle.PRIMARY,
            ),
            # Loop - PRIMARY (Blue)
            InlineKeyboardButton(
                text="ʟᴏᴏᴘ ↺", 
                callback_data=f"ADMIN Loop|{chat_id}",
                style=ButtonStyle.PRIMARY,
            ),
        ],
        [
            # Back 10 Sec - DANGER (Red)
            InlineKeyboardButton(
                text="◁ 10 sᴇᴄ",
                callback_data=f"ADMIN 1|{chat_id}",
                style=ButtonStyle.DANGER,
            ),
            # Forward 10 Sec - SUCCESS (Green)
            InlineKeyboardButton(
                text="10 sᴇᴄ ▷",
                callback_data=f"ADMIN 2|{chat_id}",
                style=ButtonStyle.SUCCESS,
            ),
        ],
        [
            # Home - PRIMARY (Blue)
            InlineKeyboardButton(
                text="❥ ʜᴏᴍᴇ ❥",
                callback_data=f"Pages Back|2|{videoid}|{chat_id}",
                style=ButtonStyle.PRIMARY,
            ),
            # Next - SUCCESS (Green)
            InlineKeyboardButton(
                text="❥ ɴᴇxᴛ ❥",
                callback_data=f"Pages Forw|2|{videoid}|{chat_id}",
                style=ButtonStyle.SUCCESS,
            ),
        ],
    ]
    return buttons



def panel_markup_2(_, videoid, chat_id):
    buttons = [
        [
            # Add to Group - SUCCESS (Green)
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
                style=ButtonStyle.SUCCESS,
            ),
        ],
        [
            # 0.5x - PRIMARY (Blue)
            InlineKeyboardButton(
                text="🕒 0.5x",
                callback_data=f"SpeedUP {chat_id}|0.5",
                style=ButtonStyle.PRIMARY,
            ),
            # 0.75x - PRIMARY (Blue)
            InlineKeyboardButton(
                text="🕓 0.75x",
                callback_data=f"SpeedUP {chat_id}|0.75",
                style=ButtonStyle.PRIMARY,
            ),
            # 1.0x (Normal) - SUCCESS (Green)
            InlineKeyboardButton(
                text="🕤 1.0x",
                callback_data=f"SpeedUP {chat_id}|1.0",
                style=ButtonStyle.SUCCESS,
            ),
        ],
        [
            # 1.5x - DANGER (Red)
            InlineKeyboardButton(
                text="🕤 1.5x",
                callback_data=f"SpeedUP {chat_id}|1.5",
                style=ButtonStyle.DANGER,
            ),
            # 2.0x - DANGER (Red)
            InlineKeyboardButton(
                text="🕛 2.0x",
                callback_data=f"SpeedUP {chat_id}|2.0",
                style=ButtonStyle.DANGER,
            ),
        ],
        [
            # Back Button - PRIMARY (Blue)
            InlineKeyboardButton(
                text="❥ ʙᴀᴄᴋ ❥",
                callback_data=f"Pages Back|1|{videoid}|{chat_id}",
                style=ButtonStyle.PRIMARY,
            ),
        ],
    ]
    return buttons



def panel_markup_5(_, videoid, chat_id):
    buttons = [
        [
            # Add to Group - SUCCESS (Green)
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
                style=ButtonStyle.SUCCESS,
            ),
        ],
        [
            # Pause - DANGER (Red)
            InlineKeyboardButton(
                text="ᴘᴀᴜsᴇ", 
                callback_data=f"ADMIN Pause|{chat_id}",
                style=ButtonStyle.DANGER,
            ),
            # Stop - DANGER (Red)
            InlineKeyboardButton(
                text="sᴛᴏᴘ", 
                callback_data=f"ADMIN Stop|{chat_id}",
                style=ButtonStyle.DANGER,
            ),
            # Skip - PRIMARY (Blue)
            InlineKeyboardButton(
                text="sᴋɪᴘ", 
                callback_data=f"ADMIN Skip|{chat_id}",
                style=ButtonStyle.PRIMARY,
            ),
        ],
        [
            # Resume - SUCCESS (Green)
            InlineKeyboardButton(
                text="ʀᴇsᴜᴍᴇ", 
                callback_data=f"ADMIN Resume|{chat_id}",
                style=ButtonStyle.SUCCESS,
            ),
            # Replay - PRIMARY (Blue)
            InlineKeyboardButton(
                text="ʀᴇᴘʟᴀʏ", 
                callback_data=f"ADMIN Replay|{chat_id}",
                style=ButtonStyle.PRIMARY,
            ),
        ],
        [
            # Home - PRIMARY (Blue)
            InlineKeyboardButton(
                text="❥ ʜᴏᴍᴇ ❥",
                callback_data=f"MainMarkup {videoid}|{chat_id}",
                style=ButtonStyle.PRIMARY,
            ),
            # Next - SUCCESS (Green)
            InlineKeyboardButton(
                text="❥ ɴᴇxᴛ ❥",
                callback_data=f"Pages Forw|1|{videoid}|{chat_id}",
                style=ButtonStyle.SUCCESS,
            ),
        ],
    ]
    return buttons


def panel_markup_3(_, videoid, chat_id):
    buttons = [
        [
            # 0.5x - PRIMARY (Blue)
            InlineKeyboardButton(
                text="🕒 0.5x",
                callback_data=f"SpeedUP {chat_id}|0.5",
                style=ButtonStyle.PRIMARY,
            ),
            # 0.75x - PRIMARY (Blue)
            InlineKeyboardButton(
                text="🕓 0.75x",
                callback_data=f"SpeedUP {chat_id}|0.75",
                style=ButtonStyle.PRIMARY,
            ),
            # 1.0x (Normal) - SUCCESS (Green)
            InlineKeyboardButton(
                text="🕤 1.0x",
                callback_data=f"SpeedUP {chat_id}|1.0",
                style=ButtonStyle.SUCCESS,
            ),
        ],
        [
            # 1.5x - DANGER (Red)
            InlineKeyboardButton(
                text="🕤 1.5x",
                callback_data=f"SpeedUP {chat_id}|1.5",
                style=ButtonStyle.DANGER,
            ),
            # 2.0x - DANGER (Red)
            InlineKeyboardButton(
                text="🕛 2.0x",
                callback_data=f"SpeedUP {chat_id}|2.0",
                style=ButtonStyle.DANGER,
            ),
        ],
        [
            # Back Button - PRIMARY (Blue)
            InlineKeyboardButton(
                text="❥ ʙᴀᴄᴋ ❥",
                callback_data=f"Pages Back|2|{videoid}|{chat_id}",
                style=ButtonStyle.PRIMARY,
            ),
        ],
    ]
    return buttons



def panel_markup_4(_, vidid, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)
    
    # Progress Bar Logic Fix
    if 0 < umm <= 10:
        bar = "◉——————————"
    elif 10 < umm < 20:
        bar = "—◉—————————"
    elif 20 < umm < 30:
        bar = "——◉————————"
    elif 30 <= umm < 40:
        bar = "———◉———————"
    elif 40 <= umm < 50:
        bar = "————◉——————"
    elif 50 <= umm < 60:
        bar = "——————◉————"
    elif 60 <= umm < 70:
        bar = "———————◉———"
    else:
        bar = "——————————◉"

    buttons = [
        [
            # Timer/Progress Bar - PRIMARY (Blue)
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
                style=ButtonStyle.PRIMARY,
            )
        ],
        [
            # Pause - DANGER (Red)
            InlineKeyboardButton(
                text="II ᴘᴀᴜsᴇ",
                callback_data=f"ADMIN Pause|{chat_id}",
                style=ButtonStyle.DANGER,
            ),
            # Stop - DANGER (Red)
            InlineKeyboardButton(
                text="▢ sᴛᴏᴘ ▢", 
                callback_data=f"ADMIN Stop|{chat_id}",
                style=ButtonStyle.DANGER,
            ),
            # Skip - PRIMARY (Blue)
            InlineKeyboardButton(
                text="sᴋɪᴘ ‣‣I", 
                callback_data=f"ADMIN Skip|{chat_id}",
                style=ButtonStyle.PRIMARY,
            ),
        ],
        [
            # Resume - SUCCESS (Green)
            InlineKeyboardButton(
                text="▷ ʀᴇsᴜᴍᴇ", 
                callback_data=f"ADMIN Resume|{chat_id}",
                style=ButtonStyle.SUCCESS,
            ),
            # Replay - PRIMARY (Blue)
            InlineKeyboardButton(
                text="ʀᴇᴘʟᴀʏ ↺", 
                callback_data=f"ADMIN Replay|{chat_id}",
                style=ButtonStyle.PRIMARY,
            ),
        ],
        [
            # Home Button - PRIMARY (Blue)
            InlineKeyboardButton(
                text="❥ ʜᴏᴍᴇ ❥",
                callback_data=f"MainMarkup {vidid}|{chat_id}",
                style=ButtonStyle.PRIMARY,
            ),
        ],
    ]

    return buttons

def panel_markup_clone(_, vidid, chat_id):
    buttons = [
        [
            # Add to Group - SUCCESS (Green)
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
                style=ButtonStyle.SUCCESS,
            ),
        ],
        [
            # Resume - SUCCESS (Green)
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}", style=ButtonStyle.SUCCESS),
            # Pause - DANGER (Red)
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}", style=ButtonStyle.DANGER),
            # Replay - PRIMARY (Blue)
            InlineKeyboardButton(text="↻", callback_data=f"ADMIN Replay|{chat_id}", style=ButtonStyle.PRIMARY),
            # Skip - PRIMARY (Blue)
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}", style=ButtonStyle.PRIMARY),
            # Stop - DANGER (Red)
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}", style=ButtonStyle.DANGER),
        ],
        [
            # Download Video - PRIMARY (Blue)
            InlineKeyboardButton(
                text="📥 ᴠɪᴅᴇᴏ", 
                callback_data=f"downloadvideo {vidid}",
                style=ButtonStyle.PRIMARY,
            ),
            # Download Audio - SUCCESS (Green)
            InlineKeyboardButton(
                text="📥 ᴀᴜᴅɪᴏ", 
                callback_data=f"downloadaudio {vidid}",
                style=ButtonStyle.SUCCESS,
            ),
        ],
        [
            # Add to Playlist - PRIMARY (Blue)
            InlineKeyboardButton(
                text="✚ ᴘʟᴀʏʟɪsᴛ ✚", 
                callback_data=f"branded_playlist {vidid}",
                style=ButtonStyle.PRIMARY,
            ),
        ],
    ]

    return buttons
