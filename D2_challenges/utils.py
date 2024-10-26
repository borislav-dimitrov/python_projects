import random


class D2Classes:
    AMA = 'Amazon'
    ASA = 'Assassin'
    NEC = 'Necromancer'
    BAR = 'Barbarian'
    PAL = 'Paladin'
    SOR = 'Sorcerer'
    DRU = 'Druid'

    ALL = [AMA, ASA, NEC, BAR, PAL, SOR, DRU]


class D2Builds:
    MELEE = 'Melee'
    RANGE = 'Range'
    SUM = 'Summoner'
    CAS = 'Caster'

    ALL = [MELEE, RANGE, SUM, CAS]

class Methods:
    GET = 'GET'
    POST = 'POST'


class PollPresets:
    EASY = 'Easy'
    MEDIUM = 'Medium'
    HARD = 'Hard'
    EXTREME = 'Extreme'
    CUSTOM = 'Custom'

    ALL = [EASY, MEDIUM, HARD, EXTREME, CUSTOM]


PRESET_SETTINGS = {
    PollPresets.EASY: {
        'qol': 1,
        'consumables': 0,
        'item': 1,
        'random_build': False,
        'cls_restricted': 0
    },
    PollPresets.MEDIUM: {
        'qol': 1,
        'consumables': 1,
        'item': 1,
        'random_build': True,
        'cls_restricted': 0
    },
    PollPresets.HARD: {
        'qol': 1,
        'consumables': 2,
        'item': 2,
        'random_build': True,
        'cls_restricted': 2
    },
    PollPresets.EXTREME: {
        'qol': 3,
        'consumables': 3,
        'item': 3,
        'random_build': True,
        'cls_restricted': 3
    }
}


class ChallengeCategories:
    QOL = 'QoL'
    CONSUMABLES = 'Consumables'
    ITEM = 'Item'

    ALL = [QOL, CONSUMABLES, ITEM]


class Errors:
    INVALID_POLL_PRESET = 'Invalid poll preset!'
    INVALID_CHALLENGE_CATEGORY = 'Invalid challenge category!'
    INVALID_BUILD = 'Invalid build!'


def roll_int(min, max):
    '''Roll random integer between(including) the given min/max values'''
    return random.randint(min, max)