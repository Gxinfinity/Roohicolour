from pyrogram.types import InlineKeyboardButton
from pyrogram.enums import ButtonStyle

class BUTTONS(object):
    MBUTTON = [
        [
            # Success (Green) | Primary (Blue) | Success (Green)
            InlineKeyboardButton("🤖 CʜᴀᴛGPT", callback_data="mplus HELP_ChatGPT", style=ButtonStyle.SUCCESS),
            InlineKeyboardButton("📜 Hɪsᴛᴏʀʏ", callback_data="mplus HELP_History", style=ButtonStyle.PRIMARY),
            InlineKeyboardButton("🎬 Rᴇᴇʟ", callback_data="mplus HELP_Reel", style=ButtonStyle.SUCCESS),
        ],
        [
            # Primary (Blue) | Success (Green) | Primary (Blue)
            InlineKeyboardButton("📢 Tᴀɢ-Aʟʟ", callback_data="mplus HELP_TagAll", style=ButtonStyle.PRIMARY),
            InlineKeyboardButton("ℹ️ Iɴꜰᴏ", callback_data="mplus HELP_Info", style=ButtonStyle.SUCCESS),
            InlineKeyboardButton("⚙️ Exᴛʀᴀ", callback_data="mplus HELP_Extra", style=ButtonStyle.PRIMARY),
        ],
        [
            InlineKeyboardButton("👩‍❤️‍👨 ᴄᴏᴜᴘʟᴇꜱ", callback_data="mplus HELP_Couples", style=ButtonStyle.SUCCESS),
            InlineKeyboardButton("🎭 Aᴄᴛɪᴏɴ", callback_data="mplus HELP_Action", style=ButtonStyle.PRIMARY),
            InlineKeyboardButton("🔍 Sᴇᴀʀᴄʜ", callback_data="mplus HELP_Search", style=ButtonStyle.SUCCESS),
        ],
        [
            InlineKeyboardButton("🔤 ғᴏɴᴛ", callback_data="mplus HELP_Font", style=ButtonStyle.PRIMARY),
            InlineKeyboardButton("🤖 Bᴏᴛs", callback_data="mplus HELP_Bots", style=ButtonStyle.SUCCESS),
            InlineKeyboardButton("📊 Ⓣ-ɢʀᴀᴘʜ", callback_data="mplus HELP_TG", style=ButtonStyle.PRIMARY),
        ],
        [
            InlineKeyboardButton("📂 Sᴏᴜʀᴄᴇ", callback_data="mplus HELP_Source", style=ButtonStyle.SUCCESS),
            InlineKeyboardButton("⚖️ Tʀᴜᴛʜ-ᗪᴀʀᴇ", callback_data="mplus HELP_TD", style=ButtonStyle.PRIMARY),
            InlineKeyboardButton("🧩 Qᴜɪᴢ", callback_data="mplus HELP_Quiz", style=ButtonStyle.SUCCESS),
        ],
        [
            InlineKeyboardButton("🗣️ ᴛᴛs", callback_data="mplus HELP_TTS", style=ButtonStyle.PRIMARY),
            InlineKeyboardButton("📻 Rᴀᴅɪᴏ", callback_data="mplus HELP_Radio", style=ButtonStyle.SUCCESS),
            InlineKeyboardButton("📝 ǫᴜᴏᴛʟʏ", callback_data="mplus HELP_Q", style=ButtonStyle.PRIMARY),
        ],
        [
            # Navigation Buttons
            InlineKeyboardButton("◁", callback_data=f"settings_back_helper", style=ButtonStyle.PRIMARY),
            InlineKeyboardButton("🗑️ ᴄʟᴏsᴇ 🗑️", callback_data=f"mbot_cb", style=ButtonStyle.DANGER),
            InlineKeyboardButton("▷", callback_data=f"managebot123 settings_back_helper", style=ButtonStyle.PRIMARY),
        ],
    ]
