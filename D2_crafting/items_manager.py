from itembase import ItemBase
from utils import ITEMS


class ItemsMgr:
    def __init__(self):
        self.normal_armors: list[ItemBase] = []
        self.exceptional_armors: list[ItemBase] = []
        self.elite_armors: list[ItemBase] = []
        self.normal_weapons: list[ItemBase] = []
        self.exceptional_weapons: list[ItemBase] = []
        self.elite_weapons: list[ItemBase] = []

        self._initialize_items()

    def _initialize_items(self):
        for category in ITEMS:
            for item_sub_category in ITEMS[category]:
                for item_base in ITEMS[category][item_sub_category]:
                    item = ITEMS[category][item_sub_category][item_base]
                    match category:
                        case 'normal armor':
                            self._add_normal_armor(item_base, item)
                        case 'exceptional armor':
                            pass
                        case 'elite armor':
                            pass
                        case 'normal weapons':
                            pass
                        case 'exceptional weapons':
                            pass
                        case 'elite weapons':
                            pass
                        case _:
                            raise RuntimeError(f'Invalid category - {category}!')

    def _add_normal_armor(self, item_base: str, item_props: dict):
        item = ItemBase(
            base=item_base,
            min_max_def=item_props['Min/Max Defense'],
            min_str=item_props['Min Strength'],
            durability=item_props['Durability'],
            sockets=item_props['Sockets'],
            qlvl=item_props['QLVL']
        )
        self.normal_armors.append(item)


ITEMS_MGR = ItemsMgr()
