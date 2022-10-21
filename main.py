import os
import telebot
import json
import urllib.request
import string
import random

API_KEY = os.getenv('API_KEY')     //telegram bot api key here.
bot = telebot.TeleBot(API_KEY)

API_YT = os.getenv('API_YT')    //youtube data api key here.

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


query = ''
@bot.message_handler(commands=["find"])
def find(message):
    global query
    query = message.text[6::]
    if(query==''):
        bot.send_message(message.chat.id, 'Please enter a song name.')
    else:
        query = query.replace(" ","+")
        data = YT()
        bot.send_message(message.chat.id, "I've found "+(data['snippet']['title']))
        video = "https://www.youtube.com/watch?v=" + (data['id']['videoId'])
        bot.send_message(message.chat.id, video)


def YT():
    global query
    urlData = "https://www.googleapis.com/youtube/v3/search?key={}&maxResults=1&part=snippet&type=video&q={}".format(API_YT,query)
    webURL = urllib.request.urlopen(urlData)
    data = webURL.read()
    encoding = webURL.info().get_content_charset('utf-8')
    results = json.loads(data.decode(encoding))

    for data in results['items']:
        return(data)

    
bot.infinity_polling()
