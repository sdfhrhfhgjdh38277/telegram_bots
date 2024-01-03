import telebot as t
import requests

bot_token = t.Telebot("6311441375:AAEDNHdgbHUnqBVKPVenZdFIGcW-GEIgwJI")

@message_handler(commands=["start"])
def start_command(message):
  bot_token.reply_to(message.chat_id, "Привет! Я помогу тебе узнать погоду, просто напишии команду /weather и название нужного места!")
