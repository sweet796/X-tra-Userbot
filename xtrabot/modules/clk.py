import random
import string
import requests
from random import randint 
from xtrabot import loader, client
  
@loader.command(pattern=r"^.enaclk", outgoing=True)
async def enaclk(event):
    await event.edit("K...")
    @loader.command(pattern=r"^http",incoming=True, func=lambda e: e.is_private)
    async def clkstart(m):
        person = await m.get_sender()
        user=person.first_name
        rantext = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(7))
        api_token = 'c4a94d4ff904a4292742e1f945b33e3efcc584ab'
        req = requests.get('https://gplinks.in/api?api={}&url={}&alias={}'.format(api_token, m.text, rantext)).json()
        if(req["status"] == 'error'):
          smsg = req["message"]
        else:
          smsg = req["shortenedUrl"]
      
        sent = await m.reply(smsg)
    await event.edit("Done...")
