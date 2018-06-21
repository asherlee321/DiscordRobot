
import discord
import asyncio
TOKEN = 'NDU4MTYxMjMzNjcwMDQ1NzEw.DgjqXg.ZYrnJyx7Fr_7-oTtNo8iOsrHD4o'

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith('james') or message.content.startswith('itai') or message.content.startswith('jude'):
        await client.send_message(message.channel, "This Bot will live forever")
    if message.content.startswith('loop') and !message.content.startswith('stop'):
       await client.send_message(message.channel, message.content)
  
    if  "pls" in message.content:
        await client.delete_message(message)
 
    
       


        
    
        

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')





    
client.run(TOKEN)
