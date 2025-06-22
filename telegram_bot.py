# pip install python-telegram-bot ccxt

import asyncio
import ccxt
from telegram import Bot
from config import TOKEN_KEY, CHAT_ID

# Binance Exchange via ccxt
exchange = ccxt.binance()

# Telegram Bot (ohne AiohttpRequest!)
bot = Bot(token=TOKEN_KEY)


async def send_btc_price():
    while True:
        try:
            ticker = exchange.fetch_ticker('BTC/USDT')
            btc_price = ticker['last']
            message = f"📈 BTC/USDT Preis: {btc_price} USDT"
            await bot.send_message(chat_id=CHAT_ID, text=message)
            print(f"Gesendet: {message}")
        except Exception as e:
            print(f"Fehler: {e}")
        await asyncio.sleep(60)  # Alle 60 Sekunden

if __name__ == '__main__':
    asyncio.run(send_btc_price())
