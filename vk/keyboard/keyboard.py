from vk_api.keyboard import VkKeyboard, VkKeyboardColor


def get_keyboard():
    keyboard = VkKeyboard(one_time=False, inline=True)
    keyboard.add_button('Быстрый поиск', VkKeyboardColor.NEGATIVE)
    keyboard.add_button('Расширеный поиск', VkKeyboardColor.PRIMARY)
    return keyboard.get_keyboard()


def get_keyboard_gender():
    keyboard = VkKeyboard(one_time=False, inline=True)
    keyboard.add_button('Мужчину', VkKeyboardColor.NEGATIVE)
    keyboard.add_button('Женщину', VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Не важно', VkKeyboardColor.SECONDARY)
    return keyboard.get_keyboard()


def get_keyboard_age():
    keyboard = VkKeyboard(one_time=False, inline=True)
    keyboard.add_button('18-25', VkKeyboardColor.NEGATIVE)
    keyboard.add_button('26-30', VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('31-40', VkKeyboardColor.POSITIVE)
    keyboard.add_button('41+', VkKeyboardColor.SECONDARY)
    return keyboard.get_keyboard()


def get_keyboard_continue():
    keyboard = VkKeyboard(one_time=False, inline=True)
    keyboard.add_button('Назад в меню', VkKeyboardColor.NEGATIVE)
    keyboard.add_button('Дальше', VkKeyboardColor.SECONDARY)
    return keyboard.get_keyboard()