from discord.ext import commands
from discord import app_commands, Interaction, SelectOption, Select, Button, ButtonStyle, ui, Embed
from radarr_sonarr import *

class Request(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="request_movie", description="Search and request a movie")
    async def request_movie(self, interaction: Interaction, title: str):
        await interaction.response.defer()
        movies = await search_radarr_movie(title)
        if not movies:
            await interaction.followup.send("No results found.")
            return

        options = [SelectOption(label=movie["title"], value=str(i)) for i, movie in enumerate(movies[:5])]

        class MovieSelect(ui.Select):
            def __init__(self):
                super().__init__(placeholder="Choose a movie", options=options)

            async def callback(self, select_interaction: Interaction):
                selected = movies[int(self.values[0])]
                existing = await get_existing_movies()
                match = next((m for m in existing if m["title"] == selected["title"]), None)

                if match:
                    status = "available" if match.get("downloaded", False) else "notify me"
                    await select_interaction.response.send_message(f"**{selected['title']}** is already {status}.")
                else:
                    class ConfirmButton(ui.View):
                        @ui.button(label="Request", style=ButtonStyle.primary)
                        async def request(self, button, btn_interaction):
                            payload = {
                                "title": selected["title"],
                                "qualityProfileId": 1,
                                "titleSlug": selected["titleSlug"],
                                "images": selected["images"],
                                "tmdbId": selected["tmdbId"],
                                "year": selected["year"],
                                "rootFolderPath": "/movies",
                                "monitored": True,
                                "addOptions": {"searchForMovie": True}
                            }
                            await add_movie(payload)
                            await btn_interaction.response.send_message(f"Requested **{selected['title']}**")
                    await select_interaction.response.send_message(f"**{selected['title']}** is not in the library.", view=ConfirmButton())

        view = ui.View()
        view.add_item(MovieSelect())
        await interaction.followup.send("Select a movie to proceed:", view=view)

async def setup(bot):
    await bot.add_cog(Request(bot))