import json
import config
from vkbottle import GroupEventType, Keyboard, EMPTY_KEYBOARD, Text, GroupTypes
from vkbottle.bot import Message, BotLabeler, MessageEvent, Bot
import proekt.utils as utils
start_bot = BotLabeler()
bot = Bot(config.bot_token)


@start_bot.message(text='Начать')
async def start(message: Message):
    user_db = utils.get_user_by_id(message.from_id)
    us_id = await bot.api.users.get(message.from_id)
    other = json.loads(user_db.other)
    if other['reg'] == 1:
        pass
    elif other['reg'] == 0:
        other['nick'] = us_id[0].first_name
        other['reg'] = 1
        user_db.other = json.dumps(other, ensure_ascii=False)
        user_db.save()
        keyboard = Keyboard()
        keyboard.add(Text('Меню', {'menu': 'menu'}))
        await message.answer('Нажми на меню', keyboard=keyboard)


# @start_bot.raw_event(GroupEventType.MESSAGE_NEW)
# async def starter(event: GroupEventType):
#     user_db = utils.get_user_by_id(event['object']['message']['from_id'])
#     await bot.api.messages.send(user_id=604398431, random_id=0, message=f"{event['object']['message']['from_id']}")