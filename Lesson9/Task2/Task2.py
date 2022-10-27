from Controller import Controller
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'input command /menu')

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(cnt.menu_view())

async def all(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(cnt.menu_all())

async def find(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if len(context.args) == 1:        
        await update.message.reply_text(cnt.menu_find(context.args[0]))
    else:
        await update.message.reply_text('method expects 1 arguments!')

async def new(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if len(context.args) == 3:        
        await update.message.reply_text(cnt.menu_add(context.args[0], context.args[1], context.args[2]))
    else:
        await update.message.reply_text('method expects 3 arguments!')

async def remove(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if len(context.args) == 1:        
        await update.message.reply_text(cnt.menu_remove(context.arg[0]))
    else:
        await update.message.reply_text('method expects 1 arguments!')

async def save(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(cnt.menu_save())

cnt = Controller()
app = ApplicationBuilder().token("5769168963:AAE4rDAAtjvmwNRUx3DmwRQDDRhUtuottAo").build()

app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("menu", menu))
app.add_handler(CommandHandler("all", all))
app.add_handler(CommandHandler("find", find))
app.add_handler(CommandHandler("new", new))
app.add_handler(CommandHandler("remove", remove))
app.add_handler(CommandHandler("save", save))

app.run_polling()