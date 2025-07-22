from pyrogram.types import InlineKeyboardButton

from config import SUPPORT_GRP, UPDATE_CHNL
from Venom import OWNER
from Venom import VenomX

DEV_OP = [
    [
        InlineKeyboardButton(text="👤 Sahibim", user_id=OWNER),
        InlineKeyboardButton(text="📤 Support", url=f"https://t.me/{SUPPORT_GRP}"),
    ],
    [
        InlineKeyboardButton(
            text="➕ Qrupa Əlavə et ➕",
            url=f"https://t.me/{VenomX.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="📚 Kömək", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="🤍 Söhbət Qrupu", url=f"https://t.me/{SUPPORT_GRP}"),
        InlineKeyboardButton(text="⚙️ Haqqında", callback_data="ABOUT"),
    ],
]

PNG_BTN = [
    [
        InlineKeyboardButton(
            text="➕ Məni Qrupuna Əlavə et ➕",
            url=f"https://t.me/{VenomX.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(
            text="🔃 Bağla ",
            callback_data="CLOSE",
        ),
    ],
]


BACK = [
    [
        InlineKeyboardButton(text="🔙 Geri", callback_data="BACK"),
    ],
]


HELP_BTN = [
    [
        InlineKeyboardButton(text="🐳 ᴄʜᴀᴛʙᴏᴛ 🐳", callback_data="CHATBOT_CMD"),
        InlineKeyboardButton(text="🎄 ᴛᴏᴏʟs 🎄", callback_data="TOOLS_DATA"),
    ],
    [
        InlineKeyboardButton(text="⬅️ Geri", callback_data="BACK"),
        InlineKeyboardButton(text="🔃 Bağla", callback_data="CLOSE"),
    ],
]


CLOSE_BTN = [
    [
        InlineKeyboardButton(text="🔃 Bağla", callback_data="CLOSE"),
    ],
]


CHATBOT_ON = [
    [
        InlineKeyboardButton(text="ᴇɴᴀʙʟᴇ", callback_data=f"addchat"),
        InlineKeyboardButton(text="ᴅɪsᴀʙʟᴇ", callback_data=f"rmchat"),
    ],
]


MUSIC_BACK_BTN = [
    [
        InlineKeyboardButton(text="sᴏᴏɴ", callback_data=f"soom"),
    ],
]

S_BACK = [
    [
        InlineKeyboardButton(text="🔙 Geri", callback_data="SBACK"),
        InlineKeyboardButton(text="🔃 Bağla", callback_data="CLOSE"),
    ],
]


CHATBOT_BACK = [
    [
        InlineKeyboardButton(text="🔙 Geri", callback_data="CHATBOT_BACK"),
        InlineKeyboardButton(text="🔃 Bağla", callback_data="CLOSE"),
    ],
]


HELP_START = [
    [
        InlineKeyboardButton(text="📚 Kömək", callback_data="HELP"),
        InlineKeyboardButton(text="🔃 Bağla", callback_data="CLOSE"),
    ],
]


HELP_BUTN = [
    [
        InlineKeyboardButton(
            text="📚 Köəmk", url=f"https://t.me/{VenomX.username}?start=help"
        ),
        InlineKeyboardButton(text="🔃 Bağla", callback_data="CLOSE"),
    ],
]


ABOUT_BTN = [
    [
        InlineKeyboardButton(text="📤 Support", url=f"https://t.me/{SUPPORT_GRP}"),
        InlineKeyboardButton(text="📚 Kömək", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="👤 Sahibim", user_id=OWNER),
        InlineKeyboardButton(text="🤍 Söhbət Qrupu", url=f"https://t.me/{SUPPORT_GRP}"),
    ],
    [
        InlineKeyboardButton(text="📤 Support", url=f"https://t.me/{UPDATE_CHNL}"),
        InlineKeyboardButton(text="🔙 Geri", callback_data="BACK"),
    ],
]
