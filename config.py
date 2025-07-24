from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", 27353035))
API_HASH = getenv("API_HASH", "cf2a75861140ceb746c7796e07cbde9e")
BOT_TOKEN = getenv("BOT_TOKEN", None)
OWNER_ID = int(getenv("OWNER_ID", "7800338935"))
MONGO_URL = getenv("MONGO_URL", None)
SUPPORT_GRP = getenv("SUPPORT_GRP", "PersionalDestek")
UPDATE_CHNL = getenv("UPDATE_CHNL", "PersionalSupport")
OWNER_USERNAME = getenv("OWNER_USERNAME", "PersionalTeamBot")

# Random Start Images
IMG = [
    "https://files.catbox.moe/b4zm7m.jpg",
]


# Random Stickers
STICKER = [
    "CAACAgUAAx0CYlaJawABBy4vZaieO6T-Ayg3mD-JP-f0yxJngIkAAv0JAALVS_FWQY7kbQSaI-geBA",
    "CAACAgUAAx0CYlaJawABBy4rZaid77Tf70SV_CfjmbMgdJyVD8sAApwLAALGXCFXmCx8ZC5nlfQeBA",
    "CAACAgUAAx0CYlaJawABBy4jZaidvIXNPYnpAjNnKgzaHmh3cvoAAiwIAAIda2lVNdNI2QABHuVVHgQ",
]


EMOJIOS = [
    "💣",
    "💥",
    "🪄",
    "🧨",
    "⚡",
    "🤡",
    "👻",
    "🎃",
    "🎩",
    "🕊",
]
