from vkbottle import Bot
from loguru import logger
from configs import api, labeler

from proekt.handlers.test import labeler
from proekt.handlers.start import start_bot
from proekt.handlers.menu import menu
from proekt.handlers.character import char
from proekt.handlers.monsters import monsters
from proekt.handlers.other import other
from proekt.handlers.invenory import inventory
from proekt.handlers.casino import casino
from proekt.handlers.bosses import bosses

logger.remove()

labeler.load(start_bot)
labeler.load(menu)
labeler.load(char)
labeler.load(monsters)
labeler.load(other)
labeler.load(inventory)
labeler.load(casino)
labeler.load(bosses)

bot = Bot(
    api=api,
    labeler=labeler,
)

bot.run_forever()
