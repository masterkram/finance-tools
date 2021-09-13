import os
import discord
from dotenv import load_dotenv

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.mention_everyone:
        return

    if message.author == client.user:
        return

    if message.content.startswith('!fin'):
        await message.channel.send("helolo")
        return


def main():
    client.run(TOKEN)


if __name__ == '__main__':
    main()
