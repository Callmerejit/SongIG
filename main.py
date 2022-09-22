import os
import telebot
import json
import urllib.request
import string
import random

API_KEY = os.getenv('API_KEY')     //add your api key here.
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Use /get_song to get a random song.')


@bot.message_handler(commands=['get_song'])
def get_vid(message):
    video = vid()
    bot.reply_to(message, video)

@bot.message_handler(commands=["hi"])
def hi(message): 
    bot.send_photo(message.chat.id, photo = open("lol.jpg",'rb'))


def vid():
    video=open("links.txt").readlines()
    ran_vid = random.choice(video)
    return(ran_vid)

bot.infinity_polling()
