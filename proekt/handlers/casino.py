import json
import random

from vkbottle import GroupEventType, Keyboard, EMPTY_KEYBOARD, Text, GroupTypes, KeyboardButtonColor
from vkbottle.bot import Message, BotLabeler, MessageEvent, Bot
import proekt.utils as utils
casino = BotLabeler()


@casino.message(payload={'menu': 'casino'})
async def casino_menu(message: Message):
    keyboard = EMPTY_KEYBOARD
    keyboard = Keyboard()

    keyboard.add(Text('Монетка', {'casino': 'coin'}), color=KeyboardButtonColor.POSITIVE)
    keyboard.row()
    keyboard.add(Text("Стаканчик", {'casino': 'glass'}), color=KeyboardButtonColor.NEGATIVE)
    keyboard.row()
    keyboard.add(Text('Кубик', {'casino': 'cube'}), color=KeyboardButtonColor.POSITIVE)
    keyboard.row()
    keyboard.add(Text('Меню', {'menu': 'menu'}))

    await message.answer("Выберите игру", keyboard=keyboard, attachment='photo-223986632_456239022')

@casino.message(payload={'casino': 'coin'})
async def coin(message: Message):
    await message.answer("Для игры напишите: Монетка  <ваша ставка>\n"
                         "В случае победы, Вы получаете 1,9х своей ставки\n"
                         "В случае проигрыша, Вы теряете свою ставку")

@casino.message(payload={'casino': 'glass'})
async def glass(message: Message):
    await message.answer("Для игры напишите: Стаканчик  <ваша ставка>\n"
                         "В случае победы, Вы получаете 2,8х своей ставки\n"
                         "В случае проигрыша, Вы теряете свою ставку")

@casino.message(payload={'casino': 'cube'})
async def glass(message: Message):
    await message.answer("Для игры напишите: Кубик  <ваша ставка>\n"
                         "В случае победы, Вы получаете 5,5х своей ставки\n"
                         "В случае проигрыша, Вы теряете свою ставку")

@casino.message(text=['Монетка <bid>', 'монетка <bid>'])
async def coin_play(message: Message, bid: int):
    user_db = utils.get_user_by_id(message.from_id)
    other = json.loads(user_db.other)
    bid = int(bid)
    if int(other['gold']) < int(bid):
        await message.answer("У вас недостаточно денег")
    elif int(bid) <= 0:
        await message.answer("Сделайте нормальную ставку")
    elif int(other['gold']) >= int(bid):
        c = random.randint(1, 2)
        if c == 1:
            other['gold'] += int(bid*0.9)
            user_db.other = json.dumps(other, ensure_ascii=False)
            user_db.save()
            await message.answer(f"Вы выиграли {int(int(bid)*0.9)}💰\n"
                                 f"Ваш баланс {other['gold']}💰")
        elif c == 2:
            other['gold'] -= int(bid)
            user_db.other = json.dumps(other, ensure_ascii=False)
            user_db.save()
            await message.answer(f"Вы проиграли {bid}💰\n"
                                 f"Ваш баланс {other['gold']}💰")


@casino.message(text=['Стаканчик <bid>', 'стаканчик <bid>'])
async def glass_play(message: Message, bid: int):
    user_db = utils.get_user_by_id(message.from_id)
    other = json.loads(user_db.other)
    bid = int(bid)
    if int(other['gold']) < int(bid):
        await message.answer("У вас недостаточно денег")
    elif int(bid) <= 0:
        await message.answer("Сделайте нормальную ставку")
    elif int(other['gold']) >= int(bid):
        c = random.randint(1, 3)
        if c == 1:
            other['gold'] += int(bid*1.8)
            user_db.other = json.dumps(other, ensure_ascii=False)
            user_db.save()
            await message.answer(f"Вы выиграли {int(int(bid)*1.8)}💰\n"
                                 f"Ваш баланс {other['gold']}💰")
        elif c == 2 or c == 3:
            other['gold'] -= int(bid)
            user_db.other = json.dumps(other, ensure_ascii=False)
            user_db.save()
            await message.answer(f"Вы проиграли {bid}💰\n"
                                 f"Ваш баланс {other['gold']}💰")


@casino.message(text=['Кубик <bid>', 'кубик <bid>'])
async def coin_play(message: Message, bid: int):
    user_db = utils.get_user_by_id(message.from_id)
    other = json.loads(user_db.other)
    bid = int(bid)
    if int(other['gold']) < int(bid):
        await message.answer("У вас недостаточно денег")
    elif int(bid) <= 0:
        await message.answer("Сделайте нормальную ставку")
    elif int(other['gold']) >= int(bid):
        c = random.randint(1, 6)
        if c == 1:
            other['gold'] += int(bid*5.5)
            user_db.other = json.dumps(other, ensure_ascii=False)
            user_db.save()
            await message.answer(f"Вы выиграли {int(int(bid)*5.5)}💰\n"
                                 f"Ваш баланс {other['gold']}💰")
        elif c == 2 or c == 3 or c == 4 or c == 5 or c == 6:
            other['gold'] -= int(bid)
            user_db.other = json.dumps(other, ensure_ascii=False)
            user_db.save()
            await message.answer(f"Вы проиграли {bid}💰\n"
                                 f"Ваш баланс {other['gold']}💰")