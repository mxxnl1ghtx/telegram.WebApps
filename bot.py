from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
import json
from config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)

# Информация о боте
BOT_NAME = "Антонио"


# Обработка команды /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    # Создание клавиатуры
    markup = types.ReplyKeyboardMarkup()

    # Добавление кнопок клавиатуры
    markup.add(types.ReplyKeyboardButton('Заказать еду', web_app=WebAppInfo(url='https://mxxnl1ghtx.github.io/telegram.WebApps/')))

    # Привествие бота
    await message.answer(f"Приветствую, {message.from_user.full_name}!\nМеня зовут {BOT_NAME} и я твой бот-ассистент по заказу еды через интернет. Давай приступим! 🍕\n\nНажми на кнопку снизу чтобы закказать себе вкусной еды!", reply_markup=markup)

# Обработка команды /help
@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.answer('Список команд:\n/start - Главное меню\n/help - Справка\n/roll_dice - Кинуть кубик\n/play_casino - Сыграть в казино')

@dp.message_handler(commands=['roll_dice'])
async def roll_dice(message: types.Message):
    await bot.send_dice(chat_id=message.chat.id, emoji='🎲')

@dp.message_handler(commands=['play_casino'])
async def play_casino(message: types.Message):
    await bot.send_dice(chat_id=message.chat.id, emoji='🎰')

@dp.message_handler(lambda message: message.text.lower() == 'привет')
async def hello(message: types.Message):
    await message.answer("Привет!")

@dp.message_handler()
async def what(message: types.Message):
    await message.answer("Я не понимаю чего вы от меня хотите.\n\nДля помощи: /help")

@dp.message_handler(content_types=['web_app_data'])
async def web_app(message: types.Message):
    parsed_data = json.loads(message.web_app_data.data)
    message = ''
    for i, item in enumerate(parsed_data['items'], start=1):
        postion = int(item['id'].replace('item', ''))
        message += f'Позиция {postion}\n'
        message == f'Стоимость: {item['price']}\n'

    message += f'Общая стоимость товаров: {parsed_data['totalPrice']}'

    await bot.send_message(message)

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)