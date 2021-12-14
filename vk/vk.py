from random import randrange
from vk_api.longpoll import VkLongPoll
from vk_api.vk_api import VkApi
from VK_token import group_token

vk_grp = VkApi(token=group_token)
longpoll = VkLongPoll(vk_grp)


def vk_msg(user_id, message, attachment=None, keyboard=None):
    vk_grp.method('messages.send', {'user_id': user_id, 'message': message,
                                    'attachment': attachment,
                                    'keyboard': keyboard,
                                    'random_id': randrange(10 ** 7)})


def get_vk(user_token):
    vk = Vk(token=user_token)
    return vk


def prepare_info(info_list):
    sex, year, city, relation = info_list
    if sex == 1:
        new_sex = 2
    elif sex == 2:
        new_sex = 1
    else:
        new_sex = 0

    if year is not None:
        year = year.split('.')[-1]

    if city is not None:
        city = city.get('title')

    return new_sex, year, city


class Vk(VkApi):
    def get_photo(self, user_id):
        photo_list = []
        photos_json = self.method('photos.get', {'owner_id': user_id, 'album_id': 'profile', 'extended': 1,
                                                 'count': '100', 'photo_sizes': 1})
        for item in photos_json['items']:
            weight = item['likes']['count'] + item['comments']['count'] * 1.5
            photo_list.append([round(weight), f'photo{user_id}_{item["id"]}'])
        lst = sorted(photo_list, key=lambda x: x[0], reverse=True)[:3]
        res = [i[1] for i in lst]
        print(res)
        return res

    def user_info(self, user_id):
        info = self.method('users.get', {'user_id': user_id, 'fields': 'bdate, sex, city, relation'})[0]
        res = [info.get('sex'), info.get('bdate'), info.get('city'), info.get('relation')]
        return res

    def is_closed(self, user_id):
        info = self.method('users.get', {'user_id': user_id})[0]
        return info.get('is_closed')

    def search_users(self, info_list):
        info = prepare_info(info_list)
        sex, year, city = info
        res = self.method('users.search',
                          {'sex': sex, 'status': 6, 'birth_year': year, 'hometown': city, 'has_photo': 1})
        return res

