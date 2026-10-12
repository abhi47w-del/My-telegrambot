from telegram.ext import Application, CommandHandler.async def start(update, context): await update.message.reply_text("হ্যালো! আমি আপনার বট.")def main(): application = Application.builder().token("8993265664:AAH5aFAd3EkTMiVcHm4V6Sj7gom6eed2y7E").build()application.add_handler(CommandHandler("start", start))application.run_polling()
if __name__ == "__main__" main()
