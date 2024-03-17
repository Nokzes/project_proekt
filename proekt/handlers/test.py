from proekt.configs import labeler

@labeler.message(text='Test')
async def test(message):
    await message.answer('ДА')