from controller import Controller
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

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

async def start(bot, update):
  await bot.message.reply_text(main_menu_message(),
                         reply_markup=main_menu_keyboard())

def main_menu(bot, update):
  bot.callback_query.message.edit_text(main_menu_message(),
                          reply_markup=main_menu_keyboard())

def main_menu_message():
  return 'Choose the option in main menu:'

def main_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Print Log', callback_data='pl')],
              [InlineKeyboardButton('Clear Log', callback_data='cl')]]
  return InlineKeyboardMarkup(keyboard)

async def menu_log_print(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:    
    await update.callback_query.edit_message_text(cnt.menu_plog())

async def menu_log_clear(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:    
    await update.callback_query.edit_message_text(cnt.menu_clog())

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

app.add_handler(CommandHandler('start', start))
app.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
app.add_handler(CallbackQueryHandler(menu_log_print, pattern='pl'))
app.add_handler(CallbackQueryHandler(menu_log_clear, pattern='сl'))

app.run_polling()