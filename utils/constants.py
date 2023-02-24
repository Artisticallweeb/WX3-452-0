from os import environ
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = environ["BOT_TOKEN"]
BOT_PREFIX = environ["BOT_PREFIX"]
REDDIT_CLIENT = environ["REDDIT_CLIENT"]
REDDIT_SECRET = environ["REDDIT_SECRET"]
