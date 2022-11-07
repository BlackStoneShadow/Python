from controller import Controller
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'input command /menu')

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(cnt.menu_view())

async def eval(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if len(context.args) == 3:        
        await update.message.reply_text(cnt.menu_eval(context.args[0], context.args[2], context.args[1]))
    else:
        await update.message.reply_text('method expects 3 arguments: x (+|-|*|/) y')

cnt = Controller()
app = ApplicationBuilder().token("5728522493:AAEmpIKuOU9_iZm-w_b7WVwQ64obtDxynDc").build()

app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("menu", menu))
app.add_handler(CommandHandler("eval", eval))

app.run_polling()