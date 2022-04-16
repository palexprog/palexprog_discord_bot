import discord
from discord.ext import commands

client = commands.Bot(command_prefix="$", intents=discord.Intents.all())


@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))

    for guild in client.guilds:
        for text_channel in guild.text_channels:
            if text_channel.name == 'test_bota':
                await text_channel.send('здорова')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.author.name == 'mendoza':
        await message.channel.send('миша иди в жопу')
        return


@client.command(name="hello")
async def hello(ctx):
    await ctx.send('hello')


@client.command()
async def winrate(ctx):
    # #a = message.content.split()  # 2 10
    # win = int(a[1])
    # all = int(a[2])
    # if win > all:
    #     await message.channel.send('ошибка')
    # else:
    #     await message.channel.send(f'твой винрейт {int(win / all * 100)}%')
    print(1)
    print(ctx.__dict__)


client.run('MzUyNTk0NDk1NTEyMTE3MjU5.WadJNg.A6FPjXnZs85ZyqXSAY7b1Dk1WY0')
