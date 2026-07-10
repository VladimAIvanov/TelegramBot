from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def main_menu_kb() -> InlineKeyboardMarkup:
    """Главное меню: Портфолио / Услуги / Контакты."""
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="💼 Портфолио", callback_data="menu:portfolio"),
    )
    builder.row(
        InlineKeyboardButton(text="🛠 Услуги", callback_data="menu:services"),
    )
    builder.row(
        InlineKeyboardButton(text="✉️ Контакты", callback_data="menu:contacts"),
    )
    return builder.as_markup()


def back_to_menu_kb() -> InlineKeyboardMarkup:
    """Кнопка возврата в главное меню (используется под разделами)."""
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="⬅️ В меню", callback_data="menu:back"),
    )
    return builder.as_markup()
