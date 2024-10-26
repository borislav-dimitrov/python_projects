import pandas as pd


class Parser:
    def __init__(self):
        self.arreat_pref_link = 'https://classic.battle.net/diablo2exp/items/magic/pre.shtml'
        self.arreat_suf_link = 'https://classic.battle.net/diablo2exp/items/magic/suf.shtml'

    @staticmethod
    def parse(url: str) -> list[pd.DataFrame]:
        result = pd.read_html(url, encoding='windows-1252')
        return result

    def parse_arreat_summit(self):
        prefixes = PARSER.parse(self.arreat_pref_link)
        suffixes = PARSER.parse(self.arreat_suf_link)
        self._clean_arreat_summit_results(prefixes, suffixes)

    @staticmethod
    def _clean_arreat_summit_results(
            prefixes: list[pd.DataFrame], suffixes: list[pd.DataFrame]
    ) -> None:
        # TODO - unwrap the parsed data and clean it
        for df in prefixes:
            import pdb;
            pdb.set_trace()


PARSER = Parser()
