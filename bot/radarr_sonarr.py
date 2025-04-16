import aiohttp
import os

RADARR_URL = os.getenv("RADARR_URL")
RADARR_API_KEY = os.getenv("RADARR_API_KEY")
SONARR_URL = os.getenv("SONARR_URL")
SONARR_API_KEY = os.getenv("SONARR_API_KEY")

async def search_radarr_movie(query):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{RADARR_URL}/api/v3/movie/lookup?term={query}",
                               headers={"X-Api-Key": RADARR_API_KEY}) as resp:
            return await resp.json()

async def get_existing_movies():
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{RADARR_URL}/api/v3/movie", headers={"X-Api-Key": RADARR_API_KEY}) as resp:
            return await resp.json()

async def add_movie(movie_data):
    async with aiohttp.ClientSession() as session:
        async with session.post(f"{RADARR_URL}/api/v3/movie",
                                headers={"X-Api-Key": RADARR_API_KEY, "Content-Type": "application/json"},
                                json=movie_data) as resp:
            return await resp.json()

async def search_sonarr_series(query):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{SONARR_URL}/api/v3/series/lookup?term={query}",
                               headers={"X-Api-Key": SONARR_API_KEY}) as resp:
            return await resp.json()

async def get_existing_series():
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{SONARR_URL}/api/v3/series", headers={"X-Api-Key": SONARR_API_KEY}) as resp:
            return await resp.json()

async def add_series(series_data):
    async with aiohttp.ClientSession() as session:
        async with session.post(f"{SONARR_URL}/api/v3/series",
                                headers={"X-Api-Key": SONARR_API_KEY, "Content-Type": "application/json"},
                                json=series_data) as resp:
            return await resp.json()
