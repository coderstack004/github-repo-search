import telebot
import requests

bot = telebot.TeleBot("5191410493:AAH-Foos-YyVYlPIMhsQNmpX7EEkphUvwT0")

users = 0
added = None

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.from_user.id, f"Привет {message.from_user.first_name}. Добро пожаловать в поисковый бот Github Repository! Теперь введите имя репозитория, который вы хотите:")
    with open('users.txt', 'r') as f:
        if str(message.from_user.id) in f.read():
            added = True
        else:
            added = False

    with open('users.txt', 'a') as f:
        if added == False:
            f.write(str(message.from_user.id) + '\n')

@bot.message_handler(commands=['count'])
def send_welcome(message):
    users = len(open('users.txt', 'r').readlines())
    bot.reply_to(message, f"Количество пользователей: {users}")

@bot.message_handler()
def search(message):
    response = requests.get(f'https://api.github.com/search/repositories?q={message.text}&per_page=80')
    for i in response.json()['items']:
        bot.send_message(message.chat.id, f'{i["html_url"]}\n{i["description"]}')

if __name__ == "__main__":
    bot.polling()