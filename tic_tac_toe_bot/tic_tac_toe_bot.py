from aiogram.utils import executor
from create_bot import dp
import commands

commands.register_handlers_commands(dp)

executor.start_polling(dp, skip_updates=True)