from aiogram import Router, types
from aiogram.filters import CommandStart, Command

from utils.keyboards import main_menu_kb
from utils.messages import WELCOME_TEXT, ABOUT_TEXT, SERVICES_TEXT

router = Router()


@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(WELCOME_TEXT, reply_markup=main_menu_kb())


@router.message(Command("about"))
async def cmd_about(message: types.Message):
    await message.answer(ABOUT_TEXT)


@router.message(Command("services"))
async def cmd_services(message: types.Message):
    await message.answer(SERVICES_TEXT)
