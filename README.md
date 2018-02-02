# Telegram Bot for Pizzeria

The main task of this project is create Bot for Pizzeria

### The service features
- Catalog is loaded from DB
- Product is editable from web page for admins

### Attention!
Below parametrs declared as environment variables, don't forget to set up:
1. **os.environ['BOT_TOKEN']**(set up bot token for  to access the HTTP API)
2. **os.getenv('USERNAME')**, **os.getenv('USER_PASSWORD')**
(set up username and password for disable anonymous user)
3. **os.environ['DATABASE_URL']**(set up the database URI that should be used for the connection)


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
