 import telebot
from telebot import types

BOT_TOKEN = "8754794998:AAFc3psbdmoBbL-tNT-4VOwKvxKlUT-BBQY"
CHANNEL_USERNAME = "@MIM9614" @MIM9614

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(content_types=['new_chat_members'])
def welcome(message):
    bot.send_message(message.chat.id, f"Welcome! Please join {CHANNEL_USERNAME} first ❤️")

@bot.message_handler(func=lambda m: True)
def check_join(message):
    try:
        user_id = message.from_user.id
        # চেক করছে ইউজার চ্যানেলে জয়েন করেছে কিনা
        chat_member = bot.get_chat_member(CHANNEL_USERNAME, user_id)
        if chat_member.status in ['left', 'kicked']:
            # জয়েন করে নাই, তাই মেসেজ ডিলিট + ওয়ার্নিং
            try:
                bot.delete_message(message.chat.id, message.message_id)
            except:
                pass
            
            markup = types.InlineKeyboardMarkup()
            btn = types.InlineKeyboardButton(text="Join Channel", url=f"https://t.me/{CHANNEL_USERNAME.replace('@','')}")
            markup.add(btn)
            
            bot.send_message(message.chat.id, f"⚠️ @{message.from_user.username or message.from_user.first_name} , মেসেজ করার আগে {CHANNEL_USERNAME} চ্যানেলে জয়েন করতে হবে!", reply_markup=markup)
        # যদি জয়েন করে থাকে, তাহলে কিছু করবে না, মেসেজ থাকবে
    except Exception as e:
        print(e)

print("Bot Started...")
bot.infinity_polling()
