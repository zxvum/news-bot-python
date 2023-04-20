import telebot
from telebot import types
import config
from keyboards import main_reply_menu, newsfeed_reply_menu, settings_reply_menu
from news_api import get_article

bot = telebot.TeleBot(config.TELEGRAM_BOT_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(msg):
    bot.reply_to(msg, f"Howdy, {msg.chat.username}! Я дал тебе навигационное меню, следуй ему!",
                 reply_markup=main_reply_menu())


@bot.message_handler(func=lambda message: True)
def handle_main_menu(message: types.Message):
    if message.text == 'Новостная лента':
        # Отправляем меню подкнопок первого уровня
        bot.send_message(message.chat.id, 'Выберите действие:', reply_markup=newsfeed_reply_menu())
    elif message.text == 'Подписка на новости':
        pass
    elif message.text == 'Настройки':
        # Отправляем меню подкнопок третьего уровня
        bot.send_message(message.chat.id, 'Выберите действие:', reply_markup=settings_reply_menu())


# Обработчик выбора кнопок подкнопок первого уровня
@bot.message_handler(func=lambda message: True)
def handle_submenu1(message: types.Message):
    if message.text == 'Поиск новости':
        # Выполняем действие для Поиска новости
        pass
    elif message.text == 'Лента новостей':
        later(msg=message)
    elif message.text == 'Назад':
        # Отправляем главное меню
        bot.send_message(message.chat.id, 'Выберте действие:', reply_markup=main_reply_menu())


@bot.message_handler(func=lambda message: True)
def handle_submenu3(message: types.Message):
    if message.text == 'Изменить язык':
        # Выполняем действие для Изменения языка
        pass
    elif message.text == 'Изменить любимые категории':
        # Выполняем действие для Изменения любимых категорий
        pass
    elif message.text == 'Назад':
        # Отправляем главное меню
        bot.send_message(message.chat.id, 'Выберите действие:', reply_markup=main_reply_menu())


@bot.message_handler(commands=['news'])
def news_finder(msg):
    topic = ' '.join(msg.text.split()[1:])
    if not topic:
        return bot.reply_to(msg,
                            'Вы неверно используете команду, используйте ее в формате /news (тема сообщения). Тема сообщения без скобочен')
    article = get_article(query=topic)
    if not article:
        return bot.reply_to(msg, 'Статья по такому названию не найдена!')

    title = article['title']
    description = article['description']
    img = article['urlToImage']
    article_url = article['url']

    text = f"Title: {title} \n Content: {description} \n [Читать дальше...]({article_url})"

    return bot.send_photo(msg.chat.id, photo=img, caption=text, parse_mode="markdown")


# Обработчик непонятных команд
@bot.message_handler(func=lambda message: True)
def handle_unknown_command(message: telebot.types.Message):
    """
    Обработчик для непонятных команд
    """
    bot.reply_to(message, "Извините, я вас не совсем понял, прочитайте текст чуть выше!")


def later(msg):
    bot.send_message(msg.chat.id, 'Скоро...')


bot.polling(none_stop=True)
