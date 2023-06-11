import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = 10012378
API_HASH = e4b851e683d75f83293ecd51ae135976
BOT_TOKEN = 5166508400:AAEBwoocaTS-Ij4ilIH-wCpl1J6QQP6wupI

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = https://telegra.ph/file/cdeae1b25b5d9799e9cde.jpg
https://telegra.ph/file/04c637aceecfce8d4af39.jpg
https://telegra.ph/file/bab9f8b3bdf18acc11991.jpg
https://telegra.ph/file/5d7175eb1a5d27ab40520.jpg
https://telegra.ph/file/45333a1182fdd724a3253.jpg
https://telegra.ph/file/0eebc207b4d46c8779d0d.jpg
https://telegra.ph/file/5231b4d99e13fc9320682.jpg
https://telegra.ph/file/e50450c34f13b6d64bb87.jpg
https://telegra.ph/file/8bf0854c24e5175611365.jpg
https://telegra.ph/file/95ae0fd0a902d811e614c.jpg
https://telegra.ph/file/d35e6daf8389f4ba6c033.jpg
https://telegra.ph/file/55cf3c5a5ef80ae6045c9.jpg
https://telegra.ph/file/094532fd1fafbe7e0de73.jpg
https://telegra.ph/file/1574016692fbfe25ee24b.jpg
https://telegra.ph/file/4850fbbdb1e7c79a459f9.jpg
https://telegra.ph/file/6f7408fc855f7c0d2f095.jpg
https://telegra.ph/file/06231a267ecc99b8be7ea.jpg
https://telegra.ph/file/4927fbbd32f4e1076e7de.jpg
https://telegra.ph/file/286c0c5975027e0ba0ed1.jpg
https://telegra.ph/file/2967c25a5e95b627b85d9.jpg
https://telegra.ph/file/496d3765872638f3d8b84.jpg
https://telegra.ph/file/44ee0109180558bdc9c3a.jpg
https://telegra.ph/file/e5c3272ccb1346fe8a724.jpg
https://telegra.ph/file/c8bff892a7239f7068c3f.jpg

# Admins, Channels & Users
ADMINS = 901899557 5238714460
CHANNELS = -1001489791799
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = -1001511186264
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = mongodb+srv://alexademiebot:alexademiebot@cluster0.wiern.mongodb.net/myFirstDatabase?retryWrites=true&w=majority
DATABASE_NAME = JinxVerseV2
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
LOG_CHANNEL = -1001724781682
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'TeamEvamaria')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = False
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "False")), False)
CUSTOM_FILE_CAPTION = <b>{file_name}</b>

○ <b>Courtesy of <a href=https://t.me/showsarchive>Cine Verse Archive</a></b>
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = <b>{title} | {year} • {kind}</b>

<b>Rating ⭐️: {rating} / 10 on IMDb</b>
<b>Runtime: {runtime} Minutes</b>
<b>Genres: {genres}</b>

<b>Language: {languages} | Subbed</b>
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = False
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = False
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
