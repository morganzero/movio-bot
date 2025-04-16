import discord
from db import get_role_by_product

async def assign_roles_from_products(products, member: discord.Member):
    guild = member.guild
    for product in products:
        product_name = product.get("name")
        role_name = get_role_by_product(product_name)
        if role_name:
            role = discord.utils.get(guild.roles, name=role_name)
            if role and role not in member.roles:
                await member.add_roles(role)
                print(f"Assigned role '{role.name}' to {member.display_name}")