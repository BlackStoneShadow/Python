from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

#async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    return None

app = ApplicationBuilder().token("5769168963:AAE4rDAAtjvmwNRUx3DmwRQDDRhUtuottAo").build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()
