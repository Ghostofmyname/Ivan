import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

Token = "8701270803:AAH19wDRZ86l6VfnD9QjsmRrljima0dAdgs"

facts = [
    "Кївська Русь була однією із найбільших держав Європи у IX-XIII століттях",
    "Стародавній Єгипет існував понад 300 років.",
    "Римська імперія впала в 476 році.",
    "Перша світова війна почалася у 1914 році.",
    "Українська проголосила незалежність у 1991 році.",

]

ukraine_history = """
   Історія України:
   
   -Київська Русь (IX-XIII ст. )
   -Козацька держава (Гетьманщина)
   -Україна у складі імперій
   -Незалежність у 1991 році
   """

world_history = """
Світова історія:

-Стародавній світ (Єгипет, Рим, Греція)
-Середньовіччя
-Новий час
-Сучасність
"""

async def start (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привіт! Я історичний гід \n\n"
        "Команди\n"
        "/fact - випадковий факт\n"
        "/ukraine - історія України\n"
        "/world - світова історія"
    )

    async def fact(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(random.choice(facts))

        async def ukraine(update: Update, context: ContextTypes.DEFAULT_TYPE):
              await update.message.reply_text(ukraine_history)

        async def world(update: Update, context: ContextTypes.DEFAULT_TYPE):
            await update.message.reply_text(world_history)

        app = ApplicationBuilder().token(TOKEN).build()

        app.add_handler(CommandHandler("start", start))
        app.add_handler(CommandHandler("fact", fact))
        app.add_handler(CommandHandler("ukraine", ukraine))
        app.add_handler(CommandHandler("world", world))

        print("Бот працює...")
        app.run_polling()