from random import randrange, shuffle
from vk_api.longpoll import VkLongPoll
from vk_api.vk_api import VkApi
from Settings import group_token, user_token
from bd.query import is_in_db, add_in_db, is_online
from vk.keyboard.keyboard import get_keyboard_continue


def json_to_list(response):
    result = []
    for el in response['items']:
        if not el['is_closed']:
            result.append(el)
    if len(result) > 0:
        shuffle(result)
    return result


def get_couple(user_id, people: list):
    for el in people:
        if is_online():
            if is_in_db(user_id, el['id']) or user.is_closed(el['id']):
                print(f'{el["id"]} есть в базе или закрытый профиль')
            else:
                photo = user.get_photo(el["id"])
                vk_msg(user_id, f'Лови\n vk.com/id{el["id"]}',
                       attachment=','.join(photo), keyboard=get_keyboard_continue())
                add_in_db(user_id, el["id"])
                return
        else:
            photo = user.get_photo(el["id"])
            vk_msg(user_id, f'База данных не доступна. Могут возникать повторы :(\nЛови\n'
                            f' vk.com/id{el["id"]}', attachment=','.join(photo), keyboard=get_keyboard_continue())
            return


def vk_msg(user_id, message, attachment=None, keyboard=None):
    vk_grp.method('messages.send', {'user_id': user_id, 'message': message,
                                    'attachment': attachment,
                                    'keyboard': keyboard,
                                    'random_id': randrange(10 ** 7)})


def get_vk(token):
    vk = Vk(token=token)
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
        res = self.method('users.search', {'sex': sex, 'status': 6, 'birth_year': year,
                                           'hometown': city, 'has_photo': 1, 'count': 500})
        return res

    def ad_search(self, info_list):
        res = self.method('users.search',
                          {'sex': info_list[0], 'status': 6, 'age_from': info_list[1][0], 'age_to': info_list[1][1],
                           'hometown': info_list[2], 'has_photo': 1, 'count': 500})
        return res


vk_grp = VkApi(token=group_token)
longpoll = VkLongPoll(vk_grp)
user = get_vk(user_token)
