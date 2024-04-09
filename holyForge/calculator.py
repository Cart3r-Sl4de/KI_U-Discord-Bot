import discord, os, asyncio, random, requests, json, dictionary
from discord.ext import commands
from discord.ext.commands import has_permissions

#Weapon type storage
claws = {
  1: 'Tiger Claws', 2: 'Wolf Claws', 3: 'Bear Claws', 4: 'Brawler Claws', 5: 'Stealth Claws', 6: 'Hedgehog Claws', 7: 'Raptor Claws', 8: 'Artillery Claws', 9: 'Cancer Claws', 10: 'Beam Claws', 11: 'Viridi Claws', 12: 'Pandora Claws'
  }
orbitars = {1: 'Standard Orbitars', 2: 'Guardian Orbitars', 3: 'Shock Orbitars', 4: 'Eyetrack Orbitars', 5: 'Fairy Orbitars', 6: 'Paw Pad Orbitars', 7: 'Jetstream Orbitars', 8: 'Boom Orbitars', 9: 'Gemni Orbitars', 10: 'Aurum Orbitars', 11: 'Centurion Orbitars', 12: 'Arlon Orbitars'
           }
blades = {1: 'First Blade', 2: 'Burst Blade', 3: 'Viper Blade', 4: 'Crusader Blade', 5: 'Royal Blade', 6: 'Optical Blade', 7: 'Samurai Blade', 8: 'Bullet Blade', 9: 'Aquarius Blade', 10: 'Aurum Blade', 11: 'Palutena Blade', 12: 'Gaol Blade'
         }
clubs = {1: 'Ore Club', 2: 'Babel Club', 3: 'Skyscraper Club', 4: 'Atlas Club', 5: 'Earthmaul Club', 6: 'Ogre Club', 7: 'Halo Club', 8: 'Black Club', 9: 'Capricorn Club', 10: 'Aurum Club', 11: 'Hedraw Club', 12: 'Magnus Club'
        }
bows = {1: 'Fortune Bow', 2: 'Silver Bow', 3: 'Meteor Bow', 4: 'Divine Bow', 5: 'Darkness Bow', 6: 'Crystal Bow', 7: 'Angel Bow', 8: 'Hawkeye Bow', 9: 'Sagittarius Bow', 10: 'Aurum Bow', 11: 'Palutena Bow', 12: 'Phosphora Bow'
       }
arms = {1: 'Crusher Arm', 2: 'Compact Arm', 3: 'Electroshock Arm', 4: 'Volcano Arm', 5: 'Drill Arm', 6: 'Bomber Arm', 7: 'Bowl Arm', 8: 'End-All Arm', 9: 'Taurus Arm', 10: 'Upperdash Arm', 11: 'Kraken Arm', 12: 'Pheonix Arm'
       }
staffs = {1: 'Insight Staff', 2: 'Orb Staff', 3: 'Rose Staff', 4: 'Knuckle Staff', 5: 'Ancient Staff', 6: 'Lancer Staff', 7: 'Flintlock Staff', 8: 'Somewhat Staff', 9: 'Scorpio Staff', 10: 'Laser Staff', 11: 'Dark Pit Staff', 12: 'Thanatos Staff'
         }
cannons = {1: 'EZ Cannon', 2: 'Ball Cannon', 3: 'Predator Cannon', 4: 'Poseidon Cannon', 5: 'Fireworks Cannon', 6: 'Rail Cannon', 7: 'Dynamo Cannon', 8: 'Doom Cannon', 9: 'Leo Cannon', 10: 'Sonic Cannon', 11: 'Twinbellow Cannon', 12: 'Cragalanche Cannon'
          }
palms = {1: 'Violet Palm', 2: 'Burning Palm', 3: 'Needle Palm', 4: 'Midnight Palm', 5: 'Cursed Palm', 6: 'Cutter Palm', 7: 'Pudgy Palm', 8: 'Ninja Palm', 9: 'Virgo Palm', 10: 'Aurum Palm', 11: 'Viridi Palm', 12: 'Great Reaper Palm'
        }

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
allWeapons = {1: claws, 2: orbitars, 3: blades, 4: clubs, 5: bows, 6: arms, 7: staffs, 8: cannons, 9: palms}
blender = {1:cw, 2:o, 3:bl, 4:cb, 5:b, 6:a, 7:s, 8:cn, 9:p}
math = {1:one, 2:two, 3:three, 4:four, 5:five, 6:six, 7:seven, 8:eight, 9:nine, 10:ten, 11:eleven, 12:twelve}

class Calculator(commands.Cog):

  def __init__(self, client):
    self.client = client

  #insert commands here
  #######>CHECK<#######
  @commands.command(aliases = ['chck'])
  async def check(self, ctx):
    def check(msg):
        return msg.author == ctx.author and msg.content.isdigit() and \
               msg.channel == ctx.channel

    await ctx.send("1: Claws, 2: Orbitars, 3: Blades, 4: Clubs, 5: Bows, 6: Arms, 7: Staffs, 8: Cannons, 9: Palms Please send corresponding number")
    msg1 = await self.client.wait_for("message", check=check)
    await ctx.send("Send a number from 1-12 to see corresponding answer")
    msg2 = await self.client.wait_for("message", check=check)
    x = int(msg1.content)
    y = int(msg2.content)

    if (((x > 0) and (x <= 12)) and ((y > 0) and (y <= 12))):
      await ctx.send((allWeapons.get(x)).get(y)) #send the weapon from the chosen category
    else:
      await ctx.send("Nice one, Pitty! Make sure you entered it correctly!")

#######>COST CALCULATOR<#######
  @commands.command(aliases = ['cost'])
  async def whatsTheCost(self, ctx):
    def check(msg):
        return msg.author == ctx.author and msg.content.isdigit() and \
               msg.channel == ctx.channel

    await ctx.send("```Please enter the corresponding category number for desired category to select:\n1: Claws\n2: Orbitars\n3: Blades\n4: Clubs\n5: Bows\n6: Arms\n7: Staffs\n8: Cannons\n9: Palms```")
    strCategory = await self.client.wait_for("message", check=check)
    result = "Now please select from the following:\n" #declare variable to store the result
    category = int(strCategory.content)
    x = 1
    while x < 13: #get all the weapons in the given category, list with numbers
      result += (str(x) + ": " + str((allWeapons.get(category)).get(x)))
      if x != 12:
        result += "\n"
      x += 1
      
    await ctx.send("```" + result + "```") #send the result
    weapon = await self.client.wait_for("message", check=check) #get user choice on weapon
    choiceWeapon = int(weapon.content)
    
    grandTotal = "**" + (allWeapons.get(category)).get(choiceWeapon) + "**\n"
    #blender and math; weapon category and weapon type
    for blendy in blender.get(category):
      for mathy in math.get(choiceWeapon):
        blendFirst = int(blendy)
        mathFirst = int(mathy)
        blendSecond = round((blender.get(category)).get(blendy)) #get second value of current blend
        mathSecond = (math.get(choiceWeapon)).get(mathy) #get second value of current math
        grandTotal += (allWeapons.get(blendFirst)).get(mathFirst) + " + " + (allWeapons.get(blendSecond)).get(mathSecond) + "\n"

    await ctx.send("```" + grandTotal + "```")


def setup(client):
  client.add_cog(Calculator(client))
