import json
import time
import aiohttp
import asyncio

url: str = "https://jsonplaceholder.typicode.com"


# - /users - все пользователи
# - /users/1/posts - посты пользователя с id 1
# - /users/1/albums - aльбомы пользователя с id 1
# - /users/1/todos - задачи пользователя с id 1
# - /posts/1/comments - комментарии под постом с id 1
# - /albums/1/photos - фотографии в альбоме с id 1

# список задач для асинхронной загрузки данных
tasks = []


# Вычитываем все данные по одному пользователю
def load_user_data(session, user_id):
    val_url = url + "/users/" + str(user_id) + "/posts"
    tasks.append(asyncio.create_task(session.get(val_url)))

    val_url = url + "/users/" + str(user_id) + "/albums"
    tasks.append(asyncio.create_task(session.get(val_url)))

    val_url = url + "/users/" + str(user_id) + "/todos"
    tasks.append(asyncio.create_task(session.get(val_url)))


# Создаем отдельные задачи для каждого пользователя
def get_tasks(session, users):
    for user in users:
        user_id = user['id']
        cur_url = url + "/users/" + str(user_id) + "/posts"
        print('Working on url {}'.format(cur_url))
        load_user_data(session, user_id)


# Общий результат для выполнения всех задач
async def gather_data():
    val_url = url + "/users"
    async with aiohttp.ClientSession() as session:
        response = await session.get(val_url)
        users = await response.json()

        print('Список USERS:', users)
        get_tasks(session, users)
        responses = await asyncio.gather(*tasks)
        for response in responses:
            print(await response.json())


# Запускаем цикл работы и считаем время
start_time = time.time()
asyncio.get_event_loop().run_until_complete(gather_data())
print("Время выполнения: %.3f секунд" % (time.time() - start_time))
