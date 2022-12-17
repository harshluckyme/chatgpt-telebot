import openai
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Set up the OpenAI API client
openai.api_key = "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"

# Set up the Telegram bot
updater = Updater(token="5574739585:AAE1mTxTxNXEiK3wUvqfmkVt4dATpm88bxw", use_context=True)
dispatcher = updater.dispatcher

def handle_message(update, context):
    # Get the user's message
    message = update.message.text
    # Use the OpenAI API to generate a response
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=message,
        max_tokens=1024,
        temperature=0.5,
    )
    # Check if the 'text' attribute is present in the response
    print(message)
    print(response)
    context.bot.send_message(chat_id=update.message.chat_id, text=response.choices[0].text)

# Add a message handler to the dispatcher
message_handler = MessageHandler(Filters.text, handle_message)
dispatcher.add_handler(message_handler)

updater.start_polling()
