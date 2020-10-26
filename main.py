import telepot
import config


token = config.API_TOKEN
TelegramBot = telepot.Bot(token)
print(TelegramBot.getMe())