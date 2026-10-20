import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

BOT_TOKEN = 8615086366:AAGsvVKXAKwdFHm7Fp2d_pMQxTAdMWHTKTw
CHANNEL_USERNAME = "@MIM9614"
REQUIRED_MESSAGES = 10

# user_id : count
user_data = {}

logging.basicConfig(level=logging.INFO)

async def check_join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.effective_user:
        return
    
    user_id = update.effective_user.id
    chat_id = update.effective_chat.id

    # চ্যানেলে জয়েন আছে কিনা চেক
    try:
        member = await context.bot.get_chat_member(CHANNEL_USERNAME, user_id)
        if member.status in ['member', 'administrator', 'creator']:
            # জয়েন আছে, কাউন্ট বাড়াও
            count = user_data.get(user_id, 0) + 1
            user_data[user_id] = count
            if count >= REQUIRED_MESSAGES:
                await update.message.reply_text(f"✅ ধন্যবাদ! {REQUIRED_MESSAGES} টি মেসেজ সম্পন্ন।")
            return
    except:
        pass

    # জয়েন নাই -> মেসেজ ডিলিট + ওয়ার্নিং
    try:
        await update.message.delete()
    except:
        pass

    count = user_data.get(user_id, 0)
    
    keyboard = [[InlineKeyboardButton("📢 চ্যানেলে জয়েন করুন", url=f"https://t.me/{CHANNEL_USERNAME.replace('@','')}")]]
    
    await context.bot.send_message(
        chat_id=chat_id,
        text=f"⚠️ মেসেজ করার আগে আপনাকে আমাদের চ্যানেলে জয়েন করতে হবে ({count}/{REQUIRED_MESSAGES})\n\nজয়েন করে আবার চেষ্টা করুন।",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_join))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
