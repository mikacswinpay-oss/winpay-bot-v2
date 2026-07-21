import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

import os

print("BOT_TOKEN =", BOT_TOKEN)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("💰 Deposit", callback_data="deposit")],
        [InlineKeyboardButton("🎁 Bonus", callback_data="bonus")],
        [InlineKeyboardButton("👑 Premium", callback_data="premium")],
        [InlineKeyboardButton("🎧 Customer Support", callback_data="support")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 Welcome to WinPay Bot\n\nPlease choose an option:",
        reply_markup=reply_markup,
    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "deposit":
        text = (
            "💰 Deposit\n\n"
            "UPI ID: mikacswinpay@oksbi\n\n"
            "Payment karne ke baad screenshot Support ko bhej dein."
        )

    elif query.data == "bonus":
        text = (
            "🎁 Bonus\n\n"
            "First Deposit Bonus Available.\n"
            "Support se contact karein."
        )

    elif query.data == "premium":
        text = (
            "👑 Premium\n\n"
            "Premium Membership ke liye Support se baat karein."
        )

    elif query.data == "support":
        text = (
            "🎧 Customer Support\n\n"
            "Telegram: @miss_MikaCS"
        )

    await query.edit_message_text(text)

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    print(f"Error: {context.error}")


def main():
    if not BOT_TOKEN:
        raise ValueError(
            "BOT_TOKEN environment variable not found!"
        )

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.add_error_handler(error_handler)

    print("✅ Bot is running...")
    app.run_polling(
        allowed_updates=Update.ALL_TYPES,
        drop_pending_updates=True,
    )


if __name__ == "__main__":
    main()