 import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes

# Render Environment থেকে Token নিবে
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_USERNAME = os.getenv("CHANNEL", "@MIM9614")
CHANNEL_LINK = f"https://t.me/{CHANNEL_USERNAME.replace('@','')}"

async def check_join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat.type not in ["group", "supergroup"]:
        return
    try:
        user_id = update.message.from_user.id
        member = await context.bot.get_chat_member(CHANNEL_USERNAME, user_id)
        if member.status in ['left', 'kicked', 'restricted']:
            raise Exception("Not Joined")
    except:
        try:
            await update.message.delete()
        except:
            pass
        keyboard = [[InlineKeyboardButton("✅ Join Channel", url=CHANNEL_LINK)]]
        await update.message.reply_text(
            f"⚠️ {update.message.from_user.first_name}, গ্রুপে কথা বলতে হলে আগে আমাদের চ্যানেল জয়েন করতে হবে!",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Bot চালু আছে! Channel: {CHANNEL_USERNAME}")

def main():
    if not BOT_TOKEN:
        print("ERROR: BOT_TOKEN not set in Environment Variables!")
        return
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_join))
    print("Bot Started...")
    app.run_polling()

if __name__ == "__main__":
    main()
