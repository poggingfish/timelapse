from timelapse import *
import sys
try:
    canvas = sys.argv[1]
    path = sys.argv[2]
except:
    print("Usage: python3 bot.py <canvas> <path>")
    exit()
print(str(datetime.datetime.now())+": Starting bot")
bot = bot(canvas, path)
print(str(datetime.datetime.now())+": Setting up bot")
bot.setup()
while True:
    bot.download()
    print(str(datetime.datetime.now())+": Downloaded image")
    sleep(20)