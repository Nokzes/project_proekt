import json
from vkbottle import GroupEventType, Keyboard, EMPTY_KEYBOARD, Text, GroupTypes, KeyboardButtonColor
from vkbottle.bot import Message, BotLabeler, MessageEvent, Bot
import proekt.utils as utils
monsters = BotLabeler()


@monsters.message(payload={'menu': 'monsters'})
async def menu_monsters(message: Message):
    keyboard = EMPTY_KEYBOARD
    keyboard = Keyboard()
    keyboard.add(Text("Монстр 1", {'monsters': '1'}), color=KeyboardButtonColor.POSITIVE)
    keyboard.row()
    keyboard.add(Text("Монстр 2", {'monsters': '2'}), color=KeyboardButtonColor.NEGATIVE)
    keyboard.row()
    keyboard.add(Text("Монстр 3", {'monsters': '3'}), color=KeyboardButtonColor.POSITIVE)
    keyboard.row()
    keyboard.add(Text('Меню', {'menu': 'menu'}))

    await message.answer("Выберите нужного монстра!", keyboard=keyboard)


@monsters.message(payload={'monsters': '1'})
async def monster_1(message: Message):
    user_db = utils.get_user_by_id(message.from_id)
    monster = json.loads(user_db.monsters)

    keyboard = EMPTY_KEYBOARD
    keyboard = Keyboard()
    keyboard.add(Text("Атаковать", {'monster 1': 'attack'}), color=KeyboardButtonColor.NEGATIVE)
    keyboard.row()
    keyboard.add(Text("Назад", {'menu': 'monsters'}), color=KeyboardButtonColor.POSITIVE)
    keyboard.row()
    keyboard.add(Text('Меню', {'menu': 'menu'}))

    await message.answer("Слизень\n"
                         f"Здоровье {monster['monster 1']['cur_hp']}/{monster['monster 1']['hp']}♥ Урон {monster['monster 1']['dmg']}🗡",
                         keyboard=keyboard, attachment='photo-223986632_456239018')

@monsters.message(payload={'monster 1': 'attack'})
async def attack_monster_1(message: Message):
    user_db = utils.get_user_by_id(message.from_id)
    user = json.loads(user_db.user)
    other = json.loads(user_db.other)
    monster = json.loads(user_db.monsters)

    if monster['monster 1']['cur_hp'] < 0:
        other['gold'] += monster['monster 1']['gold']
        user['exp'] += monster['monster 1']['exp']
        monster['monster 1']['cur_hp'] = monster['monster 1']['hp']
        user_db.user = json.dumps(user, ensure_ascii=False)
        user_db.other = json.dumps(other, ensure_ascii=False)
        user_db.monsters = json.dumps(monster, ensure_ascii=False)
        user_db.save()
        await message.answer(f"Вы убили Слизеня и получили {monster['monster 1']['gold']}💰 и {monster['monster 1']['exp']}✨")

    elif monster['monster 1']['dmg'] >= user['cur_hp']:
        user['cur_hp'] -= monster['monster 1']['dmg']
        if user['cur_hp'] < 0:
            user['cur_hp'] = 0
        user_db.user = json.dumps(user, ensure_ascii=False)
        user_db.save()
        await message.answer("Вы мертвы, восстановите здоровье и продолжайте бой!")

    elif monster['monster 1']['dmg'] < user['cur_hp']:
        user['cur_hp'] -= monster['monster 1']['dmg']
        monster['monster 1']['cur_hp'] -= user['cur_dmg']
        user_db.user = json.dumps(user, ensure_ascii=False)
        user_db.monsters = json.dumps(monster, ensure_ascii=False)
        user_db.save()
        if monster['monster 1']['cur_hp'] < 0:
            other['gold'] += monster['monster 1']['gold']
            user['exp'] += monster['monster 1']['exp']
            monster['monster 1']['cur_hp'] = monster['monster 1']['hp']
            user_db.user = json.dumps(user, ensure_ascii=False)
            user_db.other = json.dumps(other, ensure_ascii=False)
            user_db.monsters = json.dumps(monster, ensure_ascii=False)
            user_db.save()
            await message.answer(
                f"Вы убили Слизеня и получили {monster['monster 1']['gold']}💰 и {monster['monster 1']['exp']}✨")
        else:
            await message.answer(f"Ваше здоровье {user['cur_hp']}♥\n"
                             f"Здоровье монстра {monster['monster 1']['cur_hp']}♥\n"
                             f"Вам нанесли {monster['monster 1']['dmg']}🗡, а вы нанесли {user['cur_dmg']}🗡")


@monsters.message(payload={'monsters': '2'})
async def monster_2(message: Message):
    user_db = utils.get_user_by_id(message.from_id)
    monster = json.loads(user_db.monsters)

    keyboard = EMPTY_KEYBOARD
    keyboard = Keyboard()
    keyboard.add(Text("Атаковать", {'monster 2': 'attack'}), color=KeyboardButtonColor.NEGATIVE)
    keyboard.row()
    keyboard.add(Text("Назад", {'menu': 'monsters'}), color=KeyboardButtonColor.POSITIVE)
    keyboard.row()
    keyboard.add(Text('Меню', {'menu': 'menu'}))

    await message.answer("Гоблин\n"
                         f"Здоровье {monster['monster 2']['cur_hp']}/{monster['monster 2']['hp']}♥ Урон {monster['monster 2']['dmg']}🗡",
                         keyboard=keyboard, attachment='photo-223986632_456239019')


