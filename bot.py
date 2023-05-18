from src.handlers.users.category import router
from loader import bot, dp


dp.include_router(router)
dp.run_polling(bot)
