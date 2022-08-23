import discord
from discord.ext import commands
import pandas as pd
import warnings
import os

from discord import File
intents = discord.Intents.all()



client = commands.Bot(command_prefix='!', intents=intents)
guild = discord.Guild
ADMIN_1 = client.get_user(int(os.environ.get('ADMIN1_ID')))
ADMIN_2 = client.get_user(int(os.environ.get('ADMIN2_ID')))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    else:
        name_of_channel = message.channel.name
        name_of_server = message.guild.name
        if message.content == "!links":
            data = pd.DataFrame(columns=["Content", "Title", "Time"])
            limit = 10000000
            async for message in message.channel.history(limit=limit):
                if message.author != client.user:
                    words = message.content.split()
                    titles = message.content.split()
                    for word in words:
                        test_list = [".com", ".ru", ".net", ".org", ".info", ".biz", ".io", ".co", "https://",
                                     "http://"]
                        found = False
                        for extension in test_list:
                            if extension in word:
                                found = True
                                break
                        if found:
                            if message.author != client.user:
                                for heading in titles:
                                    if heading.startswith("**"):
                                        start = (titles.index(heading))
                                        for ends in titles:
                                            if ends.endswith("**"):
                                                end = titles.index(ends) + 1
                                                title = [titles[num].replace("**", '') for num in range(start, end)]
                                                title = " ".join(title).title()
                                                data = data.append({"Content": word,
                                                                    "Title": title,
                                                                    "Time": message.created_at.strftime('%Y-%m-%d'),
                                                                    }, ignore_index=True)

                                                if len(data) == limit:
                                                    break
                                            elif ends.endswith("**,"):
                                                end = titles.index(ends) + 1
                                                title = [titles[num].replace("**", '').replace(",", "") for num in range(start, end)]
                                                title = " ".join(title).title()
                                                data = data.append({"Content": word,
                                                                        "Title": title,
                                                                        "Time": message.created_at.strftime('%Y-%m-%d'),
                                                                    }, ignore_index=True)
                                                if len(data) == limit:
                                                    break
                                            elif ends.endswith("**."):
                                                end = titles.index(ends) + 1
                                                title = [titles[num].replace("**", '').replace(".","") for num in range(start, end)]
                                                title = " ".join(title).title()
                                                data = data.append({"Content": word,
                                                                    "Title": title,
                                                                    "Time": message.created_at.strftime('%Y-%m-%d')
                                                                    }, ignore_index=True)
                                                if len(data) == limit:
                                                    break
                                                warnings.simplefilter(action="ignore", category=FutureWarning)
                                            warnings.simplefilter(action="ignore", category=FutureWarning)
                                        warnings.simplefilter(action="ignore", category=FutureWarning)
                                    warnings.simplefilter(action="ignore", category=FutureWarning)
                            warnings.simplefilter(action="ignore", category=FutureWarning)
                            file_location = "Learning library.csv"
                            data.to_csv(file_location, index=False)
            authors = [ADMIN_1, ADMIN_2]
            for author in authors:
                await author.send(f"Here is the file for: \n channel: {name_of_channel} \n server: {name_of_server}",
                                          file=File("Learning library.csv"))
            await message.channel.send('SENT 😇 ')

client.run(os.environ.get('TOKEN'))

