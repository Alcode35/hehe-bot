from discord.ext import commands
import discord

class BanCog(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(moderate_members = True)
    async def ban(self, ctx:commands.Context, member:discord.Member, *r):
        reason = ""

        for word in r:
            reason = reason + word + " "
        
        await discord.Member.ban(member, reason = reason)

        banEmbed = discord.Embed(title = "Ban:", timestamp = discord.utils.utcnow(), color = 0x00FF00)

        banEmbed.add_field(name = "Member", value = member.mention, inline = False)

        banEmbed.add_field(name = "Reason:", value = reason, inline = False)

        await ctx.reply(embed = banEmbed)

async def setup(bot: commands.Bot):
    await bot.add_cog(BanCog(bot))