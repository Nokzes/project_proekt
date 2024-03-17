import json
from vkbottle import GroupEventType, Keyboard, EMPTY_KEYBOARD, Text, GroupTypes, KeyboardButtonColor
from vkbottle.bot import Message, BotLabeler, MessageEvent, Bot
import proekt.utils as utils
menu = BotLabeler()

@menu.message(payload={'menu': 'menu'})
@menu.message(text=['Меню', 'меню', 'vty.', 'Vty.'])
async def menu_base(message: Message):
    keyboard = EMPTY_KEYBOARD
    keyboard = Keyboard()
    keyboard.add(Text('Персонаж', {'menu': 'char'}), color=KeyboardButtonColor.POSITIVE)
    keyboard.row()
    keyboard.add(Text('Монстры', {'menu': 'monsters'}), color=KeyboardButtonColor.NEGATIVE)
    keyboard.row()
    keyboard.add(Text("Мировые боссы", {'menu': 'bosses'}), color=KeyboardButtonColor.NEGATIVE)
    keyboard.row()
    # keyboard.add(Text('Инвентарь', {'menu': 'inv'}), color=KeyboardButtonColor.POSITIVE)
    # keyboard.row()
    keyboard.add(Text('Игры', {'menu': 'casino'}))
    keyboard.row()
    keyboard.add(Text('Дополнительная информация', {'menu': 'info'}))
    await message.answer('Вы в главном меню', keyboard=keyboard)



@menu.message(payload={'menu': 'info'})
async def info(message: Message):
    await message.answer("Помощь в тестировке бота оказал [https://vk.com/rimtar|Ратмир]")



