from os import environ
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = environ["BOT_TOKEN"]
BOT_PREFIX = environ["BOT_PREFIX"]