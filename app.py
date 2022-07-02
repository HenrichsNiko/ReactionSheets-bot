import datetime, requests, asyncio, random, discord, os
from multiprocessing.connection import wait
import nextcord
from nextcord.ext import commands
from discord.utils import get
from discord import message, client
from authorization import list_getter
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("token")

pvm_list=[]
pvp_list=[]
hybrid_list=[]

intents = nextcord.Intents.all()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

# pvm_emoji ='<:pvm:992059085786726410>'
# hybrid_emoji = '<:hybrid:992059208650461274>'
# pvp_emoji = '<:pvp:992059224228106262>'

@bot.command(pass_context = True, name='witch')
async def test(ctx):
    
    pvm  = get(ctx.guild.emojis, name="pvm")
    hybrid  = get(ctx.guild.emojis, name="hybrid")
    pvp  = get(ctx.guild.emojis, name="pvp")
    
    msg = await ctx.send('@everyone Ice Witch Reminder')
    await msg.add_reaction(pvm)
    await msg.add_reaction(hybrid)
    await msg.add_reaction(pvp)
           
# @bot.event
# async def on_message(message):
#     if 'https://' in message.content:
#         await message.delete()
#         await message.channel.send(f"{message.author.mention} Don't send links!")
#     else:
#         await bot.process_commands(message)
        

@bot.event
async def on_reaction_add(reaction, user):
    
    message = reaction.message
    msg_id = message.id
    
    pvm  = get(message.guild.emojis, name="pvm")
    hybrid  = get(message.guild.emojis, name="hybrid")
    pvp  = get(message.guild.emojis, name="pvp")
    
    new_message = await message.channel.fetch_message(msg_id)
    
    if any(reaction.emoji == '✅' for reaction in new_message.reactions):
            
        for reaction in new_message.reactions:
            if (reaction.emoji==pvm):
                async for user in reaction.users():
                    if (user != bot.user):
                        # await ctx.send(user.name)
                        pvm_list.append(user.name)
        
        for reaction in new_message.reactions:
            if (reaction.emoji==hybrid):
                async for user in reaction.users():
                    if (user != bot.user):
                        # await ctx.send(user.name)
                        hybrid_list.append(user.name)
        
        for reaction in new_message.reactions:
            if (reaction.emoji==pvp):
                async for user in reaction.users():
                    if (user != bot.user):
                        # await message.send(user.name)
                        pvp_list.append(user.name)
        # print(pvm_list,hybrid_list,pvp_list) 
        list_getter(pvm_list,hybrid_list,pvp_list)
        pvm_list.clear()
        hybrid_list.clear()
        pvp_list.clear()
    else:
        await bot.process_commands(message)
  
@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user.name}")
    
if __name__ == '__main__':
    bot.run(token)
