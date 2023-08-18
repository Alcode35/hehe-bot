from discord.ext import commands
import discord
import datetime

class MuteCog(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(moderate_members = True)
    async def mute(self, ctx: commands.Context, member: discord.Member, d:int, h:int, m:int, *r): 
        reason = ""

        for word in r:
            reason = reason + word + " "

        time = datetime.timedelta(days = d, hours = h, minutes = m)

        timeValue:str = str(d) + " days, " + str(h) + " hours, and " + str(m) + " minutes."

        await discord.Member.timeout(member, time, reason = reason)

        muteEmbed = discord.Embed(title = f"Mute:", timestamp = discord.utils.utcnow(), color = 0xFF0000)

        muteEmbed.add_field(name = "Member:", value = member.mention, inline = False)

        muteEmbed.add_field(name = "Time:", value = timeValue, inline = False)

        muteEmbed.add_field(name = "Reason:", value = reason, inline = False)

        await ctx.reply(embed = muteEmbed)

async def setup(bot: commands.Bot):
    await bot.add_cog(MuteCog(bot))