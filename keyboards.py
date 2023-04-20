from telebot import types


def main_reply_menu():
    # Создаем кнопки первого уровня
    button1 = types.KeyboardButton('Новостная лента')
    button2 = types.KeyboardButton('Подписка на новости')
    button3 = types.KeyboardButton('Настройки')

    main_menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    return main_menu.row(button1, button2, button3)


def newsfeed_reply_menu():
    # Создаем кнопки второго уровня
    find_news = types.KeyboardButton('Поиск новости')
    news_feed = types.KeyboardButton('Лента новостей')
    go_back = types.KeyboardButton('Назад')

    submenu1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    return submenu1.row(find_news, news_feed, go_back)


def settings_reply_menu():
    # Создаем кнопки третьего уровня
    change_lang = types.KeyboardButton('Изменить язык')
    change_fav_categories = types.KeyboardButton('Изменить любимые категории')
    go_back = types.KeyboardButton('Назад')

    # Создаем меню подкнопок третьего уровня
    submenu3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    return submenu3.row(change_lang, change_fav_categories, go_back)

