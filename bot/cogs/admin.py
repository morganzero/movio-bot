from discord.ext import commands
from db import add_product_role_mapping, get_all_product_role_mappings, remove_product_role_mapping

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="addproductmap")
    @commands.has_permissions(administrator=True)
    async def add_product_map(self, ctx, *, args):
        try:
            parts = dict(part.split(":") for part in args.split('"') if ":" in part)
            product = parts.get("product", "").strip()
            role = parts.get("role", "").strip()

            if not product or not role:
                await ctx.send("Usage: `!addproductmap product:\"Product Name\" role:\"Role Name\"`")
                return

            add_product_role_mapping(product, role)
            await ctx.send(f"✅ Mapped product `{product}` → role `{role}`")
        except Exception as e:
            await ctx.send(f"❌ Failed to map product: {e}")

    @commands.command(name="listproductmaps")
    @commands.has_permissions(administrator=True)
    async def list_product_maps(self, ctx):
        mappings = get_all_product_role_mappings()
        if not mappings:
            await ctx.send("No product-role mappings found.")
        else:
            msg = "\n".join([f"`{p}` → `{r}`" for p, r in mappings])
            await ctx.send(f"**Current product-role mappings:**\n{msg}")

    @commands.command(name="removeproductmap")
    @commands.has_permissions(administrator=True)
    async def remove_product_map(self, ctx, *, args):
        try:
            parts = dict(part.split(":") for part in args.split('"') if ":" in part)
            product = parts.get("product", "").strip()

            if not product:
                await ctx.send("Usage: `!removeproductmap product:\"Product Name\"`")
                return

            removed = remove_product_role_mapping(product)
            if removed:
                await ctx.send(f"🗑️ Removed mapping for product `{product}`")
            else:
                await ctx.send(f"⚠️ No mapping found for product `{product}`")
        except Exception as e:
            await ctx.send(f"❌ Failed to remove mapping: {e}")

async def setup(bot):
    await bot.add_cog(Admin(bot))
