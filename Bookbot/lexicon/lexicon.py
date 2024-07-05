Harry = '<a href="https://harrypotter.fandom.com/ru/wiki/Гарри_Поттер">Гарри Поттер</a>'
Hermiona = '<a href="https://harrypotter.fandom.com/ru/wiki/Гермиона_Грейнджер">Гермиона Грейнджер</a>'
Ron = '<a href="https://harrypotter.fandom.com/ru/wiki/Рон_Уизли">Рон Уизли</a>'
Dambldor = '<a href="https://harrypotter.fandom.com/ru/wiki/Альбус_Дамблдор">Альбус Дамблдор</a>'

LEXICON: dict[str, str] = {
    'forward': '>>',
    'backward': '<<',
    '/start': '<b>Добро пожаловать в волшебный мир Гарри Поттера!</b>\n\nПеред Вами книга Гарри Поттер и Философский камень на английской языке!\n\nЧтобы ознакомиться с инструкцией - наберите /help',
    '/help': '<b>Это бот-читалка</b>\n\nДоступные команды:\n\n/beginning - '
             'перейти в начало книги\n/continue - продолжить '
             'чтение\n/bookmarks - посмотреть список закладок\n/help - '
             'справка по работе бота\n\nЧтобы сохранить закладку - '
             f'нажмите на кнопку с номером страницы\n\n<b>Посмотреть и почитать о героях книги можно, нажав на имя героя ниже: </b>\n\n{Harry}\n\n{Hermiona}\n\n{Ron}\n\n{Dambldor}\n\n<b>Приятного чтения!</b>',
    '/bookmarks': '<b>Это список ваших закладок:</b>',
    'edit_bookmarks': '<b>Редактировать закладки</b>',
    'edit_bookmarks_button': '❌ РЕДАКТИРОВАТЬ',
    'del': '❌',
    'cancel': 'ОТМЕНИТЬ',
    'no_bookmarks': 'У вас пока нет ни одной закладки.\n\nЧтобы '
                    'добавить страницу в закладки - во время чтения '
                    'книги нажмите на кнопку с номером этой '
                    'страницы\n\n/continue - продолжить чтение',
    'cancel_text': '/continue - продолжить чтение'
}

LEXICON_COMMANDS: dict[str, str] = {
    '/beginning': 'В начало книги',
    '/continue': 'Продолжить чтение',
    '/bookmarks': 'Мои закладки',
    '/help': 'Справка по работе бота'
}