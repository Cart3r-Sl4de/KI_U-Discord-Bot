import discord, os, asyncio, random, requests, json, dictionary
from discord.ext import commands
from discord.ext.commands import has_permissions

class Diagrams(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases = ['idk','bruh'])
  async def picture(self, ctx):
    def check(msg):
        return msg.author == ctx.author and msg.content.isdigit() and \
               msg.channel == ctx.channel

    await ctx.send("```1: Claws\n2: Orbitars\n3: Blades\n4: Clubs\n5: Bows\n6: Arms\n7: Staffs\n8: Cannons\n9: Palms\nPlease send the corresponding number to see desired Weapons group```")
    x = await self.client.wait_for("message", check=check)
    query = int(x.content)

    if query == 1:
      await ctx.send(file = discord.File("claws.png"))
      await ctx.send("```Right-Left Top row-Bottom row:\nTiger\nWolf\nBear\nBrawler\nStealth\nHedgehog\nRaptor\nArtillery\nCancer```")
    elif query == 2:
      await ctx.send(file = discord.File("orbitars.png"))
      await ctx.send("```Right-Left Top row-Bottom row:\nStandard\nGuardian\nShock\nEyetrack\nFairy\nPaw Pad\nJetstream\nBoom\nGemni\nAurum\nCenturion\nArlon```")
    elif query == 3:
      await ctx.send(file = discord.File("blades.png"))
      await ctx.send("```Right-Left Top row-Bottom row:\nFirst\nBurst\nViper\nCrusader\nRoyal\nOptical\nSamurai\nBullet\nAquarius\nAurum\nPalutena\nGaol```")
    elif query == 4:
      await ctx.send(file = discord.File("clubs.png"))
      await ctx.send("```Right-Left Top row-Bottom row:\nOre\nBabel\nSkyscraper\nAtlas\nEarthmaul\nOgre\nHalo\nBlack\nCapricorn\nAurum\nHedraw\nMagnus```")
    elif query == 5:
      await ctx.send(file = discord.File("bows.png"))
      await ctx.send("```Right-Left Top row-Bottom row:\nFortune\nSilver\nMeteor\nDivine\nDarkness\nCrystal\nAngel\nHawkeye\nSagittarius\nAurum\nPalutena\nPhosphora```")
    elif query == 6:
      await ctx.send(file = discord.File("arms.png"))
      await ctx.send("Right-Left Top row-Bottom row:\nCrusher\nCompact\nElectroshock\nVolcano\nDrill\nBomber\nBowl\nEnd-All\nTaurus\nUpperdash\nKraken\nPheonix")
    elif query == 7:
      await ctx.send(file = discord.File("staves.png"))
      await ctx.send("```Right-Left Top row-Bottom row:\nInsight\nOrb\nRose\nKnuckle\nAncient\nLances\nFlintlock\nSomewhat\nScorpio\nLaser\nDark Pit\nThanatos```")
    elif query == 8:
      await ctx.send(file = discord.File("cannons.png"))
      await ctx.send("```Right-Left Top row-Bottom row:\nEZ\nBall\nPredator\nPoseidon\nFireworks\nRail\nDynamo\nDoom\nLeo\nSonic\nTwinbellows\nCragalanche```")
    elif query == 9:
      await ctx.send(file = discord.File("palms.png"))
      await ctx.send("```Right-Left Top row-Bottom row:\nViolet\nBurning\nNeedle\nMidnight\nCursed\nCutter\nPudgy\nNinja\nVirgo\nAurum\nViridi\nGreat Reaper```")
    else:
      await ctx.send("Nice one, Pitty! ")

def setup(client):
  client.add_cog(Diagrams(client))