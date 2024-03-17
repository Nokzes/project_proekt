import json
import random
import time

import proekt.handlers.menu
from vkbottle import GroupEventType, Keyboard, EMPTY_KEYBOARD, Text, GroupTypes
from vkbottle.bot import Message, BotLabeler, MessageEvent, Bot
import config
import proekt.utils as utils
other = BotLabeler()
bot = Bot(config.bot_token)

@other.message(text='тест')
async def test(message: Message):
    # await message.answer(message.attachments[0].photo)
    owner_id = -223986632
    photo_id = 456239017
    at = f'photo{owner_id}_{photo_id}'
    await message.answer("aga", attachment=at)

    # print(message.get_photo_attachments())

@other.message(text=['Ник <nick>', 'ник <nick>'])
async def change_nick(message: Message, nick):
    if len(nick) <= 20:
        user_db = utils.get_user_by_id(message.from_id)
        other = json.loads(user_db.other)
        other['nick'] = nick
        user_db.other = json.dumps(other, ensure_ascii=False)
        user_db.save()
        await message.answer(f'Ваш ник успешно изменён на {other["nick"]}')
    elif len(nick) > 20:
        await message.answer('Слишкон большой ник, поставьте новый до 20 симоволов')


@other.raw_event(GroupEventType.MESSAGE_NEW)
async def heall(event: GroupEventType):
    user_db = utils.get_user_by_id(event['object']['message']['from_id'])
    user = json.loads(user_db.user)
    other = json.loads(user_db.other)
    lvl = json.loads(user_db.lvls)
    if other['reg'] == 1:
        pass
    elif other['reg'] == 0:
        other['nick'] = "Твой ник)"
        other['reg'] = 1
        user_db.other = json.dumps(other, ensure_ascii=False)
        user_db.save()
        keyboard = Keyboard()
        keyboard.add(Text('Меню', {'menu': 'menu'}))
        await bot.api.messages.send(user_id=event['object']['message']['from_id'], random_id=0, message='Нажми на меню', keyboard=keyboard)
    # if int(user['cur_hp']) != int(user['hp']):
    #     if int(user['cur_hp']) < int(user['hp']):
    #         user['cur_hp'] += int((int(user['hp'])/100 * (random.randint(1, 30))))
    #         if int(user['cur_hp']) > int(user['hp']):
    #             user['cur_hp'] = int(user['hp'])
    #         user_db.user = json.dumps(user, ensure_ascii=False)
    #         user_db.save()
    #     if int(user['cur_hp']) > int(user['hp']):
    #         user['cur_hp'] = int(user['hp'])
    #         user_db.user = json.dumps(user, ensure_ascii=False)
    #         user_db.save()
    if user_db.monsters is None:
        monsters = {
            "monster 1": {"hp": 100, "cur_hp": 100, "dmg": 5, "gold": 30},
            "monster 2": {"hp": 300, "cur_hp": 300, "dmg": 30, "gold": 50},
            "monster 3": {"hp": 1000, "cur_hp": 1000, "dmg": 75, "gold": 150}
        }
        user_db.monsters = json.dumps(monsters, ensure_ascii=False)
        user_db.save()
    if user['exp'] >= lvl['char']:
        for i in range(10000):
            if user['exp'] >= lvl['char']:
                user['exp'] -= lvl['char']
                user['lvl'] += 1
                user['cur_lvl'] += 1
                user['dmg'] += 1
                user['cur_dmg'] += 1
                user['hp'] += 5
                user['cur_hp'] += 5
                lvl['char'] = lvl['char'] + 100
                user_db.user = json.dumps(user, ensure_ascii=False)
                user_db.lvls = json.dumps(lvl, ensure_ascii=False)
                user_db.save()
            elif user['exp'] < lvl['char']:
                break
    # else:
        # await bot.api.messages.send(user_id=event['object']['message']['from_id'], random_id=0, message='Я тебя не понял, напиши меню!')

