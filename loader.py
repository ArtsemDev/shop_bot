from pathlib import Path

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from session import session
from src.schemas import Settings

load_dotenv()


BASE_DIR = Path(__file__).resolve().parent
SETTINGS = Settings()
bot = Bot(
    token=SETTINGS.BOT_TOKEN.get_secret_value(),
    parse_mode='HTML',
    session=session
)
dp = Dispatcher()
