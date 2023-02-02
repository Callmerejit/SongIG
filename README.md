# SongIG

It is telegram bot to get random song or searched song of your choice. It is a small project made by @life_sucks09 on telegram.

# Files breakdown

main.py contains the basic code.

.env contains your telegram api key.    //not to shared publicly.

links.txt contains video link.     //will add more.

# Packages used

1. **os**                                                     // used to import the API_KEY from .env file.
2. [**telebot**](https://pypi.org/project/pyTelegramBotAPI/)                                                // used to create the bot.
3. **InlineKeyboardButton, InlineKeyboardMarkup**             // used to add an inline keyboard(import from telebot.types).
4. **json**                                                   // used to load the html page as an python dictionary.
5. **urllib.request**                                         // used to request a wed search on youtube.
6. **random**                                                 // used to get a random link.
7. [**youtube_dl**](https://pypi.org/project/youtube_dl/)                                             // used to get the audio file link from searched video.
