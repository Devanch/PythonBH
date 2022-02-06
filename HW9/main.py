import urllib.request
import json
import time

url = "https://jsonplaceholder.typicode.com"
# - /users - все пользователи
# - /users/1/posts - посты пользователя с id 1
# - /users/1/albums - aльбомы пользователя с id 1
# - /users/1/todos - задачи пользователя с id 1
# - /posts/1/comments - комментарии под постом с id 1
# - /albums/1/photos - фотографии в альбоме с id 1


def load_data(val_url):
    cur_data = urllib.request.urlopen(val_url).read()
    output = json.loads(cur_data)
    print(output)
    return output


start_time = time.time()
users = load_data(url + "/users")


for user in users:
    user_id = user['id']

    posts = load_data(url + "/users/" + str(user_id) + "/posts")
    for post in posts:
        post_id = post['id']
        load_data(url + "/posts/" + str(post_id) + "/comments")

    albums = load_data(url + "/users/" + str(user_id) + "/albums")
    for album in albums:
        album_id = album['id']
        load_data(url + "/albums/" + str(album_id) + "/photos")

    load_data(url + "/users/" + str(user_id) + "/todos")


print("Время выполнения: %.3f секунд" % (time.time() - start_time))