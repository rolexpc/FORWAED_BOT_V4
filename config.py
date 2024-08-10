import os
from os import environ

class Config:
    API_ID = os.environ.get("API_ID", "12618934")
    API_HASH = os.environ.get("API_HASH", "49aacd0bc2f8924add29fb02e20c8a16")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7483385027:AAGzSus_uGxY6JshEFZcCShyJZCV-3TQHXU") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "forward-bot") 
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://Fahadh:Fahadh@cluster0.cpeyano.mongodb.net/")
    DB_NAME = os.environ.get("DB_NAME", "Fahadh")
    PORT = int(os.environ.get("PORT", "8080"))
    OWNER_ID = [int(id) for id in os.environ.get("OWNER_ID", '1297128957').split()]


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    


