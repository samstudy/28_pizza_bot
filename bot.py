import telebot
from jinja2 import Template
from os import getenv
from create_db import session, Pizza

# the token below is not actual, you need to register a new one
TOKEN = '483199818:AAGmOEkN3QilQ9YgVMkoXsi0IfsIaV0Tn1w'
if not TOKEN:
    raise Exception('BOT_TOKEN should be specified')

bot = telebot.TeleBot(TOKEN)

with open('templates/catalog.md', 'r') as catalog_file:
    catalog_tmpl = Template(catalog_file.read())

with open('templates/greetings.md', 'r') as greetings_file:
    greetings_tmpl = Template(greetings_file.read())


@bot.message_handler(commands=['start'])
def greet(message):
    bot.send_message(message.chat.id, greetings_tmpl.render())


@bot.message_handler(commands=['menu'])
def show_catalog(message):
    catalog = session.query(Pizza).all()
    bot.send_message(message.chat.id, catalog_tmpl.render(
        catalog=catalog), parse_mode='Markdown')


if __name__ == '__main__':
    bot.polling(none_stop=True)
