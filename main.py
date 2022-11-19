import os
import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
import json
import urllib.request
import random
import youtube_dl


API_KEY = os.getenv('API_KEY')     //telegram bot api key here.
bot = telebot.TeleBot(API_KEY)

API_YT = os.getenv('API_YT')    //youtube data api key here.

audio_link = ''
query = ''

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Use /get_song to get a random song.')


def vid():
    video=open("links.txt").readlines()
    ran_vid = random.choice(video)
    return(ran_vid)


@bot.message_handler(commands=['get_song'])
def get_vid(message):
    global audio_link
    video = vid()
    video_info = youtube_dl.YoutubeDL().extract_info(url = video,download=False)
    audio_link = video_info['formats'][0]['url']
    bot.reply_to(message, video)
    key_inline = InlineKeyboardMarkup().add(InlineKeyboardButton(text="Download", url= audio_link))
    bot.send_message(message.chat.id, 'Wait a sec while I generate the audio link for you.', reply_markup= key_inline)


@bot.message_handler(commands=["hi"])
def hi(message): 
    bot.send_message(message.chat.id,'github.com/Subham-Singha/SongIG')


@bot.message_handler(commands=["find"])
def find(message):
    global query
    global audio_link
    query = message.text[6::]
    if(query==''):
        bot.send_message(message.chat.id, 'Use /find <Song Name> to search.')
    else:
        query = query.replace(" ","+")
        data = YT()
        bot.send_message(message.chat.id, "I've found "+(data['snippet']['title']))
        video = "https://www.youtube.com/watch?v=" + (data['id']['videoId'])
        video_info = youtube_dl.YoutubeDL().extract_info(url = video,download=False)
        audio_link = video_info['formats'][0]['url']
        bot.send_message(message.chat.id, video)
        key_inline = InlineKeyboardMarkup().add(InlineKeyboardButton(text="Download", url= audio_link))
        bot.send_message(message.chat.id, 'Wait a sec while I generate the audio link for you.', reply_markup= key_inline)


def YT():
    global query
    urlData = "https://www.googleapis.com/youtube/v3/search?key={}&maxResults=1&part=snippet&type=video&q={}".format(API_YT,query)
    webURL = urllib.request.urlopen(urlData)
    data = webURL.read()
    encoding = webURL.info().get_content_charset('utf-8')
    results = json.loads(data.decode(encoding))

    for data in results['items']:
        return(data)

    
@bot.message_handler(regexp="youtu.be")
@bot.message_handler(regexp="youtube.com")
def link(message):
    global audio_link
    video = message.text
    video_info = youtube_dl.YoutubeDL().extract_info(url = video,download=False)
    audio_link = video_info['formats'][0]['url']
    key_inline = InlineKeyboardMarkup().add(InlineKeyboardButton(text="Download", url= audio_link))
    bot.send_message(message.chat.id, "Here is your audio link.",reply_markup= key_inline)


@bot.message_handler(commands=["creator"])
def creator(message):
    bot.send_message(message.chat.id, "t.me/life_sucks09")    

    
bot.infinity_polling()
