import json
from vkbottle import GroupEventType, Keyboard, EMPTY_KEYBOARD, Text, GroupTypes, KeyboardButtonColor
from vkbottle.bot import Message, BotLabeler, MessageEvent, Bot
import proekt.utils as utils
char = BotLabeler()



@char.message(payload={'menu': 'char'})
async def character(message: Message):
    user_db = utils.get_user_by_id(message.from_id)
    user = json.loads(user_db.user)
    other = json.loads(user_db.other)
    lvl = json.loads(user_db.lvls)

    keyboard = EMPTY_KEYBOARD
    keyboard = Keyboard()
    keyboard.add(Text('Прокачка', {'char': 'lvl'}), color=KeyboardButtonColor.NEGATIVE)
    keyboard.row()
    keyboard.add(Text('Восстановить здоровье', {'char': "heall"}), color=KeyboardButtonColor.POSITIVE)
    keyboard.row()
    keyboard.add(Text('Обновить данные', {'menu': 'char'}))
    keyboard.add(Text('Меню', {'menu': 'menu'}))

    await message.answer(f"Профиль игрока {other['nick']}\n🆔{user_db.vk_id}\n"
                         f"Здоровье {user['cur_hp']}♥ / {user['hp']}♥\n"
                         f"Урон {user['cur_dmg']}🗡\n"
                         f"Золото {other['gold']}💰 Алмазы {other['diamond']}💎\n"
                         f"Уровень {user['lvl']}⭐ Опыт {user['exp']}/{lvl['char']}✨",
                         keyboard=keyboard, attachment='photo-223986632_456239021')


@char.message(payload={'char': 'lvl'})
async def lvl_up(message: Message):
    user_db = utils.get_user_by_id(message.from_id)
    user = json.loads(user_db.user)
    lvl = json.loads(user_db.lvls)

    keyboard = EMPTY_KEYBOARD
    keyboard = Keyboard()
    keyboard.add(Text("Прокачать здоровье", {'lvl': 'hp'}), color=KeyboardButtonColor.POSITIVE)
    keyboard.row()
    keyboard.add(Text("Прокачать урон", {'lvl': 'dmg'}), color=KeyboardButtonColor.NEGATIVE)
    keyboard.row()
    keyboard.add(Text('Меню', {'menu': 'menu'}))

    await message.answer(f"Выберите, что хотите прокачать\n"
                         f"Прокачка здоровья даёт {user['hp_lvl']*5}\n"
                         f"Уровень прокачки здоровья {user['hp_lvl']}\n"
                         f"Стоимость прокачки здоровья {lvl['hp']}💰\n\n"
                         f"Прокачка урона даёт {user['dmg_lvl']}\n"
                         f"Уровень прокачки урона {user['dmg_lvl']}\n"
                         f"Стоимость прокачки урона {lvl['dmg']}💰\n\n",

                         keyboard=keyboard)

@char.message(payload={'lvl': 'hp'})
async def hp_up(message: Message):
    user_db = utils.get_user_by_id(message.from_id)
    user = json.loads(user_db.user)
    lvl = json.loads(user_db.lvls)
    other = json.loads(user_db.other)

    if other['gold'] >= lvl['hp']:
        user['hp'] += 5
        user['cur_hp'] += 5
        other['gold'] -= lvl['hp']
        lvl['hp'] += 100
        user['hp_lvl'] += 1
        user_db.user = json.dumps(user, ensure_ascii=False)
        user_db.other = json.dumps(other, ensure_ascii=False)
        user_db.lvls = json.dumps(lvl, ensure_ascii=False)
        user_db.save()
        await message.answer("Вы успешно прокачали здорье")

    elif other['gold'] < lvl['hp']:
        await message.answer("У Вас недостаточно золота")
    else:
        await message.answer('Произошла ошибка')


@char.message(payload={'lvl': 'dmg'})
async def dmg_up(message: Message):
    user_db = utils.get_user_by_id(message.from_id)
    user = json.loads(user_db.user)
    lvl = json.loads(user_db.lvls)
    other = json.loads(user_db.other)

    if other['gold'] >= lvl['dmg']:
        user['dmg'] += 1
        user['cur_dmg'] += 1
        other['gold'] -= lvl['dmg']
        lvl['dmg'] += 100
        user['dmg_lvl'] += 1
        user_db.user = json.dumps(user, ensure_ascii=False)
        user_db.other = json.dumps(other, ensure_ascii=False)
        user_db.lvls = json.dumps(lvl, ensure_ascii=False)
        user_db.save()
        await message.answer("Вы успешно прокачали урон")

    elif other['gold'] < lvl['dmg']:
        await message.answer("У Вас недостаточно золота")
    else:
        await message.answer('Произошла ошибка')


@char.message(payload={'char': "heall"})
async def heal(message: Message):
    user_db = utils.get_user_by_id(message.from_id)
    user = json.loads(user_db.user)
    if user['cur_hp'] == user['hp']:
        await message.answer("У Вас уже полное здоровье")
    elif user['cur_hp'] < user['hp']:
        user['cur_hp'] = int(user['hp'])
        user_db.user = json.dumps(user, ensure_ascii=False)
        user_db.save()
        await message.answer("Здоровье восстановлено")
    elif user['cur_hp'] > user['hp']:
        user['cur_hp'] = int(user['hp'])
        user_db.user = json.dumps(user, ensure_ascii=False)
        user_db.save()
        await message.answer("Вернул здоровье до максимального значения")
