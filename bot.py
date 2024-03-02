from telebot import TeleBot, types
from telebot.types import Message


bot = TeleBot("6878848160:AAH6QkZs5ecP8gxg7Ym9IxZcpj3uUdVYpns")


def start_bot_polling():
    @bot.message_handler(commands=["start"])
    def start(message: Message):
        chat_id = message.chat.id
        name = message.from_user.full_name
        markup = types.InlineKeyboardMarkup(row_width=2)
        itembtn1 = types.InlineKeyboardButton('👍', callback_data='like')
        itembtn2 = types.InlineKeyboardButton('👎', callback_data='dislike')
        markup.add(itembtn1, itembtn2)
        bot.send_message(chat_id, f"Assalomu alaykum {name} ")
        bot.send_message(message.chat.id, "Tanlang:", reply_markup=markup)

        print(message.chat.id)

    @bot.message_handler(content_types=["text", "photo", "animation", "video", "gif", "emoji"])
    def eco_text(message: Message):
        group_chat_id = -1002042393767
        chat_id = message.chat.id
        bot.copy_message(group_chat_id, chat_id, message.message_id)

    liked_count = {}

    @bot.callback_query_handler(func=lambda call: True)
    def callback_inline(call):
        if call.data == "like":
            user_id = call.from_user.id
            liked_count[user_id] = liked_count.get(user_id, 0) + 1
            bot.answer_callback_query(call.id, "Siz bu xabarni yoqtirgansiz")
        elif call.data == "dislike":
            bot.answer_callback_query(call.id, "Siz bu xabarni yoqmayapsiz")

    bot.polling()
