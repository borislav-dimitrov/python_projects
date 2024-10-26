import math

from itembase import ItemBase


class CraftingResult:
    def __init__(self, new_item_level: int, new_affix_level: int, promised_affixes: int):
        self.new_item_level = new_item_level
        self.new_affix_level = new_affix_level
        self.promised_affixes = promised_affixes
        self.possible_affixes = []
        self.possible_suffixes = []


class Crafting:
    def __init__(self):
        self.base_qlvl: int = 0
        self.crafted_item_ilvl: int = 0
        self.character_lvl: int = 0

    def new(
            self, base_qlvl: int, crafted_item_ilvl: int, character_lvl: int
    ) -> CraftingResult:
        self._validate_input_data(base_qlvl, crafted_item_ilvl, character_lvl)

        self.base_qlvl = base_qlvl
        self.crafted_item_ilvl = crafted_item_ilvl
        self.character_lvl = character_lvl
        new_item_level, new_affix_level = self._calculations()

        result = CraftingResult(
            new_item_level=new_item_level,
            new_affix_level=new_affix_level,
            promised_affixes=self._get_promised_affixes_count()
        )
        return result

    def _get_promised_affixes_count(self) -> int:
        if self.crafted_item_ilvl <= 30:
            return 1
        elif self.crafted_item_ilvl <= 50:
            return 2
        elif self.crafted_item_ilvl <= 70:
            return 3
        else:
            return 4

    def _calculations(self) -> list[int]:
        new_item_level = (self.character_lvl // 2) + (self.crafted_item_ilvl // 2)
        new_item_level = 99 if new_item_level > 99 else new_item_level

        if new_item_level < (99 - (self.base_qlvl // 2)):
            new_affix_level = new_item_level - (self.base_qlvl // 2)
        else:
            new_affix_level = math.floor(new_item_level * 2) - 99

        return [new_item_level, new_affix_level]

    @staticmethod
    def _validate_input_data(
            base_qlvl: int, crafted_item_ilvl: int, character_lvl: int
    ) -> None:
        if (
                not base_qlvl
                or not isinstance(base_qlvl, int)
                or base_qlvl not in list(range(1, 100))
        ):
            raise RuntimeError(f'Invalid base qlvl - {base_qlvl}!')
        if (
                not crafted_item_ilvl
                or not isinstance(crafted_item_ilvl, int)
                or crafted_item_ilvl not in list(range(1, 101))
        ):
            raise RuntimeError(f'Invalid crafted item ilvl - {crafted_item_ilvl}!')
        if (
                not character_lvl
                or not isinstance(character_lvl, int)
                or character_lvl not in list(range(1, 100))
        ):
            raise RuntimeError(f'Invalid character level - {character_lvl}!')


CRAFT = Crafting()
