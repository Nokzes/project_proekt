import json
from vkbottle import GroupEventType, Keyboard, EMPTY_KEYBOARD, Text, GroupTypes, KeyboardButtonColor
from vkbottle.bot import Message, BotLabeler, MessageEvent, Bot
import proekt.utils as utils
inventory = BotLabeler()

@inventory.message(payload={'menu': 'inv'})
async def inv(message: Message):
    user_db = utils.get_user_by_id(message.from_id)


