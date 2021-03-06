import os

# Partial URL for coin logo
CMC_LOGO_URL_PARTIAL = "https://s2.coinmarketcap.com/static/img/coins/128x128/"

CFG_DIR = "conf"
CFG_FILE = "config.json"
BOT_TKN_FILE = "bot.token"
CRYPAN_TKN_FILE = "cryptopanic.token"

LOG_DIR = "log"
LOG_FILE = "opencryptobot.log"

DAT_DIR = "data"
DAT_FILE = "opencryptobot.db"

SQL_DIR = "sql"

RES_DIR = "res"
BPMN_DIR = os.path.join(RES_DIR, "bpmn")

MAX_TG_MSG_LEN = 4096
CG_DATA_LIMIT = 2000
DEF_CACHE_REFRESH = 86400  # In seconds
DEF_UPDATE_CHECK = 86400  # In seconds
