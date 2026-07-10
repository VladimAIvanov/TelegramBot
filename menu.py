from aiogram import Router, types
from aiogram.filters import Command

from utils.keyboards import back_to_menu_kb, main_menu_kb
from utils.messages import CONTACTS_TEXT, PORTFOLIO_TEXT, SERVICES_TEXT, WELCOME_TEXT

router = Router()


@router.message(Command("menu"))
async def cmd_menu(message: types.Message):
    await message.answer("Выберите раздел:", reply_markup=main_menu_kb())


@router.callback_query(lambda c: c.data == "menu:portfolio")
async def show_portfolio(callback: types.CallbackQuery):
    await callback.message.edit_text(PORTFOLIO_TEXT, reply_markup=back_to_menu_kb())
    await callback.answer()


@router.callback_query(lambda c: c.data == "menu:services")
async def show_services(callback: types.CallbackQuery):
    await callback.message.edit_text(SERVICES_TEXT, reply_markup=back_to_menu_kb())
    await callback.answer()


@router.callback_query(lambda c: c.data == "menu:contacts")
async def show_contacts(callback: types.CallbackQuery):
    await callback.message.edit_text(CONTACTS_TEXT, reply_markup=back_to_menu_kb())
    await callback.answer()


@router.callback_query(lambda c: c.data == "menu:back")
async def back_to_menu(callback: types.CallbackQuery):
    await callback.message.edit_text("Выберите раздел:", reply_markup=main_menu_kb())
    await callback.answer()
