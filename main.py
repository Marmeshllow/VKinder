from vk_api.longpoll import VkEventType
from vk.vk import get_vk, vk_msg, longpoll
from VK_token import user_token
from bd.query import is_in_db, add_in_db
user = get_vk(user_token)


def get_couple(user_id, people: list):
    for el in people:
        if is_in_db(user_id, el['id']) or user.is_closed(el['id']):
            print(f'{el["id"]} есть в базе или закрытый профиль')
        else:
            photo = user.get_photo(el["id"])
            vk_msg(user_id, 'Лови', attachment=','.join(photo))
            add_in_db(user_id, el["id"])
            return


def listen():
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            request = event.text.lower()
            if request == "привет":
                vk_msg(event.user_id, 'Привет')
            elif request == "пока":
                vk_msg(event.user_id, "Пока(("),
            elif request == "быстрый поиск":
                vk_msg(event.user_id, "Ищем...")
                info = user.user_info(event.user_id)
                people = user.search_users(info)['items']   # Выдавать по одному + подрубить базу
                get_couple(event.user_id, people)
                # photo = user.get_photo(people[0].get('id'))
                #vk_msg(event.user_id, 'Лови', attachment=','.join(photo))   # Прикрепить ссылку
            else:
                vk_msg(event.user_id, "Не поняла вашего ответа...")


if __name__ == '__main__':
    listen()
# берем список юзеров. кидаем его в функцию1. функция1 чекает есть ли чел с таким id и парой в бд. если нет то выдаем пару.
# если да то некст

