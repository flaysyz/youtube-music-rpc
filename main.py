import sys
import os

os.system('pip install ytmusicapi')
os.system('pip install pypresence')

import time
from ytmusicapi import YTMusic
from pypresence import Presence

print('Авторизуйся через google аккаунт и нажми Enter')
time.sleep(3)
os.system('ytmusicapi oauth')
ytmusic = YTMusic("oauth.json")
discord_rpc = Presence('1150430824693497990')
discord_rpc.connect()
left = 0
n_title = ''


def update_discord_rpc():
    global n_title
    global left
    lm = ''
    ls = ''
    art = ''
    zero = ''
    his = ytmusic.get_history()
    dur = his[1]
    title = dur.setdefault('title')
    if n_title != title:
        left = dur.setdefault('duration_seconds')
        n_title = title
    else:
        if left == 0:
            lm = '0'
            ls = '0'
        else:
            left -= 1
            lm = str(left // 60)
            ls = str(left % 60)
    if len(ls) == 1:
        zero += '0'
    ico = dur.setdefault('thumbnails')
    if len(ico) < 2:
        rico = ico[0].setdefault('url')
    else:
        rico = ico[1].setdefault('url')

    artist = dur.setdefault('artists')
    for i in range(len(artist)):
        arti = artist[i].setdefault('name')
        if i == len(artist) - 1:
            art += str(arti)
        else:
            art += f'{arti}, '

    discord_rpc.update(
        details=f'{art} - {title}',
        state=f'Осталось {lm}:{zero}{ls}',
        large_image=rico,
    )


while True:
    update_discord_rpc()
    time.sleep(1)
