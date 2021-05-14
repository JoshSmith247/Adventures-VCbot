import discord
from mcstatus import MinecraftServer

client = discord.Client()
server = MinecraftServer.lookup("aicrealm.mcpro.co")

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
            await client.change_presence(activity=discord.Game(name="The Server is OPEN ("))

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
        await message.author.send('Commands (All Users):')
        await message.author.send('$help    - Sends pm of all current commands')
        await message.author.send('$pack    - Sends pm of resource pack downloads')
        
        await message.author.send('Commands (Admin Only):')
        await message.author.send('$enable  - Enables campers to connect to VCs')
        await message.author.send('$disable - Blocks campers from connect to VCs')

    if message.content.startswith('$pack'):
        embed = discord.Embed(title='AiC Server Resource Pack', url='https://github.com/JoshSmith247/RelicBuild-Bukkit-Plugin/releases/download/3.4/AIC_mc_texture_pack_V3.4.zip', description='Adventures In Cardboard Resource Packs', color=discord.Color.blue())
        embed.set_thumbnail(url='https://adventuresincardboard.com/wp-content/uploads/bb-plugin/cache/lastmonsterlivekid-scaled-circle.jpg')
        embed.add_field(name="v. 3.4", value="[Link](https://github.com/JoshSmith247/RelicBuild-Bukkit-Plugin/releases/download/3.4/AIC_mc_texture_pack_V3.4.zip)", inline=True)
        embed.add_field(name="v. 3.3", value="[Link](https://github.com/JoshSmith247/RelicBuild-Bukkit-Plugin/releases/download/3.3/AIC_mc_texture_pack_V3.3.zip)", inline=True)
        embed.set_footer(text='Add .zip to .minecraft/resourcepacks folder for installation and select in game menu.')
        await message.author.send(embed=embed)

client.run('ODQxNzI2MDk4Mzc0MDAwNjQx.YJq8hA.1CG3BOzkwO-dexoB2lC0QZk1PmI')