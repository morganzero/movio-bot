from fastapi import FastAPI, Request
import discord
from db import get_discord_id_by_email

app = FastAPI()
discord_client: discord.Client = None

@app.post("/api/whmcs-webhook")
async def handle_webhook(request: Request):
    data = await request.json()
    event = data.get("event")
    email = data.get("client", {}).get("email")
    discord_id = get_discord_id_by_email(email)

    if not discord_id:
        return {"status": "no user linked"}

    user = await discord_client.fetch_user(int(discord_id))

    messages = {
        "InvoiceCreated": "A new invoice has been created.",
        "InvoicePaid": "Thank you! Your invoice has been paid.",
        "ServiceSuspended": "Your service has been suspended.",
        "ServiceUnsuspended": "Your service has been unsuspended."
    }

    if event in messages:
        await user.send(messages[event])

    return {"status": "notified"}