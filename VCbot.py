import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$enable'):

        if message.guild.name == "Deverman but its a server":
            perms = discord.Permissions()
            perms.update(connect = True)

            await message.guild.get_role(740031880610709525).edit(permissions=perms, reason=None)
            await message.channel.send('Channels Enabled.')
            return

    if message.content.startswith('$disable'):

        if message.guild.name == "Deverman but its a server":  
            perms = discord.Permissions()
            perms.update(connect = False)

            await message.guild.get_role(740031880610709525).edit(permissions=perms, reason=None)
            await message.channel.send('Channels Disabled.')
            return

client.run('ODQxNzI2MDk4Mzc0MDAwNjQx.YJq8hA.VL49KRzuceeU_-j1uuYK-HZNFWo')