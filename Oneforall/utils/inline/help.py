from typing import Union
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import ButtonStyle
from Oneforall import app

def help_pannel(_, START: Union[bool, int] = None):
    # Close Button - DANGER (Red)
    first = [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data=f"close", style=ButtonStyle.DANGER)]
    
    # Navigation Row - PRIMARY (Blue) for Pages, DANGER (Red) for Back
    second = [
        InlineKeyboardButton(
            text=_["BACK_PAGE"],
            callback_data=f"mbot_cb",
            style=ButtonStyle.PRIMARY,
        ),
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
            style=ButtonStyle.DANGER,
        ),
        InlineKeyboardButton(
            text=_["NEXT_PAGE"],
            callback_data=f"mbot_cb",
            style=ButtonStyle.PRIMARY,
        ),
    ]
    
    mark = second if START else first
    
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text=_["H_B_1"], callback_data="help_callback hb1", style=ButtonStyle.SUCCESS),
                InlineKeyboardButton(text=_["H_B_2"], callback_data="help_callback hb2", style=ButtonStyle.PRIMARY),
                InlineKeyboardButton(text=_["H_B_3"], callback_data="help_callback hb3", style=ButtonStyle.SUCCESS),
            ],
            [
                InlineKeyboardButton(text=_["H_B_4"], callback_data="help_callback hb4", style=ButtonStyle.PRIMARY),
                InlineKeyboardButton(text=_["H_B_5"], callback_data="help_callback hb5", style=ButtonStyle.SUCCESS),
                InlineKeyboardButton(text=_["H_B_6"], callback_data="help_callback hb6", style=ButtonStyle.PRIMARY),
            ],
            [
                InlineKeyboardButton(text=_["H_B_7"], callback_data="help_callback hb7", style=ButtonStyle.DANGER),
                InlineKeyboardButton(text=_["H_B_8"], callback_data="help_callback hb8", style=ButtonStyle.PRIMARY),
                InlineKeyboardButton(text=_["H_B_9"], callback_data="help_callback hb9", style=ButtonStyle.DANGER),
            ],
            [
                InlineKeyboardButton(text=_["H_B_10"], callback_data="help_callback hb10", style=ButtonStyle.PRIMARY),
                InlineKeyboardButton(text=_["H_B_11"], callback_data="help_callback hb11", style=ButtonStyle.SUCCESS),
                InlineKeyboardButton(text=_["H_B_12"], callback_data="help_callback hb12", style=ButtonStyle.PRIMARY),
            ],
            [
                InlineKeyboardButton(text=_["H_B_13"], callback_data="help_callback hb13", style=ButtonStyle.SUCCESS),
                InlineKeyboardButton(text=_["H_B_14"], callback_data="help_callback hb14", style=ButtonStyle.PRIMARY),
                InlineKeyboardButton(text=_["H_B_15"], callback_data="help_callback hb15", style=ButtonStyle.SUCCESS),
            ],
            [
                InlineKeyboardButton(text=_["H_B_26"], callback_data="help_callback hb17", style=ButtonStyle.DANGER),
                InlineKeyboardButton(text=_["H_B_25"], callback_data="help_callback hb16", style=ButtonStyle.SUCCESS),
                InlineKeyboardButton(text="🎮 ғᴜɴ ɢᴀᴍᴇ", callback_data="help_callback hb21", style=ButtonStyle.DANGER),
            ],
            [
                InlineKeyboardButton(text=_["H_B_27"], callback_data="help_callback hb18", style=ButtonStyle.SUCCESS),
                InlineKeyboardButton(text=_["H_B_28"], callback_data="help_callback hb19", style=ButtonStyle.PRIMARY),
                InlineKeyboardButton(text="✨ ғsᴜʙ", callback_data="help_callback hb20", style=ButtonStyle.SUCCESS),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                # Back Button - DANGER (Red)
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                    style=ButtonStyle.DANGER,
                ),
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            # Help in PM - SUCCESS (Green)
            InlineKeyboardButton(
                text=_["S_B_4"],
                url=f"https://t.me/{app.username}?start=help",
                style=ButtonStyle.SUCCESS,
            ),
        ],
    ]
    return buttons
