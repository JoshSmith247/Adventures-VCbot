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
            
            print('Channels Enabled.')
            await client.change_presence(activity=discord.Game(name="The Server is OPEN"))

    if message.content.startswith('$disable'):

        if message.guild.name == "AiC Minecraft Voice Channels & Hub":
            perms = discord.Permissions()
            perms.update(connect = False)

            await message.guild.get_role(746811071955730562).edit(permissions=perms, reason=None)
            await message.channel.send('Channels Disabled.')

            print('Channels Disabled.')
            await client.change_presence(activity=discord.Game(name="The Server is CLOSED"))

    if message.content.startswith('$help'):
        await message.delete()
        await message.author.send('Commands:')
        await message.author.send('$help    - Sends pm of all current commands')
        await message.author.send('$enable  - Enables campers to connect to VCs')
        await message.author.send('$disable - Blocks campers from connect to VCs')

client.run('ODQxNzI2MDk4Mzc0MDAwNjQx.YJq8hA.1CG3BOzkwO-dexoB2lC0QZk1PmI')