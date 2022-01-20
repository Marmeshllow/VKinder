from vk_api.longpoll import VkEventType
from vk.vk import vk_msg, longpoll, get_couple, user, json_to_list
from vk.keyboard.keyboard import get_keyboard, get_keyboard_gender, get_keyboard_age


def listen():
    ad_info = [None, None, None]
    people = None
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            request = event.text.lower()
            if request == "привет":
                vk_msg(event.user_id, 'Привет.', keyboard=get_keyboard())
            elif request == "пока":
                vk_msg(event.user_id, "Пока(("),
            elif request == "быстрый поиск":
                vk_msg(event.user_id, "Ищем...")
                info = user.user_info(event.user_id)
                json_people = user.search_users(info)
                people = json_to_list(json_people)
                get_couple(event.user_id, people)
            elif request == "расширеный поиск":
                vk_msg(event.user_id, "Кого хочешь найти?", keyboard=get_keyboard_gender())
            elif request == "мужчину":
                ad_info[0] = 2
                vk_msg(event.user_id, "Предпочитаемый возраст", keyboard=get_keyboard_age())
            elif request == "женщину":
                ad_info[0] = 1
                vk_msg(event.user_id, "Предпочитаемый возраст", keyboard=get_keyboard_age())
            elif request == "не важно":
                ad_info[0] = 0
                vk_msg(event.user_id, "Предпочитаемый возраст", keyboard=get_keyboard_age())
            elif request == "18-25":
                ad_info[1] = (18, 25)
                vk_msg(event.user_id, "Город в котором будем искать. Перед названием города ОБЯЗАТЕЛЬНО"
                                      " поставь символ '#'\n Пример: #Москва")
            elif request == "26-30":
                ad_info[1] = (26, 30)
                vk_msg(event.user_id, "Город в котором будем искать. Перед названием города ОБЯЗАТЕЛЬНО"
                                      " поставь символ '#'\n Пример: #Москва")
            elif request == "31-40":
                ad_info[1] = (31, 40)
                vk_msg(event.user_id, "Город в котором будем искать. Перед названием города ОБЯЗАТЕЛЬНО"
                                      " поставь символ '#'\n Пример: #Москва")
            elif request == "41+":
                ad_info[1] = (41, 99)
                vk_msg(event.user_id, "Город в котором будем искать. Перед названием города ОБЯЗАТЕЛЬНО"
                                      " поставь символ '#'\n Пример: #Москва")
            elif request[0] == '#':
                ad_info[2] = request[1:]
                json_people = user.ad_search(ad_info)
                people = json_to_list(json_people)
                get_couple(event.user_id, people)
            elif request == "дальше" and people is not None:
                get_couple(event.user_id, people)
            elif request == "назад в меню":
                vk_msg(event.user_id, 'Выбери как будем искать', keyboard=get_keyboard())
            else:
                vk_msg(event.user_id, "Не поняла вашего ответа...")


if __name__ == '__main__':
    listen()
