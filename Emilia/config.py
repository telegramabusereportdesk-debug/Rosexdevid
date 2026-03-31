import orjson
import os


def get_user_list(config, key):
    with open("{}/Emilia/{}".format(os.getcwd(), config), "rb") as json_file:
        return orjson.loads(json_file.read())[key]


class Config(object):
    API_HASH = "a09fd0f00561713230b4d04b27f4b3ac"
    API_ID =36277508

    BOT_ID = 521
    BOT_USERNAME = "@MissRose_XRobot"

    MONGO_DB_URL = "mongodb+srv://rj5706603:O95nvJYxapyDHfkw@cluster0.fzmckei.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    SUPPORT_CHAT = "https://t.me/+WITJGdIyT2kzOGI1"
    UPDATE_CHANNEL = "TheTechXDev"
    START_PIC = "https://pic-bstarstatic.akamaized.net/ugc/9e98b6c8872450f3e8b19e0d0aca02deff02981f.jpg@1200w_630h_1e_1c_1f.webp"
    DEV_USERS = [6211784722]
    TOKEN = "8603959688:AAFlVj8ZDQxZJ5iTXzBucSMvP3r_eWrnb-Y"
    CLONE_LIMIT = 50

    REDIS_URL = os.getenv("REDIS_URL", "https://fine-flounder-25319.upstash.io")
    REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", None)

    EVENT_LOGS = -1002778788447
    OWNER_ID = 6211784722

    TEMP_DOWNLOAD_DIRECTORY = "./"
    BOT_NAME = "Rose"
    WALL_API = "6950f53"
    GROQ_API_KEY = "gsk_mm"


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
