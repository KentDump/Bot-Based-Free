import discord
from discord.ext import commands

# Replace with your bot's token
bot = commands.Bot(command_prefix="!")

@bot.command()
async def Ninja Master Hattori Mgui(ctx):
  embed = discord.Embed(title="myprincessiskwin Information", description="Please check this information out before it's too late!", color=0x00ff00)
  embed.add_field(name="Game Info", value="Visits: \nPlaying: \nFavorites: ", inline=False)
  embed.add_field(name="Username", value="username", inline=True)
  embed.add_field(name="Password", value="Password", inline=True)
  embed.add_field(name="Membership", value="P\nNBC", inline=True)
  embed.add_field(name="Security", value="Unverified", inline=True)
  embed.add_field(name="Country", value="country", inline=True)
  embed.add_field(name="Account Age", value="", inline=True)
  embed.add_field(name="Check Account", value="", inline=True)
  embed.add_field(name="Join Date", value=".", inline=True)
  embed.add_field(name="Game", value="", inline=True)
  await ctx.send(embed=embed)

# Run the bot
bot.run("YOUR_BOT_TOKEN")
