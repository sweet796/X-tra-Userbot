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
        rantext = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))
        api_token = '690b490e0f197d97b059e32b56a7639c1ca936a2'
        req = requests.get('https://clicksfly.com/api?api={}&url={}&alias={}'.format(api_token, m.text, rantext)).json()
        if(req["status"] == 'error'):
          smsg = req["message"]
        else:
          smsg = req["shortenedUrl"]
      
        sent = await m.reply(smsg)
    await event.edit("Done...")

@loader.command(pattern="^.remclk", outgoing=True)
async def remclk(event):
    await event.edit("K...")
    client.remove_event_handler(clkstart)
    await event.edit("Done...")
