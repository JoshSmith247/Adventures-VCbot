import discord
from mcstatus import MinecraftServer
import asyncio

client = discord.Client()

ArenasServer1 = MinecraftServer.lookup("104.193.183.98:56157")
CrSrServer1 = MinecraftServer.lookup("108.62.104.83:33861")
HubServer1 = MinecraftServer.lookup("192.210.236.66:10156")
AdventureServer1 = MinecraftServer.lookup("192.210.236.66:13552")

ArenasServer1status = ArenasServer1.status()
CrSrServer1status = CrSrServer1.status()
HubServer1status = HubServer1.status()
AdventureServer1status = AdventureServer1.status()

playerCount = ArenasServer1status.players.online + CrSrServer1status.players.online + HubServer1status.players.online + AdventureServer1status.players.online

def load_stats():
    ArenasServer1 = MinecraftServer.lookup("104.193.183.98:56157")
    CrSrServer1 = MinecraftServer.lookup("108.62.104.83:33861")
    HubServer1 = MinecraftServer.lookup("192.210.236.66:10156")
    AdventureServer1 = MinecraftServer.lookup("192.210.236.66:13552")

    ArenasServer1status = ArenasServer1.status()
    CrSrServer1status = CrSrServer1.status()
    HubServer1status = HubServer1.status()
    AdventureServer1status = AdventureServer1.status()
    
    global playerCount
    playerCount = ArenasServer1status.players.online + CrSrServer1status.players.online + HubServer1status.players.online + AdventureServer1status.players.online

stats = False
countMsg = 0

print("There are a total of " + str(playerCount) + " players online.")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    #Note reset stats channel and new stats

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

    if message.content.startswith('$newstats'):
        
        if message.guild.name == "AiC Minecraft Voice Channels & Hub" and message.channel.name == "server-stats":
            await message.delete()
            
            global stats
            stats = True
            
            await message.channel.send(":bar_chart:  Server Stats  :bar_chart:")
            await message.channel.send("Player Count: " + str(playerCount))
            
            global countMsg
            countMsg = message.channel.last_message_id
    
    if message.content.startswith('$updatestats'):
        await message.delete()
        load_stats()
        await update_stats()
    
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
    
    if message.content.startswith('$event'):
        await message.delete()
        args = message.content.split('"');
        
        embed = discord.Embed(title=args[1], url=args[2], description=args[3], color=discord.Color.blue())
        embed.set_thumbnail(url=args[4])
        
        if len(args) > 5 and args[5] != "null":
            embed.set_footer(text=args[5]);
        
        i = 6
        while i + 1 < len(args):
            embed.add_field(name=args[i], value=args[i+1])
            i += 2
            
        await message.channel.send(embed=embed)

# Updating Stats
async def update_stats():
    if stats == True:
        thisMsg = client.get_channel(842803726296416266)
        thisMsg = await thisMsg.fetch_message(countMsg)
        
        cnt = "Player Count: " + str(playerCount)
        await thisMsg.edit(content=cnt)

# Updating Stats
async def periodic():
    while True:
        load_stats()
        await update_stats()
        print("UPDATE")
        await asyncio.sleep(5)

client.run('ODQxNzI2MDk4Mzc0MDAwNjQx.YJq8hA.1CG3BOzkwO-dexoB2lC0QZk1PmI')