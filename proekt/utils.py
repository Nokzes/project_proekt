from models import User
from models import Boss
import json

def get_user_by_id(user_id):
    try:
        return User().get(vk_id=user_id)
    except:
        User(
            vk_id=user_id,
            user=json.dumps({'hp': 100, 'cur_hp': 100, 'dmg': 15, 'cur_dmg': 15, 'exp': 0, 'lvl': 0, 'cur_lvl': 0,
                             'hp_lvl': 0, 'dmg_lvl': 0}),
            other=json.dumps({"reg": 0, "nick": "nick", "gold": 0, "diamond": 0, "in_menu": 1}),
            monsters=json.dumps({
                "monster 1": {"hp": 100, "cur_hp": 100, "dmg": 5, "gold": 30, "exp": 50},
                "monster 2": {"hp": 300, "cur_hp": 300, "dmg": 30, "gold": 50, "exp": 150},
                "monster 3": {"hp": 1000, "cur_hp": 1000, "dmg": 75, "gold": 150, "exp": 500}
                                }),
            lvls=json.dumps({'char': 100, 'hp': 100, 'dmg': 100})
        ).save()
        return User().get(vk_id=user_id)


def top_func(id):
    return User().get(id=id)

def bosses(id):
    try:
        return Boss().get(id=id)
    except:
        Boss(
            stats=json.dumps({
                "hp": 10000, "cur_hp": 10000, "dmg": 100, "boss_start": 0, "gold": 1000, "exp": 1000, "players": {}, "state": "live"
            })
        ).save()
        return Boss().get(id=id)