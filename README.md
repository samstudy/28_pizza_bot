# Telegram Bot for Pizzeria

The main task of this project is create Bot for Pizzeria

### The service features
- Catalog is loaded from DB
- Product is editable from web page for admins

## How to Use

Step 1. Register new telegram bot for development purposes, get the new token. [@BotFather](https://telegram.me/botfather)

Step 2. Install modules from requirement 

Step 3. Create DB and migrate catalog to DB

Step 4. Launch bot

Step 5. Launch server for web admin

Example of  launch on Linux, Python 3.5:

```
pip install -r requirements.txt
python3 create_db.py
python3 bot.py
python3 server.py

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
