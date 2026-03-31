# Импортируем класс Router, чтобы создать отдельный роутер для меню и reply-кнопок.
from aiogram import Router

# Импортируем объект F, чтобы удобно фильтровать текст сообщений.
from aiogram import F

# Импортируем фильтр CommandStart, чтобы ловить команду /start.
from aiogram.filters import CommandStart

# Импортируем тип Message, чтобы работать с обычными сообщениями пользователя.
from aiogram.types import Message

# Импортируем функцию создания главной reply-клавиатуры.
from keyboards.user_keyboards import get_main_menu_keyboard


# Создаём роутер для команд и кнопок главного меню.
menu_router = Router()


# Регистрируем обработчик команды /start.
@menu_router.message(CommandStart())
# Создаём асинхронную функцию, которая будет выполняться при вводе /start.
async def start_command(message: Message) -> None:
    # Получаем имя пользователя, если Telegram его передал.
    user_name = message.from_user.first_name if message.from_user and message.from_user.first_name else "пользователь"

    # Отправляем красивое приветственное сообщение с подключением reply-клавиатуры.
    await message.answer(
        text=(
            "🌟 Добро пожаловать в учебного Telegram-бота.\n\n"
            f"👤 Ваше имя: {user_name}\n"
            "📋 Ниже открыто главное меню.\n"
            "Нажмите кнопку «Привет» или «Пока»."
        ),
        reply_markup=await get_main_menu_keyboard()
    )


# Регистрируем обработчик текста, равного слову Привет.
@menu_router.message(F.text == "Привет")
# Создаём функцию для ответа на кнопку Привет.
async def hello_button(message: Message) -> None:
    # Получаем имя пользователя безопасным способом.
    user_name = message.from_user.first_name if message.from_user and message.from_user.first_name else "пользователь"

    # Отправляем сообщение в точном соответствии с логикой задания.
    await message.answer(f"Привет, {user_name}!")


# Регистрируем обработчик текста, равного слову Пока.
@menu_router.message(F.text == "Пока")
# Создаём функцию для ответа на кнопку Пока.
async def bye_button(message: Message) -> None:
    # Получаем имя пользователя безопасным способом.
    user_name = message.from_user.first_name if message.from_user and message.from_user.first_name else "пользователь"

    # Отправляем сообщение в точном соответствии с логикой задания.
    await message.answer(f"До свидания, {user_name}!")