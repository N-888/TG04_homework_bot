# Импортируем класс Router, чтобы создать отдельный роутер для динамической клавиатуры.
from aiogram import Router

# Импортируем объект F, чтобы фильтровать callback_data у inline-кнопок.
from aiogram import F

# Импортируем фильтр Command, чтобы ловить команду /dynamic.
from aiogram.filters import Command

# Импортируем тип Message, чтобы работать с обычными сообщениями.
from aiogram.types import Message

# Импортируем тип CallbackQuery, чтобы работать с нажатиями на inline-кнопки.
from aiogram.types import CallbackQuery

# Импортируем функцию создания стартовой inline-клавиатуры.
from keyboards.user_keyboards import get_dynamic_start_keyboard

# Импортируем функцию создания второй inline-клавиатуры с двумя опциями.
from keyboards.user_keyboards import get_dynamic_options_keyboard


# Создаём роутер для динамической клавиатуры.
dynamic_router = Router()


# Регистрируем обработчик команды /dynamic.
@dynamic_router.message(Command("dynamic"))
# Создаём функцию, которая покажет стартовую кнопку Показать больше.
async def dynamic_command(message: Message) -> None:
    # Отправляем пользователю описание раздела и стартовую inline-кнопку.
    await message.answer(
        text=(
            "⚙️ Динамическое меню\n\n"
            "Сейчас под сообщением находится стартовая кнопка.\n"
            "Нажмите «Показать больше», чтобы заменить её на новые варианты."
        ),
        reply_markup=await get_dynamic_start_keyboard()
    )


# Регистрируем обработчик callback_data со значением show_more.
@dynamic_router.callback_query(F.data == "show_more")
# Создаём функцию, которая заменит одну кнопку на две новые.
async def show_more_callback(callback: CallbackQuery) -> None:
    # Сообщаем Telegram, что нажатие обработано, чтобы кнопка не "висела" в состоянии загрузки.
    await callback.answer(text="Открываю дополнительные варианты")

    # Проверяем, что у callback действительно есть исходное сообщение, которое можно изменить.
    if callback.message:
        # Изменяем текст исходного сообщения и подставляем новую клавиатуру с двумя кнопками.
        await callback.message.edit_text(
            text=(
                "✨ Дополнительное меню открыто\n\n"
                "Теперь выберите одну из кнопок ниже:"
            ),
            reply_markup=await get_dynamic_options_keyboard()
        )


# Регистрируем обработчик callback_data со значением option_1.
@dynamic_router.callback_query(F.data == "option_1")
# Создаём функцию обработки кнопки Опция 1.
async def option_1_callback(callback: CallbackQuery) -> None:
    # Подтверждаем нажатие, чтобы Telegram понимал, что действие выполнено.
    await callback.answer(text="Выбрана Опция 1")

    # Проверяем, что исходное сообщение существует.
    if callback.message:
        # Отправляем отдельное сообщение с текстом выбранной опции.
        await callback.message.answer("Вы выбрали: Опция 1")


# Регистрируем обработчик callback_data со значением option_2.
@dynamic_router.callback_query(F.data == "option_2")
# Создаём функцию обработки кнопки Опция 2.
async def option_2_callback(callback: CallbackQuery) -> None:
    # Подтверждаем нажатие, чтобы Telegram понимал, что действие выполнено.
    await callback.answer(text="Выбрана Опция 2")

    # Проверяем, что исходное сообщение существует.
    if callback.message:
        # Отправляем отдельное сообщение с текстом выбранной опции.
        await callback.message.answer("Вы выбрали: Опция 2")