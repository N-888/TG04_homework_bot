# Импортируем класс KeyboardButton для обычных reply-кнопок.
from aiogram.types import KeyboardButton

# Импортируем класс InlineKeyboardButton для inline-кнопок под сообщением.
from aiogram.types import InlineKeyboardButton

# Импортируем ReplyKeyboardBuilder для удобной сборки обычной клавиатуры.
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Импортируем InlineKeyboardBuilder для удобной сборки inline-клавиатуры.
from aiogram.utils.keyboard import InlineKeyboardBuilder


# Создаём асинхронную функцию для главного reply-меню.
async def get_main_menu_keyboard():
    # Создаём builder для обычной клавиатуры.
    keyboard = ReplyKeyboardBuilder()

    # Добавляем кнопку Привет в builder.
    keyboard.add(KeyboardButton(text="Привет"))

    # Добавляем кнопку Пока в builder.
    keyboard.add(KeyboardButton(text="Пока"))

    # Возвращаем готовую клавиатуру в один ряд из двух кнопок с уменьшенным размером.
    return keyboard.adjust(2).as_markup(resize_keyboard=True)


# Создаём асинхронную функцию для inline-клавиатуры со ссылками.
async def get_links_keyboard():
    # Создаём builder для inline-клавиатуры.
    keyboard = InlineKeyboardBuilder()

    # Добавляем кнопку Новости со ссылкой на новостной сайт.
    keyboard.add(InlineKeyboardButton(text="📰 Новости", url="https://ria.ru/"))

    # Добавляем кнопку Музыка со ссылкой на музыкальный сервис.
    keyboard.add(InlineKeyboardButton(text="🎵 Музыка", url="https://music.yandex.ru/"))

    # Добавляем кнопку Видео со ссылкой на видеохостинг.
    keyboard.add(InlineKeyboardButton(text="🎬 Видео", url="https://www.youtube.com/"))

    # Возвращаем клавиатуру, где каждая кнопка находится на своей строке.
    return keyboard.adjust(1).as_markup()


# Создаём асинхронную функцию для первой динамической клавиатуры.
async def get_dynamic_start_keyboard():
    # Создаём builder для inline-клавиатуры.
    keyboard = InlineKeyboardBuilder()

    # Добавляем стартовую кнопку Показать больше с callback_data для дальнейшей обработки.
    keyboard.add(InlineKeyboardButton(text="Показать больше", callback_data="show_more"))

    # Возвращаем готовую клавиатуру с одной кнопкой в одной строке.
    return keyboard.adjust(1).as_markup()


# Создаём асинхронную функцию для второй динамической клавиатуры.
async def get_dynamic_options_keyboard():
    # Создаём builder для inline-клавиатуры.
    keyboard = InlineKeyboardBuilder()

    # Добавляем кнопку Опция 1 с callback_data option_1.
    keyboard.add(InlineKeyboardButton(text="Опция 1", callback_data="option_1"))

    # Добавляем кнопку Опция 2 с callback_data option_2.
    keyboard.add(InlineKeyboardButton(text="Опция 2", callback_data="option_2"))

    # Возвращаем клавиатуру, в которой две кнопки стоят в одном ряду.
    return keyboard.adjust(2).as_markup()