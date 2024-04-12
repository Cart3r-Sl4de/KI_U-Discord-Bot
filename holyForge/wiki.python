import discord, os, asyncio, random, requests, json, dictionary
from discord.ext import commands
from discord.ext.commands import has_permissions

#copy and paste is a funny thing

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

#wiki links
clawsWiki = {
  1: 'https://kidicarus.fandom.com/wiki/Tiger_Claws', 2: 'https://kidicarus.fandom.com/wiki/Wolf_Claws', 3: 'https://kidicarus.fandom.com/wiki/Bear_Claws', 4: 'https://kidicarus.fandom.com/wiki/Brawler_Claws', 5: 'https://kidicarus.fandom.com/wiki/Stealth_Claws', 6: 'https://kidicarus.fandom.com/wiki/Hedgehog_Claws', 7: 'https://kidicarus.fandom.com/wiki/Raptor_Claws', 8: 'https://kidicarus.fandom.com/wiki/Artillery_Claws', 9: 'https://kidicarus.fandom.com/wiki/Cancer_Claws', 10: 'https://kidicarus.fandom.com/wiki/Beam_Claws', 11: 'https://kidicarus.fandom.com/wiki/Viridi_Claws', 12: 'https://kidicarus.fandom.com/wiki/Pandora_Claws'
  }
orbitarsWiki = {1: 'https://kidicarus.fandom.com/wiki/Standard_Orbitars', 2: 'https://kidicarus.fandom.com/wiki/Guardian_Orbitars', 3: 'https://kidicarus.fandom.com/wiki/Shock_Orbitars', 4: 'https://kidicarus.fandom.com/wiki/Eyetrack_Orbitars', 5: 'https://kidicarus.fandom.com/wiki/Fairy_Orbitars', 6: 'https://kidicarus.fandom.com/wiki/Paw_Pad_Orbitars', 7: 'https://kidicarus.fandom.com/wiki/Jetstream_Orbitars', 8: 'https://kidicarus.fandom.com/wiki/Boom_Orbitars', 9: 'https://kidicarus.fandom.com/wiki/Gemni_Orbitars', 10: 'https://kidicarus.fandom.com/wiki/Aurum_Orbitars', 11: 'https://kidicarus.fandom.com/wiki/Centurion_Orbitars', 12: 'https://kidicarus.fandom.com/wiki/Arlon_Orbitars'
           }
bladesWiki = {1: 'https://kidicarus.fandom.com/wiki/First_Blade', 2: 'https://kidicarus.fandom.com/wiki/Burst_Blade', 3: 'https://kidicarus.fandom.com/wiki/Viper_Blade', 4: 'https://kidicarus.fandom.com/wiki/Crusader_Blade', 5: 'https://kidicarus.fandom.com/wiki/Royal_Blade', 6: 'https://kidicarus.fandom.com/wiki/Optical_Blade', 7: 'https://kidicarus.fandom.com/wiki/Samurai_Blade', 8: 'https://kidicarus.fandom.com/wiki/Bullet_Blade', 9: 'https://kidicarus.fandom.com/wiki/Aquarius_Blade', 10: 'https://kidicarus.fandom.com/wiki/Aurum_Blade', 11: 'https://kidicarus.fandom.com/wiki/Palutena_Blade', 12: 'https://kidicarus.fandom.com/wiki/Gaol_Blade'
         }
clubsWiki = {1: 'https://kidicarus.fandom.com/wiki/Ore_Club', 2: 'https://kidicarus.fandom.com/wiki/Babel_Club', 3: 'https://kidicarus.fandom.com/wiki/Skyscraper_Club', 4: 'https://kidicarus.fandom.com/wiki/Atlas_Club', 5: 'https://kidicarus.fandom.com/wiki/Earthmaul_Club', 6: 'https://kidicarus.fandom.com/wiki/Ogre_Club', 7: 'https://kidicarus.fandom.com/wiki/Halo_Club', 8: 'https://kidicarus.fandom.com/wiki/Black_Club', 9: 'https://kidicarus.fandom.com/wiki/Capricorn_Club', 10: 'https://kidicarus.fandom.com/wiki/Aurum_Club', 11: 'https://kidicarus.fandom.com/wiki/Hedraw_Club', 12: 'https://kidicarus.fandom.com/wiki/Magnus_Club'
        }
bowsWiki = {1: 'https://kidicarus.fandom.com/wiki/Fortune_Bow', 2: 'https://kidicarus.fandom.com/wiki/Silver_Bow', 3: 'https://kidicarus.fandom.com/wiki/Meteor_Bow', 4: 'https://kidicarus.fandom.com/wiki/Divine_Bow', 5: 'https://kidicarus.fandom.com/wiki/Darkness_Bow', 6: 'https://kidicarus.fandom.com/wiki/Crystal_Bow', 7: 'https://kidicarus.fandom.com/wiki/Angel_Bow', 8: 'https://kidicarus.fandom.com/wiki/Hawkeye Bow', 9: 'https://kidicarus.fandom.com/wiki/Sagittarius_Bow', 10: 'https://kidicarus.fandom.com/wiki/Aurum_Bow', 11: 'https://kidicarus.fandom.com/wiki/Palutena_Bow', 12: 'https://kidicarus.fandom.com/wiki/Phosphora_Bow'
       }
