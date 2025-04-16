from discord.ext import commands
from db import add_product_role_mapping

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(administrator=True)
    @commands.command(name="addproductmap")
    async def add_product_mapping(self, ctx, *, args):
        try:
            parts = dict(arg.split(":") for arg in args.split(" ") if ":" in arg)
            product = parts.get("product").strip("\" ")
            role = parts.get("role").strip("\" ")

            if not product or not role:
                raise ValueError

            add_product_role_mapping(product, role)
            await ctx.send(f"Mapped product '{product}' to role '{role}'.")
        except Exception:
            await ctx.send("Usage: !addproductmap product:\"Product Name\" role:\"Role Name\"")

async def setup(bot):
    await bot.add_cog(Admin(bot))
