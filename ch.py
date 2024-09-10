from telethon.sync import TelegramClient
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.types import InputUser
from telethon.errors import SessionPasswordNeededError
import random
import time

# Ваши данные
api_id = '23074483'
api_hash = '5a66e1a234fb820bb52376ba360a162f'
phone = '+992117700176'
username = '@wmsfhack'

# Функция для получения случайного пользователя из файла
def get_random_user(filename):
    with open(filename, 'r') as file:
        usernames = file.read().splitlines()
    return random.choice(usernames)

# Функция для добавления пользователя в канал
async def add_user_to_channel(client, user_to_add, channel_id):
    try:
        # Получаем пользователя по юзернейму
        user = await client.get_entity(user_to_add)
        # Добавляем пользователя в канал
        await client(AddChatUserRequest(
            chat_id=channel_id,
            user_id=InputUser(
                user_id=user.id,
                access_hash=user.access_hash
            ),
            fwd_limit=10  # Ограничение на количество пересылаемых сообщений
        ))
        print(f'Пользователь {user_to_add} добавлен в канал {channel_id}')
    except Exception as e:
        print(f'Ошибка при добавлении пользователя {user_to_add} в канал {channel_id}: {e}')

# Функция для добавления пользователей в конкретные каналы
async def add_users_to_channels(client, channel_ids, filename):
    while True:
        for channel_id in channel_ids:
            user_to_add = get_random_user(filename)
            await add_user_to_channel(client, user_to_add, channel_id)
            time.sleep(12)  # Ожидание 12 секунд перед добавлением следующего пользователя

# Запуск клиента
async def main():
    async with TelegramClient(username, api_id, api_hash) as client:
        await client.start(phone)
        await add_users_to_channels(client, [-1001982592202], "../../parser & inviter/users(05.05.2024 09_49).txt")

# Запуск асинхронного цикла событий
import asyncio
asyncio.run(main())