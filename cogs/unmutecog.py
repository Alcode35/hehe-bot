from discord.ext import commands
import discord

class UnmuteCog(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(moderate_members = True)
    async def unmute(self, ctx: commands.Context, member: discord.Member, *r): 
        reason = ""

        for word in r:
            reason = reason + word + " "

        await discord.Member.timeout(member, None, reason = reason)

        unmuteEmbed = discord.Embed(title = f"Unute:", timestamp = discord.utils.utcnow(), color = 0x00FF00)

        unmuteEmbed.add_field(name = "Member:", value = member.mention, inline = False)

        unmuteEmbed.add_field(name = "Reason:", value = reason, inline = False)

        await ctx.reply(embed = unmuteEmbed)

async def setup(bot: commands.Bot):
    await bot.add_cog(UnmuteCog(bot))