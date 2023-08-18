from discord.ext import commands
import discord

class UnbanCog(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(moderate_members = True)
    async def unban(self, ctx:commands.Context, member:discord.Member, *r):
        reason = ""

        for word in r:
            reason = reason + word + " "

        await ctx.guild.unban(member, reason = reason)

        unbanEmbed = discord.Embed(title = "Unban:", timestamp = discord.utils.utcnow(), color = 0x00FF00)

        unbanEmbed.add_field(name = "Member", value = member.mention, inline = False)

        unbanEmbed.add_field(name = "Reason:", value = reason, inline = False)

        await ctx.reply(embed = unbanEmbed)

async def setup(bot: commands.Bot):
    await bot.add_cog(UnbanCog(bot))