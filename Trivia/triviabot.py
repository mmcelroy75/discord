import discord
from discord.ext import commands
import random
from dotenv import load_dotenv
import os

load_dotenv('.env')
client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print("Bot is ready.")


@client.event
async def on_member_join(member):
    print(f'{member} has joined {discord.Guild.name}.')


@client.event
async def on_member_remove(member):
    print(f'{member} has left {discord.Guild.name}.')

'''
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')
'''


@client.command(aliases=['trivia', 'test'])
async def _trivia(ctx):
    trivia_list = [
        'Carlos Santana was only 16 years old when he played Woodstock in 1969.',
        'Jeff Lynne\'s first band was called "The Move".',
        'Tom Waits and Rickie Lee Jones dated for a while in the 1970s.'
    ]

    await ctx.send(f'{random.choice(trivia_list)}')


client.run(os.getenv('MUSIC_TRIVIA_TOKEN'))