armsWiki = {1: 'https://kidicarus.fandom.com/wiki/Crusher_Arm', 2: 'https://kidicarus.fandom.com/wiki/Compact_Arm', 3: 'https://kidicarus.fandom.com/wiki/Electroshock_Arm', 4: 'https://kidicarus.fandom.com/wiki/Volcano_Arm', 5: 'https://kidicarus.fandom.com/wiki/Drill_Arm', 6: 'https://kidicarus.fandom.com/wiki/Bomber_Arm', 7: 'https://kidicarus.fandom.com/wiki/Bowl_Arm', 8: 'https://kidicarus.fandom.com/wiki/https://kidicarus.fandom.com/wiki/End-All_Arm', 9: 'https://kidicarus.fandom.com/wiki/Taurus_Arm', 10: 'https://kidicarus.fandom.com/wiki/Upperdash_Arm', 11: 'https://kidicarus.fandom.com/wiki/Kraken_Arm', 12: 'https://kidicarus.fandom.com/wiki/Pheonix_Arm'
       }
staffsWiki = {1: 'https://kidicarus.fandom.com/wiki/Insight_Staff', 2: 'https://kidicarus.fandom.com/wiki/Orb_Staff', 3: 'https://kidicarus.fandom.com/wiki/Rose_Staff', 4: 'https://kidicarus.fandom.com/wiki/Knuckle_Staff', 5: 'https://kidicarus.fandom.com/wiki/Ancient_Staff', 6: 'https://kidicarus.fandom.com/wiki/Lancer_Staff', 7: 'https://kidicarus.fandom.com/wiki/Flintlock_Staff', 8: 'https://kidicarus.fandom.com/wiki/Somewhat_Staff', 9: 'https://kidicarus.fandom.com/wiki/Scorpio_Staff', 10: 'https://kidicarus.fandom.com/wiki/Laser_Staff', 11: 'https://kidicarus.fandom.com/wiki/Dark_Pit Staff', 12: 'https://kidicarus.fandom.com/wiki/Thanatos_Staff'
         }
cannonsWiki = {1: 'https://kidicarus.fandom.com/wiki/EZ_Cannon', 2: 'https://kidicarus.fandom.com/wiki/Ball_Cannon', 3: 'https://kidicarus.fandom.com/wiki/Predator_Cannon', 4: 'https://kidicarus.fandom.com/wiki/Poseidon_Cannon', 5: 'https://kidicarus.fandom.com/wiki/Fireworks_Cannon', 6: 'https://kidicarus.fandom.com/wiki/Rail_Cannon', 7: 'https://kidicarus.fandom.com/wiki/Dynamo_Cannon', 8: 'https://kidicarus.fandom.com/wiki/Doom_Cannon', 9: 'https://kidicarus.fandom.com/wiki/Leo_Cannon', 10: 'https://kidicarus.fandom.com/wiki/Sonic_Cannon', 11: 'https://kidicarus.fandom.com/wiki/Twinbellow_Cannon', 12: 'https://kidicarus.fandom.com/wiki/Cragalanche_Cannon'
          }
palmsWiki = {1: 'https://kidicarus.fandom.com/wiki/Violet_Palm', 2: 'https://kidicarus.fandom.com/wiki/Burning_Palm', 3: 'https://kidicarus.fandom.com/wiki/Needle_Palm', 4: 'https://kidicarus.fandom.com/wiki/Midnight_Palm', 5: 'https://kidicarus.fandom.com/wiki/Cursed_Palm', 6: 'Cutter_Palm', 7: 'https://kidicarus.fandom.com/wiki/Pudgy_Palm', 8: 'https://kidicarus.fandom.com/wiki/Ninja_Palm', 9: 'https://kidicarus.fandom.com/wiki/Virgo_Palm', 10: 'https://kidicarus.fandom.com/wiki/Aurum_Palm', 11: 'https://kidicarus.fandom.com/wiki/Viridi_Palm', 12: 'https://kidicarus.fandom.com/wiki/Great_Reaper_Palm'
        }

allWeaponsWiki = {1: clawsWiki, 2: orbitarsWiki, 3: bladesWiki, 4: clubsWiki, 5: bowsWiki, 6: armsWiki, 7: staffsWiki, 8: cannonsWiki, 9: palmsWiki}

allWeapons = {1: claws, 2: orbitars, 3: blades, 4: clubs, 5: bows, 6: arms, 7: staffs, 8: cannons, 9: palms}

class Wiki(commands.Cog):

  def __init__(self, client):
    self.client = client

  #insert command here

  @commands.command(aliases = ['wiki'])
  async def weaponWiki(self, ctx):
    def check(msg):
        return msg.author == ctx.author and msg.content.isdigit() and \
               msg.channel == ctx.channel

    await ctx.send("```Please enter the corresponding category number for desired category to select:\n1: Claws\n2: Orbitars\n3: Blades\n4: Clubs\n5: Bows\n6: Arms\n7: Staffs\n8: Cannons\n9: Palms.```")
    strCategory = await self.client.wait_for("message", check=check)
    result = "Now please select from the following:\n" #declare variable to store the result
    category = int(strCategory.content)
    x = 1
    while x < 13: #get all the weapons in the given category, list with numbers
      result += (str(x) + ": " + str((allWeapons.get(category)).get(x)))
      if x != 12:
        result += "\n"
      x += 1

    await ctx.send("```" + result + "\nPlease type the desired corresponding weapon number.```")
    weapon = await self.client.wait_for("message", check=check)
    weaponChoice = int(weapon.content)
    if (((category > 0) and (category <= 12)) and ((weaponChoice > 0) and (weaponChoice <= 12))):
      await ctx.send((allWeaponsWiki.get(category)).get(weaponChoice)) #send the weapon from the chosen category
    else:
      await ctx.send("Nice one, Pitty! Make sure you entered it correctly!")


      

def setup(client):
  client.add_cog(Wiki(client))