
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, BotCommand
from aiogram.dispatcher.event.bases import UNHANDLED

TOKEN = "8838820962:AAGjhW-SfPbV1Wun8BtdI_f0ZWq1Hvc7h7k"
ADMIN_ID = 7640442503

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Choynak Piyola do'koniga xush kelibsiz!")


@dp.message(Command("choynak"))
async def choynak(message: Message):
    await message.answer("Choynaklar: chinni, shisha, sopol")


@dp.message(Command("piyola"))
async def piyola(message: Message):
    await message.answer("Piyolalar: chinni, naqshli, shisha")


@dp.message(Command("buyurtma"))
async def buyurtma(message: Message):
    await message.answer("Buyurtma uchun mahsulot nomini yozing")


@dp.message(Command("aloqa"))
async def aloqa(message: Message):
    await message.answer("Savolingizni yozing, admin ko'radi")


@dp.message()
async def adminga_yubor(message: Message):
    await message.copy_to(ADMIN_ID)
    return UNHANDLED


@dp.message(F.text | F.photo | F.video | F.audio | F.contact | F.location)
async def kontent(message: Message):
    await message.answer("Xabaringiz qabul qilindi!")


async def main():
    await bot.set_my_commands(commands=[
        BotCommand(command="start", description="Botni ishga tushirish"),
        BotCommand(command="choynak", description="Choynaklar"),
        BotCommand(command="piyola", description="Piyolalar"),
        BotCommand(command="buyurtma", description="Buyurtma berish"),
        BotCommand(command="aloqa", description="Aloqa"),
    ])
    await dp.start_polling(bot)


asyncio.run(main())