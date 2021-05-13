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

        if message.guild.name == "AiC Minecraft Voice Channels & Hub":
            perms = discord.Permissions()
            perms.update(connect = True)

            await message.guild.get_role(746811071955730562).edit(permissions=perms, reason=None)
            await message.channel.send('Channels Enabled.')
            
            print('Channels Disabled.')

    if message.content.startswith('$disable'):

        if message.guild.name == "AiC Minecraft Voice Channels & Hub":
            perms = discord.Permissions()
            perms.update(connect = False)

            await message.guild.get_role(746811071955730562).edit(permissions=perms, reason=None)
            await message.channel.send('Channels Disabled.')

            print('Channels Disabled.')

client.run('ODQxNzI2MDk4Mzc0MDAwNjQx.YJq8hA.1CG3BOzkwO-dexoB2lC0QZk1PmI')