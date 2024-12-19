# from telegram import Update
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
# import openai

# # OpenAI API kalitingiz
# # Telegram Bot API tokeningiz
# TELEGRAM_BOT_TOKEN = "7920896903:AAFoa2z9wLSEdParZBXVDInvlwrEWpprU1o"

# # OpenAI bilan muloqot funksiyasi
# def chat_with_gpt(prompt):
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",  # Yoki kerakli modelni tanlang
#         messages=[{"role": "user", "content": prompt}]
#     )
#     return response['choices'][0]['message']['content']

# # /start buyrug'i uchun funksiya
# def start(update: Update, context: CallbackContext):
#     update.message.reply_text("Salom! Men ChatGPT botman. Menga savollaringizni yuboring.")

# # Xabarlarni qayta ishlash
# def handle_message(update: Update, context: CallbackContext):
#     user_message = update.message.text
#     bot_response = chat_with_gpt(user_message)
#     update.message.reply_text(bot_response)

# # Asosiy funksiya
# def main():
#     updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
#     dp = updater.dispatcher

#     dp.add_handler(CommandHandler("start", start))
#     dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

#     updater.start_polling()
#     updater.idle()

# if __name__ == "__main__":
#     main()


from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import openai

# OpenAI API kalitingiz

# Telegram Bot API tokeningiz
TELEGRAM_BOT_TOKEN = "7920896903:AAFoa2z9wLSEdParZBXVDInvlwrEWpprU1o"

# OpenAI bilan muloqot funksiyasi
async def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Yoki kerakli modelni tanlang
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

# /start buyrug'i uchun funksiya
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! Men ChatGPT botman. Menga savollaringizni yuboring.")

# Xabarlarni qayta ishlash
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    bot_response = await chat_with_gpt(user_message)
    await update.message.reply_text(bot_response)

# Asosiy funksiya
def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot ishga tushdi!")
    app.run_polling()

if __name__ == "__main__":
    main()
