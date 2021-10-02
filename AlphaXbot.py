# This a part of https://t.me/AlphaXProject
# AlphaXbot_v0.0.1

import time
import asyncio
import sys
import random
import threading

from telethon import TelegramClient, events, utils
from Config import STRING, API_ID, API_HASH

api_id = API_ID
api_hash = API_HASH
sesi_file = STRING

dest_1 = 'https://t.me/tg_lpm'
dest_2 = 'https://t.me/https://t.me/tgiklan'



isi_pesan = """🔥🔥🔥 KUMPULAN LINK 🔥🔥🔥
#CHANNEL DAN #GROUP

📣 @TGRECEH


POWERED BY:
✅ @CARITEMANLINK"""

def hard():
    loop = asyncio.set_event_loop(asyncio.new_event_loop())
    with TelegramClient('AlphaXbot', api_id, api_hash, loop=loop) as client:

        async def nungguin(w):
            await asyncio.sleep(w)

        async def pythonclass(client, w):
            while True:
                await client.send_message(dest_1, {isi_pesan})
                print (time.asctime(),'_','Success -> Messages Task 1 Sent!!!')

                await client.send_message(dest_2, {isi_pesan})
                print (time.asctime(),'_','Success -> Messages Task 2 Sent!!!')
                await nungguin(w)


        with client:
            # parameter kedua Python Class adalah lamanya menunggu dalam detik jika 8 menit maka dalam detik 480
            client.loop.create_task(pythonclass(client, 30))
            client.run_until_disconnected()


threading.Thread(target=hard).start()
print('========================================')
print(' TELEGRAM | AUTO POST BOT IS STARTING...')
print('       Powered by: Python | Telethon    ')
print('            Edited by: TEAM-X           ')
print('            -----------------           ')
print('       connect with us on Telegram:     ')
print('-> @PenaklukVagina | @FuckBoyPensiun <- ')
print('   -> @LesbiLator | @SukriHamdiP02 <-   ')
print(' -> @SunghaJungGuitar | @MacRichReal <- ')
print('========================================')

# if abis == 2 :
#    client.disconnect()
#    clien.disconnect()
