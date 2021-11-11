import os
import discord
from discord.ext import commands
from keep_alive import keep_alive

client = commands.Bot(command_prefix = '^')

word_list = ['shit', 'fuck', 'ass', 'crap', 'dick', 'eee', 'penis', 'nigg', 'fag', 'gay', 'queer']


@client.event
async def on_ready():
  print('Bot is ready {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  messageAuthor = message.author
  messageContent = message.content
  lowerCaseContent = messageContent.lower()
  hate = 'uwu'
  if len(messageContent) > 0:
    if lowerCaseContent == hate:
      await message.channel.send(messageAuthor)
      await message.channel.send('I hate you')
  
    for word in word_list:
      if word in lowerCaseContent:
        await message.delete()
        await message.channel.send('Do not say that!')
        await message.channel.send(file=discord.File('eye.jpeg'))
  
    
    

  if message.content.startswith('$hello'):
    await message.channel.send('hello')


token = os.environ['TOKEN']

keep_alive()
client.run(token)