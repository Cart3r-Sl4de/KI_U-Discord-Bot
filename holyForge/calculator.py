import discord, os, asyncio, random, requests, json, dictionary
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import has_permissions
import weapons_forge as wf

#blender (pretty much, classes)
cw = {3:3, 7:3, 4:7, 2:4, 2.4:8} #claws 1
o = {6:7, 8:5, 9:6, 4:4, 8.4:4} #orbitars 2
bl = {7:8, 5:8, 4:9, 8:9, 6:8} #blades 3
cb = {1.4:3, 2:7, 1:1, 5:1, 9:5} #clubs 4
b = {6:3, 4:1, 8:1, 2:9, 6.4:6} #bows 5
a = {3:9, 1:7, 5:7, 1.4:9, 9:9} #arms 6
s = {4:3, 8:3, 2:1, 1:6, 6:8} #staves 7
cn = {7:7, 9:7, 5:5, 2.4:5, 2:2} #cannons 8
p = {5:3, 2:3, 4:5, 8:8, 6:2} #palms 9

#math (pretty much, specific weapon)
one = {12:1, 11:2, 10:3, 9:4, 8:5, 7:6}
two = {1:1, 12:2, 11:3, 10:4, 9:5, 8:6, 7:7}
three = {2:1, 12:3, 11:4,10:5, 9:6, 8:7}
four = {2:2, 12:4, 11:5, 10:6, 9:7, 8:8}
five = {2:3, 12:5, 11:6, 10:7, 9:8, 4:1}
six = {3:3, 12:6, 11:7, 10:8, 9:9, 5:1, 4:2}
seven = {3:4, 12:7, 11:8, 10:9, 5:2, 6:1}
eight = {4:4, 12:8, 11:9, 10:10, 5:3, 6:2, 7:1}
nine = {4:5, 12:9, 11:10, 6:3, 7:2, 8:1}
ten = {5:5, 12:10, 11:11, 6:4, 7:3, 8:2, 9:1}
eleven = {6:5, 12:11, 10:1, 7:4,8:3, 9:2}
twelve = {12:12, 6:6, 7:5, 10:2,11:1, 8:4, 9:3}

#the whole package
allWeapons = {1: wf.claws, 2: wf.orbitars, 3: wf.blades, 4: wf.clubs, 5: wf.bows, 6: wf.arms, 7: wf.staffs, 8: wf.cannons, 9: wf.palms}
blender = {1:cw, 2:o, 3:bl, 4:cb, 5:b, 6:a, 7:s, 8:cn, 9:p}
math = {1:one, 2:two, 3:three, 4:four, 5:five, 6:six, 7:seven, 8:eight, 9:nine, 10:ten, 11:eleven, 12:twelve}

class Calculator(commands.Cog):

    def __init__(self, bot: commands.Cog) -> None:
        self.bot = bot

  #insert commands here

#######>COST CALCULATOR<#######
    @app_commands.command(name="weapon-calculator", description="yes")
    async def whatsTheCost(self, interaction: discord.Interaction, claws: wf.Claws = None, orbitars: wf.Orbitars = None, blades: wf.Blades = None,
                           clubs: wf.Clubs = None, bows: wf.Bows = None, arms: wf.Arms = None,
                           staves: wf.Staffs = None, cannons: wf.Cannons = None, palms: wf.Palms = None):

        weapon_iter = [claws, orbitars, blades, clubs, bows, arms, staves, cannons, palms]

    '''grandTotal = "**" + (allWeapons.get(category)).get(choiceWeapon) + "**\n"
    #blender and math; weapon category and weapon type
    for blendy in blender.get(category):
      for mathy in math.get(choiceWeapon):
        blendFirst = int(blendy)
        mathFirst = int(mathy)
        blendSecond = round((blender.get(category)).get(blendy)) #get second value of current blend
        mathSecond = (math.get(choiceWeapon)).get(mathy) #get second value of current math
        grandTotal += (allWeapons.get(blendFirst)).get(mathFirst) + " + " + (allWeapons.get(blendSecond)).get(mathSecond) + "\n"

    await ctx.send("```" + grandTotal + "```")'''


def setup(client):
  client.add_cog(Calculator(client))
