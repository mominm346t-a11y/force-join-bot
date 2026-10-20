import telebot
import time
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN, threaded=False)

@bot.message_handler(commands=['start'])
def start(message):
    try:
        bot.send_message(message.chat.id, "Assalamu Alaikum! ✅ Bot Online!")
    except Exception as e:
        print(e)

@bot.message_handler(func=lambda m: True)
def echo(message):
    try:
        bot.send_message(message.chat.id, f"Tumi bolcho: {message.text}")
    except Exception as e:
        print(e)
        time.sleep(2)

print("Bot Started...")
while True:
    try:
        bot.infinity_polling(skip_pending=True, timeout=30)
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(10)
