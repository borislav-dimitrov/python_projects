from crafting import CRAFT
from utils import ITEMS
from parser import PARSER


def main():
    PARSER.parse_arreat_summit()
    # base_qlvl = ITEMS['normal armor']['helms']['Cap']['QLVL']
    #
    # result = CRAFT.new(
    #     base_qlvl=base_qlvl,
    #     crafted_item_ilvl=86,
    #     character_lvl=84
    # )
    # print(result.__dict__)


if __name__ == '__main__':
    main()
