import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import os

# ទាញយក Token ពី Environment Variables របស់ Railway
BOT_TOKEN = os.environ.get('BOT_TOKEN', 'YOUR_BOT_TOKEN_HERE')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # សារស្វាគមន៍ទី១
    welcome_text = "Hello! Welcome to Toad Store 24/7
Please select a service below"
    bot.send_message(message.chat.id, welcome_text)
    
    # សារទី២ សម្រាប់ជ្រើសរើសភាសា (Inline Keyboard)
    markup_lang = InlineKeyboardMarkup(row_width=2)
    btn_kh = InlineKeyboardButton("🇰🇭 ខ្មែរ", callback_data="lang_kh")
    btn_en = InlineKeyboardButton("🇬🇧 English", callback_data="lang_en")
    markup_lang.add(btn_kh, btn_en)
    
    bot.send_message(message.chat.id, "សូមជ្រើសរើសភាសា / Please choose your language:", reply_markup=markup_lang)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "lang_kh":
        bot.send_message(call.message.chat.id, "អ្នកបានជ្រើសរើសភាសាខ្មែរ។")
        show_main_menu(call.message.chat.id)
    elif call.data == "lang_en":
        bot.send_message(call.message.chat.id, "You have selected English.")
        show_main_menu(call.message.chat.id)

def show_main_menu(chat_id):
    # បង្កើត Menu ខាងក្រោម (Reply Keyboard)
    markup_menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = KeyboardButton("🥷 គណនី")
    btn2 = KeyboardButton("🛍 ហាង")
    btn3 = KeyboardButton("💸 ដាក់ប្រាក់")
    btn4 = KeyboardButton("💬 Admin")
    btn5 = KeyboardButton("📚 របៀបប្រើប្រាស់")
    btn6 = KeyboardButton("🕒 ប្រវត្តិទិញ")
    
    markup_menu.add(btn1, btn2, btn3, btn4, btn5, btn6)
    bot.send_message(chat_id, "សូមជ្រើសរើសសេវាកម្មក្នុង Menu៖", reply_markup=markup_menu)

if __name__ == "__main__":
    print("Bot កំពុងដំណើរការ...")
    bot.infinity_polling()
