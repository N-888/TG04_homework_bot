# Импортируем модуль asyncio, чтобы запускать асинхронную функцию main().
import asyncio

# Импортируем модуль logging, чтобы видеть служебные сообщения в консоли PyCharm.
import logging

# Импортируем класс Bot, чтобы создать объект Telegram-бота.
from aiogram import Bot

# Импортируем класс Dispatcher, чтобы регистрировать роутеры и запускать обработку сообщений.
from aiogram import Dispatcher

# Импортируем токен из файла config.py.
from config import TOKEN

# Импортируем роутер с командами /start и обработкой reply-кнопок.
from handlers.menu_handlers import menu_router

# Импортируем роутер с командой /links.
from handlers.links_handlers import links_router

# Импортируем роутер с командой /dynamic и callback-кнопками.
from handlers.dynamic_handlers import dynamic_router


# Создаём главную асинхронную функцию запуска всего бота.
async def main() -> None:
    # Включаем базовое логирование уровня INFO, чтобы видеть запуск и работу бота в консоли.
    logging.basicConfig(level=logging.INFO)

    # Создаём объект бота и передаём ему токен, который хранится в config.py.
    bot = Bot(token=TOKEN)

    # Создаём диспетчер, который будет принимать сообщения и распределять их по обработчикам.
    dp = Dispatcher()

    # Подключаем роутер с командой /start и кнопками Привет / Пока.
    dp.include_router(menu_router)

    # Подключаем роутер с командой /links.
    dp.include_router(links_router)

    # Подключаем роутер с командой /dynamic и inline-callback-кнопками.
    dp.include_router(dynamic_router)

    # Пытаемся запустить бота безопасно и корректно.
    try:
        # Удаляем webhook и сбрасываем старые необработанные сообщения, чтобы бот стартовал "с чистого листа".
        await bot.delete_webhook(drop_pending_updates=True)

        # Запускаем long polling, чтобы бот начал получать сообщения от Telegram.
        await dp.start_polling(bot)

    # Гарантированно закрываем HTTP-сессию бота, даже если программа остановится.
    finally:
        # Закрываем сетевую сессию, чтобы не оставлять незавершённые подключения.
        await bot.session.close()


# Проверяем, что файл запущен напрямую, а не импортирован из другого файла.
if __name__ == "__main__":
    # Пытаемся аккуратно запустить асинхронную функцию main().
    try:
        # Запускаем точку входа в программу.
        asyncio.run(main())

    # Ловим остановку с клавиатуры, например если вы нажали красный квадрат Stop в PyCharm или Ctrl + C в терминале.
    except KeyboardInterrupt:
        # Печатаем в консоль понятное сообщение о том, что бот остановлен.
        print("Бот остановлен пользователем.")