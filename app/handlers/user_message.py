from aiogram import F, Router, Bot
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, ChatJoinRequest
from aiogram.fsm.context import FSMContext

import app.keyboards.reply as rkb
import app.keyboards.builder as bkb
import app.keyboards.inline as ikb

from app.filters.admin_filter import AdminProtect

from app.database import insert_user
from config import CHANNEL_ID

user = Router()


@user.message(CommandStart())
async def start_command(message: Message):
    admin = AdminProtect()
    if not await admin(message):  # Добавляем await здесь
        await insert_user(message.from_user.id, message.from_user.username)
    else:
        await insert_user(message.from_user.id, message.from_user.username)
        await message.answer(f"Вы успешно авторизовались как администратор!",
                             reply_markup=rkb.admin_menu)


@user.chat_join_request()
async def handle_chat_join_request(join_request: ChatJoinRequest, bot: Bot):
    if join_request.chat.id == CHANNEL_ID:
        await insert_user(join_request.from_user.id, join_request.from_user.username)
        await join_request.approve()
        await bot.send_message(join_request.from_user.id, "Заявка принята!")

