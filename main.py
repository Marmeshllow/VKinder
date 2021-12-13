from vk_api.longpoll import VkEventType
from vk.vk import get_vk, vk_msg, longpoll
from VK_token import user_token


def listen():
    user = get_vk(user_token)
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
                photo = user.get_photo(people[0].get('id'))
                vk_msg(event.user_id, 'Лови', attachment=','.join(photo))   # Прикрепить ссылку
            else:
                vk_msg(event.user_id, "Не поняла вашего ответа...")


if __name__ == '__main__':
    listen()



