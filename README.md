readme_content = """\
# Discord WHMCS Integration Bot

A fully docker-compatible Discord bot that integrates with WHMCS for product-role mapping, invoice tracking, and media requests via Radarr/Sonarr.

---

## ✅ Features

- Welcome DM flow with rule approval
- WHMCS product lookup + role assignment
- Admin commands to manage product-role links:
  - `!addproductmap product:"X" role:"Y"`
  - `!listproductmaps`
  - `!removeproductmap product:"X"`
- Radarr/Sonarr `/request` integration (WIP)
- WHMCS webhook listener via FastAPI
- SQLite database (persistent)
- Slash and prefix command support

---

## 🚀 Quick Setup

### 1. Clone repo

```bash
git clone https://github.com/yourname/discord-whmcs-bot.git
cd discord-whmcs-bot
