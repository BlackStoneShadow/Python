from controller import Controller
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'input command /menu')

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(cnt.menu_view())

async def eval(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    cnt.set_user(update.message.from_user.full_name)
    await update.message.reply_text(cnt.menu_eval(str().join(context.args)))        

async def plog(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(cnt.menu_plog())

async def clog(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(cnt.menu_clog())

cnt = Controller()
#print(cnt.menu_eval('1.1+20'))
#print(cnt.menu_eval('1+1i+2+2i'))
#print(cnt.menu_plog())
app = ApplicationBuilder().token("5728522493:AAEmpIKuOU9_iZm-w_b7WVwQ64obtDxynDc").build()

app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("menu", menu))
app.add_handler(CommandHandler("eval", eval))
app.add_handler(CommandHandler("plog", plog))
app.add_handler(CommandHandler("clog", clog))

app.run_polling()