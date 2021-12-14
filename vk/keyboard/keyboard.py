from vk_api.keyboard import VkKeyboard, VkKeyboardColor

def get_keyboard():
    keyboard = VkKeyboard(one_time=False, inline=True)
    keyboard.add_button('Быстрый поиск', VkKeyboardColor.NEGATIVE)
    keyboard.add_line()
    keyboard.add_button('Разширеный поиск', VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('???', VkKeyboardColor.POSITIVE)
    keyboard.add_button('???', VkKeyboardColor.SECONDARY)
    return keyboard.get_keyboard()


