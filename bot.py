import telegram
import schedule
import time
import os
from datetime import datetime

# Telegram Bot Token (replace with your actual token)
TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")  # Your Telegram user ID or group ID
bot = telegram.Bot(token=TOKEN)

def send_market_report():
    today = datetime.utcnow().strftime('%d %B %Y')
    
    report = f"""
📈 *MauriceFX Daily Market Intel – {today}*
_Asset Focus: Gold (XAU/USD)_

🧠 *Macro Outlook:*
• Fed tone: Hawkish post-CPI  
• Risk sentiment: Bearish  
• Global growth fears linger

💰 *Market Sentiment:*
• VIX: 14.3  
• DXY: 105.70 (USD strength = Bearish Gold)  
• SPX futures: ↓ 0.4%

📊 *Economic Events Today:*
`12:30 GMT`: US GDP  
`14:00 GMT`: Oil Inventories  

📉 *Gold Technicals (M15):*
• Price under POC ($2320)  
• Pullback to $2335 = short zone  
• Key Fib: 0.764 at $2315

🔗 *Correlation:*
• DXY ↑ | Oil ↑ | SPX ↓  
• Gold bias = Bearish

📊 *Quant Stats:*
• ATR: $26  
• IV: 13.2%  
• Range: $2310 – $2340

🏦 *Central Bank Outlook:*
• Sept rate hike odds: 70%  
• Yield curve = Inverted

📥 *Net Positioning:*
• Funds increased longs on Gold  
• Retail mixed positioning

📍 *Bias & Plan:*
*London:* Neutral – Watch $2325  
*NY Open:* Bearish – Reject $2335  
📌 *Invalidate if price holds above $2342*

💡 _"Gold likely to reject $2335 in NY. Watch DXY + volume shift."_
    """
    bot.send_message(chat_id=CHAT_ID, text=report, parse_mode=telegram.ParseMode.MARKDOWN)

# Schedule for once per day
schedule.every().day.at("06:00").do(send_market_report)

while True:
    schedule.run_pending()
    time.sleep(60)