@monsters.message(payload={'monster 2': 'attack'})
async def attack_monster_2(message: Message):
    user_db = utils.get_user_by_id(message.from_id)
    user = json.loads(user_db.user)
    other = json.loads(user_db.other)
    monster = json.loads(user_db.monsters)

    if monster['monster 2']['cur_hp'] < 0:
        other['gold'] += monster['monster 2']['gold']
        user['exp'] += monster['monster 2']['exp']
        monster['monster 2']['cur_hp'] = monster['monster 2']['hp']
        user_db.user = json.dumps(user, ensure_ascii=False)
        user_db.other = json.dumps(other, ensure_ascii=False)
        user_db.monsters = json.dumps(monster, ensure_ascii=False)
        user_db.save()
        await message.answer(f"Вы убили Гоблина и получили {monster['monster 2']['gold']}💰 и {monster['monster 2']['exp']}✨")

    elif monster['monster 2']['dmg'] >= user['cur_hp']:
        user['cur_hp'] -= monster['monster 2']['dmg']
        if user['cur_hp'] < 0:
            user['cur_hp'] = 0
        user_db.user = json.dumps(user, ensure_ascii=False)
        user_db.save()
        await message.answer("Вы мертвы, восстановите здоровье и продолжайте бой!")

    elif monster['monster 2']['dmg'] < user['cur_hp']:
        user['cur_hp'] -= monster['monster 2']['dmg']
        monster['monster 2']['cur_hp'] -= user['cur_dmg']
        user_db.user = json.dumps(user, ensure_ascii=False)
        user_db.monsters = json.dumps(monster, ensure_ascii=False)
        user_db.save()
        if monster['monster 2']['cur_hp'] < 0:
            other['gold'] += monster['monster 2']['gold']
            user['exp'] += monster['monster 2']['exp']
            monster['monster 2']['cur_hp'] = monster['monster 2']['hp']
            user_db.user = json.dumps(user, ensure_ascii=False)
            user_db.other = json.dumps(other, ensure_ascii=False)
            user_db.monsters = json.dumps(monster, ensure_ascii=False)
            user_db.save()
            await message.answer(
                f"Вы убили Гоблина и получили {monster['monster 2']['gold']}💰 и {monster['monster 2']['exp']}✨")
        else:
            await message.answer(f"Ваше здоровье {user['cur_hp']}♥\n"
                             f"Здоровье монстра {monster['monster 2']['cur_hp']}♥\n"
                             f"Вам нанесли {monster['monster 2']['dmg']}🗡, а вы нанесли {user['cur_dmg']}🗡")


@monsters.message(payload={'monsters': '3'})
async def monster_3(message: Message):
    user_db = utils.get_user_by_id(message.from_id)
    monster = json.loads(user_db.monsters)

    keyboard = EMPTY_KEYBOARD
    keyboard = Keyboard()
    keyboard.add(Text("Атаковать", {'monster 3': 'attack'}), color=KeyboardButtonColor.NEGATIVE)
    keyboard.row()
    keyboard.add(Text("Назад", {'menu': 'monsters'}), color=KeyboardButtonColor.POSITIVE)
    keyboard.row()
    keyboard.add(Text('Меню', {'menu': 'menu'}))

    await message.answer("Орк\n"
                         f"Здоровье {monster['monster 3']['cur_hp']}/{monster['monster 3']['hp']}♥ Урон {monster['monster 3']['dmg']}🗡",
                         keyboard=keyboard, attachment='photo-223986632_456239020')


@monsters.message(payload={'monster 3': 'attack'})
async def attack_monster_3(message: Message):
    user_db = utils.get_user_by_id(message.from_id)
    user = json.loads(user_db.user)
    other = json.loads(user_db.other)
    monster = json.loads(user_db.monsters)

    if monster['monster 3']['cur_hp'] < 0:
        other['gold'] += monster['monster 3']['gold']
        user['exp'] += monster['monster 3']['exp']
        monster['monster 3']['cur_hp'] = monster['monster 1']['hp']
        user_db.user = json.dumps(user, ensure_ascii=False)
        user_db.other = json.dumps(other, ensure_ascii=False)
        user_db.monsters = json.dumps(monster, ensure_ascii=False)
        user_db.save()
        await message.answer(f"Вы убили Орка и получили {monster['monster 3']['gold']}💰 и {monster['monster 3']['exp']}✨")

    elif monster['monster 3']['dmg'] >= user['cur_hp']:
        user['cur_hp'] -= monster['monster 3']['dmg']
        if user['cur_hp'] < 0:
            user['cur_hp'] = 0
        user_db.user = json.dumps(user, ensure_ascii=False)
        user_db.save()
        await message.answer("Вы мертвы, восстановите здоровье и продолжайте бой!")

    elif monster['monster 3']['dmg'] < user['cur_hp']:
        user['cur_hp'] -= monster['monster 3']['dmg']
        monster['monster 3']['cur_hp'] -= user['cur_dmg']
        user_db.user = json.dumps(user, ensure_ascii=False)
        user_db.monsters = json.dumps(monster, ensure_ascii=False)
        user_db.save()
        if monster['monster 3']['cur_hp'] < 0:
            other['gold'] += monster['monster 3']['gold']
            user['exp'] += monster['monster 3']['exp']
            monster['monster 3']['cur_hp'] = monster['monster 3']['hp']
            user_db.user = json.dumps(user, ensure_ascii=False)
            user_db.other = json.dumps(other, ensure_ascii=False)
            user_db.monsters = json.dumps(monster, ensure_ascii=False)
            user_db.save()
            await message.answer(
                f"Вы убили Орк и получили {monster['monster 3']['gold']}💰 и {monster['monster 3']['exp']}✨")
        else:
            await message.answer(f"Ваше здоровье {user['cur_hp']}♥\n"
                             f"Здоровье монстра {monster['monster 3']['cur_hp']}♥\n"
                             f"Вам нанесли {monster['monster 3']['dmg']}🗡, а вы нанесли {user['cur_dmg']}🗡")
