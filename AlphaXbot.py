# This a part of https://t.me/AlphaXProject
# AlphaXbot_v0.0.3

import time
import asyncio
import sys
import random
import threading

from telethon import TelegramClient, events, utils
from Config import STRING, API_ID, API_HASH
from Utils import RABSEN


api_id = API_ID
api_hash = API_HASH
sesi_file = STRING

dest_1 = 'https://t.me/tg_lpm'
dest_2 = 'https://t.me/https://t.me/tgiklan'



isi_pesan = """🔥🔥🔥 KUMPULAN LINK 🔥🔥🔥
#CHANNEL DAN #GROUP

📣 @ALPHAXPROJECT"""

def hard():
	print("AlphaXbot_v0.0.3 is Starting...")
    loop = asyncio.set_event_loop(asyncio.new_event_loop())
    with TelegramClient(session=STRING,
    	api_id=API_ID,
        api_hash=API_HASH,
        loop=loop) as client:

        async def nungguin(w):
            await asyncio.sleep(w)

        async def alphax(client, w):
            while True:
                await client.send_message(dest_1, {isi_pesan})
                print (time.asctime(),'_','Success -> Messages Task 1 Sent!!!')

                await client.send_message(dest_2, {isi_pesan})
                print (time.asctime(),'_','Success -> Messages Task 2 Sent!!!')
                await nungguin(w)


        with client:
            # parameter kedua alphax adalah lamanya menunggu dalam detik jika 8 menit maka dalam detik 480
            client.loop.create_task(alphax(client, 30))
            client.run_until_disconnected()


threading.Thread(target=hard).start()
print('==============================')
print('AlphaXbot_v0.0.3 IS RUNNING...')
print('==============================')

# if abis == 2 :
#    client.disconnect()
#    clien.disconnect()
