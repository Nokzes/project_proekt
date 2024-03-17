import json
from vkbottle import GroupEventType, Keyboard, EMPTY_KEYBOARD, Text, GroupTypes, KeyboardButtonColor
from vkbottle.bot import Message, BotLabeler, MessageEvent, Bot
import proekt.utils as utils
bosses = BotLabeler()

@bosses.message(payload={'menu': 'bosses'})
async def boss_menu(message: Message):
    keyboard = EMPTY_KEYBOARD
    keyboard = Keyboard()

    keyboard.add(Text('Лич', {'bosses': '1'}), color=KeyboardButtonColor.NEGATIVE)
    keyboard.row()
    keyboard.add(Text('Меню', {'menu': 'menu'}))

    await message.answer('Список боссов', keyboard=keyboard)


@bosses.message(payload={'bosses': '1'})
async def boss_1(message: Message):
    boss = utils.bosses(1)
    lich = json.loads(boss.stats)
    keyboard = EMPTY_KEYBOARD
    keyboard = Keyboard()

    keyboard.add(Text('Атаковать', {'boss 1': 'attack'}), color=KeyboardButtonColor.NEGATIVE)
    keyboard.row()
    keyboard.add(Text('Топ урона', {'boss 1': 'top_attacks'}), color=KeyboardButtonColor.POSITIVE)
    keyboard.row()
    keyboard.add(Text('Меню', {'menu': 'menu'}))

    await message.answer(f"Лич {lich['cur_hp']}/{lich['hp']}🖤 {lich['dmg']}🗡",
                         keyboard=keyboard, attachment='photo-223986632_456239023')


@bosses.message(payload={'boss 1': 'top_attacks'})
async def top_attacks(message: Message):
    boss = utils.bosses(1)
    lich = json.loads(boss.stats)
    top = ''
    a = sorted(lich['players'].items(), key=lambda x: x[1], reverse=True)
    for i in a:
        user_db = utils.get_user_by_id(i[0])
        other = json.loads(user_db.other)
        top += f'[https://vk.com/id{i[0]}|{other["nick"]}] нанёс {i[1]}\n'
    await message.answer(f'{top}')


@bosses.message(text='Тест')
async def test(message: Message):
    user_db = utils.get_user_by_id(message.from_id)
    await message.answer(user_db.vk_id)





@bosses.message(payload={'boss 1': 'attack'})
async def boss_1_attack(message: Message):
    boss = utils.bosses(1)
    lich = json.loads(boss.stats)

    user_db = utils.get_user_by_id(message.from_id)
    user = json.loads(user_db.user)
    other = json.loads(user_db.other)
    if lich['cur_hp'] < 0:
        if lich['state'] == 'live':
            for player in list(lich['players']):
                user_db_cycle = utils.get_user_by_id(player)
                other_cycle = json.loads(user_db_cycle.other)
                user_cycle = json.loads(user_db_cycle.user)

                other_cycle['gold'] += lich['gold']
                user_cycle['exp'] += lich['exp']
                user_db_cycle.user = json.dumps(user_cycle, ensure_ascii=False)
                user_db_cycle.other = json.dumps(other_cycle, ensure_ascii=False)
                user_db_cycle.save()
                await message.answer(f"Вы убили Лича и получили {lich['gold']}💰 и {lich['exp']}✨")
            lich['state'] = 'die'
            lich['cur_hp'] = lich['hp']
            lich['boss_start'] = message.date + 10800
            boss.stats = json.dumps(lich, ensure_ascii=False)
            boss.save()
    elif lich['state'] == 'die':
        if message.date > lich['boss_start']:
            lich['state'] = 'live'
            boss.stats = json.dumps(lich, ensure_ascii=False)
            boss.save()
            await message.answer("Босс только возродился, атакуйте ещё раз")
        else:
            await message.answer(f'Босс уже мёртв, приходите через {lich["boss_start"] - message.date}')


    elif lich['dmg'] >= user['cur_hp']:
        user['cur_hp'] -= lich['dmg']
        if user['cur_hp'] < 0:
            user['cur_hp'] = 0
        user_db.user = json.dumps(user, ensure_ascii=False)
        user_db.save()
        await message.answer("Вы мертвы, восстановите здоровье и продолжайте бой!")

    elif lich['dmg'] < user['cur_hp']:
        user['cur_hp'] -= lich['dmg']
        lich['cur_hp'] -= user['cur_dmg']
        other['boss_attack'] += user['cur_dmg']
        lich['players'][f'{message.from_id}'] += int(f'{user[f"cur_dmg"]}')
        if str(user_db.vk_id) not in lich['players']:
            lich['players'][f'{user_db.vk_id}'] = int(f'{user[f"cur_dmg"]}')
        user_db.user = json.dumps(user, ensure_ascii=False)
        boss.stats = json.dumps(lich, ensure_ascii=False)
        user_db.other = json.dumps(other, ensure_ascii=False)
        user_db.save()
        boss.save()
        if lich['cur_hp'] < 0:
            for player in list(lich['players']):
                user_db_cycle = utils.get_user_by_id(player)
                other_cycle = json.loads(user_db_cycle.other)
                user_cycle = json.loads(user_db_cycle.user)

                other_cycle['gold'] += lich['gold']
                other_cycle['boss_attack'] = 0
                user_cycle['exp'] += lich['exp']
                lich['players'].remove(player)
                user_db_cycle.user = json.dumps(user_cycle, ensure_ascii=False)
                user_db_cycle.other = json.dumps(other_cycle, ensure_ascii=False)
                user_db_cycle.save()
                await message.answer(f"Вы убили Слизеня и получили {lich['gold']}💰 и {lich['exp']}✨")

            lich['state'] = 'die'
            lich['cur_hp'] = lich['hp']
            lich['boss_start'] = message.date + 10800
            boss.stats = json.dumps(lich, ensure_ascii=False)
            boss.save()
        else:
            await message.answer(f"Ваше здоровье {user['cur_hp']}♥\n"
                                 f"Здоровье Лича {lich['cur_hp']}🖤\n"
                                 f"Вам нанесли {lich['dmg']}🗡, а вы нанесли {user['cur_dmg']}🗡")


    # await message.answer(f'{lich}')


