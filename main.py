import random
import json
from mcstatus import JavaServer
from javascript import require, On
import os
import colorama
import time

colorama.init()

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

mineflayer = require('mineflayer')
symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
with open('servers.txt') as f:
    servers = f.readlines()
with open('settings.json') as f:
    settings = json.load(f)

def ping(ip):
    try:
        JavaServer.lookup(ip,timeout=1).ping()
        return True
    except:
        return False

def joinjs(ip: str, nickname: str):
    ipz = ip.replace("\n", "")
    if ping(ip):
        if ip.__contains__(':'):
            bot = mineflayer.createBot({
                'host': ip.split(':')[0],
                'port': ip.split(':')[1],
                'username': nickname,
                'version': False
            })

            @On(bot, 'spawn')
            def jointoserver(*args):
                print(colorama.Fore.LIGHTBLUE_EX + '[' + time.strftime("%H:%M:%S")+']' + f' {nickname} joined to {ipz}')
                bot.end()
        else:
            bot = mineflayer.createBot({
                'host': ip,
                'port': 25565,
                'username': nickname,
                'version': False
            })

            @On(bot, 'spawn')
            def jointoserver(*args):
                print(colorama.Fore.LIGHTBLUE_EX + '[' + time.strftime("%H:%M:%S")+']' + f' {nickname} joined to {ipz}')
                bot.end()
    else:
        print(colorama.Fore.LIGHTRED_EX + '[' + time.strftime("%H:%M:%S")+']' + f' {ipz} is not on')


def spamjs(ip: str, nickname: str):
    ipz = ip.replace("\n", "")
    if ping(ip):
        with open('message.txt') as f:
            message = f.read()
        if ip.__contains__(':'):
            bot = mineflayer.createBot({
                'host': ip.split(':')[0],
                'port': ip.split(':')[1],
                'username': nickname,
                'version': False
            })

            @On(bot, 'spawn')
            def spam(*args):
                print(colorama.Fore.LIGHTBLUE_EX + '[' + time.strftime("%H:%M:%S")+']' + f' {nickname} joined to {ipz}')
                for i in range(settings['message_per_bot']):
                    bot.chat(message)
                    print(colorama.Fore.LIGHTCYAN_EX + '[' + time.strftime("%H:%M:%S") + ']' + f' {nickname} sent message on {ipz}')
                time.sleep(0.3)
                bot.end()
                print(colorama.Fore.LIGHTBLUE_EX + '[' + time.strftime("%H:%M:%S") + ']' + f' {nickname} disconnected from {ipz}')

        else:
            bot = mineflayer.createBot({
                'host': ip,
                'port': 25565,
                'username': nickname,
                'version': False
            })

            @On(bot, 'spawn')
            def spam(*args):
                print(colorama.Fore.LIGHTBLUE_EX + '[' + time.strftime("%H:%M:%S")+']' + f' {nickname} joined to {ipz}')
                for i in range(settings['message_per_bot']):
                    bot.chat(message)
                    print(colorama.Fore.LIGHTCYAN_EX + '[' + time.strftime("%H:%M:%S") + ']' + f' {nickname} sent message on {ipz}')
                time.sleep(0.3)
                bot.end()
                print(colorama.Fore.LIGHTCYAN_EX + '[' + time.strftime("%H:%M:%S") + ']' + f' {nickname} disconnected from {ipz}')
    else:
        print(colorama.Fore.LIGHTRED_EX + '[' + time.strftime("%H:%M:%S")+']' + f' {ipz} is not on')

def main():
    print(colorama.Fore.LIGHTBLUE_EX + '[1] Spam with message on many servers\n[2] Spam with message on 1 server\n[3] Spam with join/left message on 1 server')
    choice = int(input())
    if choice == 1:
        cls()

        with open('message.txt') as f:
            if settings['bots'] == 1:
                nickname = settings['bots']
                print(colorama.Fore.LIGHTBLUE_EX + '[' + time.strftime("%H:%M:%S") + ']' + f' Your nickname : {nickname}')
                print(colorama.Fore.LIGHTBLUE_EX + '[' + time.strftime("%H:%M:%S")+']' + ' Started spamming...')
                for server in servers:
                    spamjs(server, nickname)
            else:
                for server in servers:
                    print(colorama.Fore.LIGHTBLUE_EX + '[' + time.strftime("%H:%M:%S") + ']' + ' Started spamming...')
                    nickname = ''
                    for i in range(7): nickname += random.choice(symbols)
                    spamjs(server,nickname)
    elif choice == 2:
        if settings['bots'] == 1:
            nickname = settings['bots']
            print(colorama.Fore.LIGHTBLUE_EX + '[' + time.strftime("%H:%M:%S") + ']' + f' Your nickname : {nickname}')
            print(colorama.Fore.LIGHTBLUE_EX + '[' + time.strftime("%H:%M:%S") + ']' + ' Started spamming...')
            for server in servers:
                for i in range(999):
                    spamjs(server,nickname)
        else:
            print(colorama.Fore.LIGHTBLUE_EX + '[' + time.strftime("%H:%M:%S") + ']' + ' Started spamming...')
            for server in servers:
                for i in range(999):
                    nickname = ''
                    for z in range(7): nickname += random.choice(symbols)
                    spamjs(server,nickname)
                    time.sleep(0.3)

    elif choice == 3:
        cls()
        print(colorama.Fore.LIGHTBLUE_EX + '[' + time.strftime("%H:%M:%S") + ']' + ' Started joining...')
        for server in servers:
            for i in range(3):
                for i in range(settings['bots']):
                    nickname = ''
                    for f in range(10): nickname += random.choice(symbols)
                    joinjs(server,nickname)
    else:
        cls()
        print(colorama.Fore.RED + '[' + time.strftime("%H:%M:%S") + ']' + ' Input correct number!')
        time.sleep(2)
        cls()
        main()



if __name__ == "__main__":
    main()
