import telebot
from time import sleep
from telebot import types
from wa_check import check_number
from keep_alive import keep_alive

bot = telebot.TeleBot("7190742210:AAG55Orf8PAQ0uh2Amx4CQcjCIsDBhjJOPY")

@bot.message_handler(commands=['start'])
def welcome_message(message):
  chat_id = message.chat.id
  username = message.from_user.username
  group_id = "-4268811340"
  bot.send_chat_action(chat_id, 'typing')
  sleep(1)
  markup = types.ForceReply(selective=False)
  bot.send_message(chat_id, 'Send me a number with country code\n(*ex=628xxxxx*)', parse_mode='Markdown', reply_markup=markup)
  bot.send_message(group_id, f'*@{username}* starting bot...', parse_mode='Markdown')
  
@bot.message_handler(func=lambda message: True)
def receive_number(message):
  if message.text.isdigit():
    if check_number(message.text) is True:
      bot.send_chat_action(message.chat.id, 'typing')
      sleep(1)
      bot.reply_to(message, 'This number is *on* WhatsApp', parse_mode='Markdown')
    else:
      bot.send_chat_action(message.chat.id, 'typing')
      sleep(1)
      bot.reply_to(message, 'This number is *not available* in WhatsApp', parse_mode='Markdown')
  else:
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)
    bot.reply_to(message, 'Please send me a number not alphabet!')
    
if __name__=='__main__':
  keep_alive()
  print('starting bot...')
  bot.infinity_polling()
