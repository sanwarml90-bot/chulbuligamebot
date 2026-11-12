"""Generic Telegram bot built by Sanji AI."""
import os
from pyrogram import Client, filters

API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]
BOT_TOKEN = os.environ["BOT_TOKEN"]

app = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply_text(
        "Namaste! Main aapka bot hun. /help bhejo, main kya kar sakta hun ye dekhne ke liye."
    )


@app.on_message(filters.command("help") & filters.private)
async def help_cmd(client, message):
    await message.reply_text(
        "/start - bot shuru karo\n/help - ye madad"
    )


@app.on_message(filters.private & filters.text & ~filters.command(["start", "help"]))
async def echo(client, message):
    await message.reply_text(f"Aapne kaha: {message.text}")


app.run()
