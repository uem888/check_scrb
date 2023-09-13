from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# Создаем экземпляры бота и диспетчера
bot = Bot(token="6210531204:AAGSgQrxSDfgzmW6JoYpwHy2n8_1QRGdqTk")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    # Проверяем подписку пользователя на канал
    is_subscribed = await bot.get_chat_member(chat_id="-1001610247765", user_id=message.from_user.id)  # chat_id нужно поменять id нужного канала/чата
    if is_subscribed.is_chat_member():
        await message.answer("Ты подписан на канал! Получай вкусняшки!")
        # Здесь можно разместить код для отправки вкусняшки
    else:
        channel_link = "https://t.me/egorvnegor"  # Поменяйте ссылку на свою
        await message.answer(f"Подпишись на канал {channel_link}, чтобы получать вкусняшки!")
        # Здесь можно разместить код для приглашения подписаться на канал

# Запускаем бота
if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
