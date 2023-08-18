from discord.ext import commands
import discord

class KickCog(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(moderate_members = True)
    async def kick(self, ctx:commands.Context, member:discord.Member, *r):
        reason = ""

        for word in r:
            reason = reason + word + " "
            
        await discord.Member.kick(member, reason = reason)

        kickEmbed = discord.Embed(title = "Kick:", timestamp = discord.utils.utcnow(), color = 0x00FF00)

        kickEmbed.add_field(name = "Member", value = member.mention, inline = False)

        kickEmbed.add_field(name = "Reason:", value = reason, inline = False)

        await ctx.reply(embed = kickEmbed)

async def setup(bot: commands.Bot):
    await bot.add_cog(KickCog(bot))