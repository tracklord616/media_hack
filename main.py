import sys
import time
import telepot
import os
import random
import datetime
from telepot.loop import MessageLoop
arr = [0]
ids = []


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    k = open('ids.txt', 'a')
    if str(chat_id) not in open('ids.txt').read():
        k.write(str(chat_id))
        k.write('\n')
    k.close()
    global i
    if content_type == 'text' and msg['text'] != '/start':
        f = open('link.txt', 'w')
        f.write(msg['text'])
        f.close()
        # bot.sendMessage(chat_id, "link is goin' to ML script")
        # bot.sendMessage(chat_id, "ML script is workin' ")
        # bot.sendMessage(chat_id, "...")
        res = random.randrange(0, 2)
        if res == 1:
            bot.sendPhoto(chat_id, open('like.jpg', 'rb'))
        elif res == 0:
            bot.sendPhoto(chat_id, open('unlike.jpg', 'rb'))


def sts(id):
    bot.sendMessage(id, "hello")


TOKEN = '805328174:AAFSqdi-I20SNxQPI504D_F7WHAgfdJGJ6g'
bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print('Listening ...')

# Keep the program running.
while 1:
    retell()
    time.sleep(10)
