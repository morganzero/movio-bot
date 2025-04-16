import json
import discord

with open("product_roles.json", "r") as f:
    PRODUCT_ROLE_MAP = json.load(f)

async def assign_roles_from_products(products, member: discord.Member):
    guild = member.guild
    for product in products:
        name = product.get("name")
        if name in PRODUCT_ROLE_MAP:
            role_name = PRODUCT_ROLE_MAP[name]
            role = discord.utils.get(guild.roles, name=role_name)
            if role and role not in member.roles:
                await member.add_roles(role)
                print(f"Assigned role {role_name} to {member.display_name}")
