from random import randrange
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from VK_token import user_token, group_token

vk_user = vk_api.VkApi(token=user_token)
vk = vk_api.VkApi(token=group_token)
longpoll = VkLongPoll(vk)


def get_photo(user_id):
    photo_list = []
    photos_json = vk_user.method('photos.get', {'owner_id': user_id, 'album_id': 'profile', 'extended': 1,
                                                'count': '100', 'photo_sizes': 1})
    for item in photos_json['items']:
        weight = item['likes']['count'] + item['comments']['count'] * 1.5
        photo_list.append([round(weight), f'{user_id}_{item["id"]}'])
    res = sorted(photo_list, key=lambda x: x[0], reverse=True)[:3]
    return res


def user_info(user_id):
    info = vk.method('users.get', {'user_id': user_id, 'fields': 'bdate, sex, city, relation'})[0]
    res = [info.get('sex'), info.get('bdate'), info.get('city'), info.get('relation')]
    print(res)
    return res


def send_msg(user_id, message, photo=None):
    if photo is not None:
        vk.method('messages.send', {'user_id': user_id, 'message': message,
                                    'attachment': f'photo{photo[0][1]},photo{photo[1][1]},photo{photo[2][1]}',
                                    'random_id': randrange(10 ** 7)})
    else:
        vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': randrange(10 ** 7)})


def listen():
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            request = event.text.lowwer()
            if request == "привет":
                #s = vk_user.method('users.search', {'age_from': 45, 'age_to': 60})  # в отдельный метод
                photo = get_photo('87878521')
                send_msg(event.user_id, 'Лови', photo=photo)

            elif request == "пока":
                send_msg(event.user_id, "Пока((")
            else:
                send_msg(event.user_id, "Не поняла вашего ответа...")



user_info('87878521')
info = user_info('43320396')
if info[2] is not None:
    city = info[2].get('title')
else:
    city = 'Москва'
# listen()
s = vk_user.method('users.search', {'sex': 1, 'status': 6, 'birth_year': 1996, 'hometown': city})
print(s)