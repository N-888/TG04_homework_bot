# Импортируем класс Router, чтобы создать отдельный роутер для команды /links.
from aiogram import Router

# Импортируем фильтр Command, чтобы ловить команду /links.
from aiogram.filters import Command

# Импортируем тип Message, чтобы обрабатывать обычные сообщения.
from aiogram.types import Message

# Импортируем функцию создания inline-клавиатуры со ссылками.
from keyboards.user_keyboards import get_links_keyboard


# Создаём роутер для раздела со ссылками.
links_router = Router()


# Регистрируем обработчик команды /links.
@links_router.message(Command("links"))
# Создаём асинхронную функцию, которая отправит пользователю inline-кнопки со ссылками.
async def links_command(message: Message) -> None:
    # Отправляем пользователю заголовок раздела и подключаем inline-клавиатуру.
    await message.answer(
        text=(
            "🔗 Раздел ссылок\n\n"
            "Выберите нужную кнопку ниже:\n"
            "📰 Новости\n"
            "🎵 Музыка\n"
            "🎬 Видео"
        ),
        reply_markup=await get_links_keyboard()
    )