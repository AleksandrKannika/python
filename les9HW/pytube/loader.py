from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage


token = '5510996756:AAERwrpf9ZUB0jDEbY3A5ucKooZt8_5nB4E'

bot = Bot(token=token, parse_mode=types.ParseMode.HTML)

storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)