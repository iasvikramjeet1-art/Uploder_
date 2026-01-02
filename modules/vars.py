#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "24401265"))
API_HASH = environ.get("API_HASH", "628f9742666d8b5e437d37adaa453234")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

OWNER = int(environ.get("OWNER", "7899422608"))
CREDIT = environ.get("CREDIT", "𓆩𝑺𝒉𝒊𝒏𝒆 𝑩𝒚 𝑳𝒐𝒓𝒅𓆪")
cookies_file_path = os.getenv("cookies_file_path", "youtube_cookies.txt")

TOTAL_USER = os.environ.get('TOTAL_USERS', '7899422608').split('5822555086')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '7899422608').split('5822555086')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))



