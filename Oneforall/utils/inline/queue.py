from typing import Union
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import ButtonStyle

def queue_markup(
    _,
    DURATION,
    CPLAY,
    videoid,
    played: Union[bool, int] = None,
    dur: Union[bool, int] = None,
):
    not_dur = [
        [
            # Get Queued - SUCCESS (Green)
            InlineKeyboardButton(
                text=_["QU_B_1"],
                callback_data=f"GetQueued {CPLAY}|{videoid}",
                style=ButtonStyle.SUCCESS,
            ),
            # Close - DANGER (Red)
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
                style=ButtonStyle.DANGER,
            ),
        ]
    ]
    dur_buttons = [
        [
            # Timer Button - PRIMARY (Blue)
            InlineKeyboardButton(
                text=_["QU_B_2"].format(played, dur),
                callback_data="GetTimer",
                style=ButtonStyle.PRIMARY,
            )
        ],
        [
            # Get Queued - SUCCESS (Green)
            InlineKeyboardButton(
                text=_["QU_B_1"],
                callback_data=f"GetQueued {CPLAY}|{videoid}",
                style=ButtonStyle.SUCCESS,
            ),
            # Close - DANGER (Red)
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
                style=ButtonStyle.DANGER,
            ),
        ],
    ]
    upl = InlineKeyboardMarkup(not_dur if DURATION == "Unknown" else dur_buttons)
    return upl


def queue_back_markup(_, CPLAY):
    upl = InlineKeyboardMarkup(
        [
            [
                # Back Button - PRIMARY (Blue)
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"queue_back_timer {CPLAY}",
                    style=ButtonStyle.PRIMARY,
                ),
                # Close Button - DANGER (Red)
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                    style=ButtonStyle.DANGER,
                ),
            ]
        ]
    )
    return upl


def aq_markup(_, chat_id):
    buttons = [
        [
            # Controls: Resume (Green), Pause (Red), Skip (Blue), Stop (Red)
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}", style=ButtonStyle.SUCCESS),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}", style=ButtonStyle.PRIMARY),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}", style=ButtonStyle.PRIMARY),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}", style=ButtonStyle.SUCCESS),
        ],
        [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close", style=ButtonStyle.DANGER)],
    ]
    return buttons


def queuemarkup(_, vidid, chat_id):
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
                text="ʀᴇsᴜᴍ", 
                callback_data=f"ADMIN Resume|{chat_id}",
                style=ButtonStyle.SUCCESS,
            ),
            # Replay - PRIMARY (Blue)
            InlineKeyboardButton(
                text="ʀᴇᴘʟᴀ", 
                callback_data=f"ADMIN Replay|{chat_id}",
                style=ButtonStyle.PRIMARY,
            ),
        ],
        [
            # More/Support - PRIMARY (Blue)
            InlineKeyboardButton(
                text="๏ ᴍᴏʀᴇ ๏",
                url="https://t.me/BRANDED_WORLD",
                style=ButtonStyle.PRIMARY,
            ),
        ],
    ]
    return buttons
