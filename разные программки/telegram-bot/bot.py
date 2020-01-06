'''
Простой бот для ответа на сообщения Telegram.
Сначала определяется несколько функций-обработчиков. Затем эти функции передаются
Диспетчер и зарегистрированы на своих местах.
Затем бот запускается и работает, пока мы не нажмем Ctrl-C в командной строке.
Использование:
Базовый пример Echobot, повторяет сообщения.
Нажмите Ctrl-C в командной строке или отправьте сигнал процессу, чтобы остановить
бот.
'''

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Включить ведение журнала
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Определите несколько обработчиков команд. Они обычно принимают два аргумента обновления и
# контекст. Обработчики ошибок также получают объект TelegramError с ошибкой.
def start(update, context):
    """Отправьте сообщение при вводе команды / запуска."""
    update.message.reply_text('Hi!')


def help(update, context):
    """Отправьте сообщение при вводе команды / справки."""
    update.message.reply_text('Help!')


def echo(update, context):
    """ Эхо сообщения пользователя. """
    update.message.reply_text(update.message.text)


def error(update, context):
    """Ошибки журнала, вызванные обновлениями."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Запусти бота."""
    # Создание Updater и передать его маркер вашего бота.
    # Обязательно установите use_context = True, чтобы использовать новые контекстные обратные вызовы
    # Сообщение версия 12 это больше не будет необходимости
    updater = Updater("TOKEN", use_context=True)

    # Получить диспетчер для регистрации обработчиков
    dp = updater.dispatcher

    # на разные команды - ответьте в Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # на некоманде т.е. сообщение - повторить сообщение в Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # регистрировать все ошибки
    dp.add_error_handler(error)

    # Запустить бот
    updater.start_polling()

    # Запускать бот, пока вы не нажмете Ctrl-C или процесс не получит SIGINT,
    # SIGTERM или SIGABRT. Это следует использовать большую часть времени, так как
    # start_polling () неблокирует и корректно остановит бота.
    updater.idle()


if __name__ == '__main__':
    main()