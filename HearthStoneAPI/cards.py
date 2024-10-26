import json
import typing

MURLOK_ID = 12

class RaceIDMap:
    UNDEAD = 11 # ok (22)
    MURLOC = 14 # ok (23)
    DEMON = 15 # ok (21)
    MECH = 17 # ok (27)
    ELEMENTAL = 18 # ok (24)
    BEAST = 20 # ok (25)
    PIRATE = 23 # ok (22)
    DRAGON = 24 # ok (22)
    ALL = 26
    QUILBOAR = 43 # ok (21)
    NAGA = 92 # ok (23)


class Card:
    def __init__(self, race_ids, name, tier, hero, duos_only, solos_only, attack, health, armor, text, image):
        self.race_ids = race_ids
        self.name = name
        self.tier = tier
        self.hero = hero
        self.spell = False
        self.duos_only = duos_only
        self.solos_only = solos_only
        self.attack = attack
        self.health = health
        self.armor = armor
        self.text = text if text != '' else -1
        self.image = image
        if not hero and not attack and not health:
            self.spell = True

    def dump(self, indent: int = 2) -> str:
        dmp = f'{" " * indent}Class: {RaceIDMap[self.race_ids]}\n'
        dmp = f'{" " * indent}Name: {self.name}\n'
        dmp += f'{" " * indent}Tier: {self.tier}\n'
        dmp += f'{" " * indent}Hero: {self.hero}\n'
        dmp += f'{" " * indent}Spell: {self.spell}\n'
        dmp += f'{" " * indent}Duos Only: {self.duos_only}\n'
        dmp += f'{" " * indent}Solos Only: {self.solos_only}\n'
        dmp += f'{" " * indent}Attack: {self.attack}\n'
        dmp += f'{" " * indent}Health: {self.health}\n'
        dmp += f'{" " * indent}Armor: {self.armor}\n'
        dmp += f'{" " * indent}Text: {self.text}\n'
        dmp += f'{" " * indent}Image: {self.image}'

        return dmp


class Cards:
    def __init__(self):
        self.all = {}
        self.cards: list[Card] = []
        self.cards_count = 0
        self.pages = 0

        self.heroes = []
        self.monsters = []
        self.spells = []

        self.beasts = []
        self.murlocs = []
        self.undeads = []
        self.demons = []
        self.mechs = []
        self.elementals = []
        self.pirates = []
        self.dragons = []
        self.quilboars = []
        self.nagas = []

    def collect_cards(self, response: dict) -> None:
        if not self.cards_count:
            self.cards_count = response['cardCount']

        if not self.pages:
            self.pages = response['pageCount']

        self.all[response['page']] = []
        for card in response['cards']:
            self.all[response['page']].append(card)

    def process_cards(self) -> None:
        for page in self.all:
            if page in ('cards_count', 'pages'):
                continue

            for card in self.all[page]:
                if 'battlegrounds' in card:
                    race_ids = []
                    race = card['minionTypeId'] if 'minionTypeId' in card else None
                    multi_race = card['multiTypeIds'][0] if 'multiTypeIds' in card else None
                    race_ids.append(race)
                    race_ids.append(multi_race)
                    name = card['name'] if 'name' in card else None
                    text = card['text'] if 'text' in card else None
                    attack = card['attack'] if 'attack' in card else None
                    health = card['health'] if 'health' in card else None
                    armor = card['armor'] if 'armor' in card else None
                    image = card['battlegrounds']['image'] if 'image' in card['battlegrounds'] else None
                    tier = card['battlegrounds']['tier'] if 'tier' in card['battlegrounds'] else None
                    hero = card['battlegrounds']['hero'] if 'hero' in card['battlegrounds'] else None
                    duos_only = card['battlegrounds']['duosOnly'] if 'duosOnly' in card['battlegrounds'] else None
                    solos_only = card['battlegrounds']['solosOnly'] if 'solosOnly' in card['battlegrounds'] else None

                    self.cards.append(
                        Card(
                            race_ids=race_ids, name=name, tier=tier, hero=hero,
                            duos_only=duos_only, solos_only=solos_only,
                            attack=attack, health=health, armor=armor,
                            text=text, image=image
                            )
                    )

        self.sort_cards()

    def add_metadata(self):
        self.all = list(self.all.items())
        self.all.insert(0, ('cards_count', self.cards_count))
        self.all.insert(0, ('pages', self.pages))
        self.all = dict(self.all)

    def dump_all(self, file_handle: typing.TextIO) -> str:
        json.dump(self.all, file_handle, indent=2)

    def sort_cards(self) -> None:
        for card in self.cards:
            # By type
            if card.hero == True:
                self.heroes.append(card)
            elif not card.hero and not card.spell:
                self.monsters.append(card)
            else:
                self.spells.append(card)

            # By race
            if RaceIDMap.ALL in card.race_ids or RaceIDMap.BEAST in card.race_ids:
                self.beasts.append(card)
            if RaceIDMap.ALL in card.race_ids or RaceIDMap.MURLOC in card.race_ids:
                self.murlocs.append(card)
            if RaceIDMap.ALL in card.race_ids or RaceIDMap.UNDEAD in card.race_ids:
                self.undeads.append(card)
            if RaceIDMap.ALL in card.race_ids or RaceIDMap.DEMON in card.race_ids:
                self.demons.append(card)
            if RaceIDMap.ALL in card.race_ids or RaceIDMap.MECH in card.race_ids:
                self.mechs.append(card)
            if RaceIDMap.ALL in card.race_ids or RaceIDMap.ELEMENTAL in card.race_ids:
                self.elementals.append(card)
            if RaceIDMap.ALL in card.race_ids or RaceIDMap.PIRATE in card.race_ids:
                self.pirates.append(card)
            if RaceIDMap.ALL in card.race_ids or RaceIDMap.DRAGON in card.race_ids:
                self.dragons.append(card)
            if RaceIDMap.ALL in card.race_ids or RaceIDMap.QUILBOAR in card.race_ids:
                self.quilboars.append(card)
            if RaceIDMap.ALL in card.race_ids or RaceIDMap.NAGA in card.race_ids:
                self.nagas.append(card)



CARDS = Cards()
