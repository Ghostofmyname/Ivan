from datetime import datetime

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

Token = "8701270803:AAH19wDRZ86l6VfnD9QjsmRrljima0dAdgs"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привіт! Я простий Telegram бот \n"
        "Напиши \help щоб побачити команди."
    )

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - запуск бота\n"
        "/help - список команд\n"
        "/about - інформація про бота\n"
        "/time - час\n"
        "/date - дата\n"

    )

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
     "Я бот, створений у PyCharm на Python"
    )

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(
            "Я бот, створений у PyCharm на Python"
        )

async def time(update: Update, context: ContextTypes.DEFAULT_TYPE):
    now = datetime.now().strftime("%H:%M:%S")
    await update.message.reply_text(f"Зараз час: {now}")

async def date(update: Update, context: ContextTypes.DEFAULT_TYPE):
        today = datetime.datetime.now().strftime("%d.%m.%Y")
        await update.message.reply_text(f"Сьогодні: {today}")

app = ApplicationBuilder().token(Token).build()

app.add_handler(CommandHandler("time", time))
app.add_handler(CommandHandler("date", date))
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("about", about))

print("Бот запущений...")

app.run_polling()