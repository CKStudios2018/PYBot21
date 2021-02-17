import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('PYBot is ready!')

@client.command()
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount)

@client.command()
async def ping(ctx):
    await ctx.send(f'Reply! {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball', '8Ball', 'eightball'])
async def _8ball(ctx, *, question):
    responses = ['It is certain.',
                 'It is decidedly so.',
                 'Without a doubt.',
                 'Yes - definitely.',
                 'You may rely on it.',
                 'As I see it, yes.',
                 'Most likely.',
                 'Outlook good.',
                 'Outcome positive.',
                 'Yes.',
                 'Signs point to yes.',
                 'Reply hazy, try again later...',
                 'Ask again... later.',
                 'Better not tell you now.',
                 'Cannot predict now',
                 'Concentrate and ask again',
                 "Don't count on it",
                 "You mustn't rely on it.",
                 'My reply is no',
                 'My sources say no',
                 'Outlook not so good',
                 'Very doubtful.',
                 'Ask @Chawi Mi#8485']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')



client.run(random.token.py) #This is NOT the actual token, this code is hidden
