# region DEFINITIONS
LATEST_LOBBY_ID = -1
LATEST_CARD_ID = -1


class Definitions:
    EMPTY_CELL = 'X'
    LEFT_TEAM = 0
    RIGHT_TEAM = 1


class CardType:
    MINION = 0
    SPELL = 1


class LobbyType:
    ARENA_1v1 = 0
    ARENA_2v2 = 1
    ARENA_3v3 = 2
    ARENA_4v4 = 3
    DUNGEON = 4


class LobbyState:
    DELETE = -1
    IDLE = 0
    LOOKING_FOR_FIGHT = 1
    PLAYING = 2

    ALL = [DELETE, IDLE, LOOKING_FOR_FIGHT, PLAYING]


class Field:
    TEAMS_GRID = [
        [Definitions.EMPTY_CELL] * 4,
        [Definitions.EMPTY_CELL] * 4
    ]
    COMBAT_GRID = [
        [Definitions.EMPTY_CELL] * 11,
        [Definitions.EMPTY_CELL] * 11,
        [Definitions.EMPTY_CELL] * 11,
        [Definitions.EMPTY_CELL] * 11,

    ]


# endregion


# region CLASSES
class Card:
    def __init__(self, name: str, type_: int):
        self.id_ = self.generate_id()
        self.name = name
        self.type_ = type_

    def generate_id(self):
        global LATEST_CARD_ID
        LATEST_CARD_ID += 1
        return LATEST_CARD_ID


class Player:
    def __init__(self, name):
        self.name = name
        self.active_lobby: Lobby | None = None

    def leave_active_lobby(self):
        if not self.active_lobby:
            return

        status = self.active_lobby.leave(self)
        if status:
            self.active_lobby = None
        else:
            raise Exception(f'Something went wrong while leaving the lobby {self.active_lobby.name}')

    def ready(self, status: bool = True):
        if not self.active_lobby:
            return

        self.active_lobby.set_ready_status(self, status)

    def start_lobby(self):
        if not self.active_lobby:
            return

        self.active_lobby.start_lobby(self)

    def join_lobby(self, lobby):
        if self.active_lobby:
            return

        self.active_lobby = lobby
        status, message = lobby.join(self)
        print(message)

    def create_lobby(self, name: str, lobby_type: int, size: int):
        LOBBY_MGR.create_new(self, name, lobby_type, size)


class CombatManager:
    def __init__(self, left_team: list[Player], right_team: list[Player], sudden_death: int | None = 15):
        self.started = False
        self.combat_grid = Field.COMBAT_GRID
        self.left_team_grid = Field.TEAMS_GRID[Definitions.LEFT_TEAM]
        self.right_team_grid = Field.TEAMS_GRID[Definitions.RIGHT_TEAM]
        self.left_team = left_team
        self.right_team = right_team
        self.round = 1
        self.sudden_death = sudden_death

    def start(self):
        print('Combat started')

        for idx, player in enumerate(self.left_team):
            self.left_team_grid[idx] = player.name[-1]

        for idx, player in enumerate(self.right_team):
            self.right_team_grid[idx] = player.name[-1]

    def process(self):
        self.display_battle_field()

    def end(self):
        print('Combat ended')

    def display_battle_field(self):
        print(f'Round: {self.round}    |    Battle Field:')
        for row_idx, row in enumerate(Field.COMBAT_GRID):
            print(
                Field.TEAMS_GRID[Definitions.LEFT_TEAM][row_idx],
                row,
                Field.TEAMS_GRID[Definitions.RIGHT_TEAM][row_idx]
            )

    def play_card(self, player: Player, card: Card, cell: tuple[int, int]):
        if player in self.left_team:
            valid_positions = self.get_valid_spawn_positions()
        else:
            valid_positions = self.get_valid_spawn_positions(left=False)

        if card.type_ is CardType.MINION:
            pass
        elif card.type_ is CardType.SPELL:
            pass

    def get_valid_spawn_positions(self, left: bool = True):
        valid_positions = []

        if left:
            for r in range(4):
                for c in range(3):
                    valid_positions.append((r, c))
        if not left:
            first_column = len(self.combat_grid[0]) - 1

            for r in range(4):
                for c in range(first_column, 7, -1):
                    valid_positions.append((r, c))

        return valid_positions


class Lobby:
    def __init__(self, id_: int, host: Player, name: str, lobby_type: int, size: int):
        self.id_ = id_
        self.name = name
        self.lobby_type = lobby_type
        self._state = LobbyState.IDLE

        self.host = host
        self.host.active_lobby = self

        self.size = size
        self.slots: dict = self.init_slots()
        self.slots[0]['player'] = host

        self.available_slots = self.size - 1

    def debug(self):
        sep_line = f'{"=" * 20}\n'

        msg = sep_line
        msg += f'    Name: {self.name}\n    Host: {self.host.name if self.host else self.host}\n'
        msg += f'    State: {self.state}\n    Type: {self.lobby_type}\n    Size: {self.size}\n'
        msg += f'    Slots: {self.slots}\n    Available Slots: {self.available_slots}\n'
        msg += sep_line
        print(msg)

    def init_slots(self):
        slots = {}

        for slot in range(self.size):
            slots[slot] = {'player': None, 'ready': False}

        return slots

    def get_players(self):
        players = []

        for slot in self.slots:
            if self.slots[slot]['player'] is not None:
                players.append(self.slots[slot]['player'])

        return players

    def join(self, player: Player):
        if not isinstance(player, Player):
            raise Exception(f'Invalid player object: {type(player)}')

        if self.available_slots <= 0:
            return False, 'Sorry! Lobby is full!'

        player.active_lobby = self

        for slot in self.slots:
            if self.slots[slot]['player'] is None:
                self.slots[slot]['player'] = player
                self.available_slots -= 1
                break

        return True, f'Player {player.name} has joined the lobby {self.name} {self.id_}'

    def remove_player_from_lobby(self, player: Player):
        for slot in self.slots:
            if self.slots[slot]['player'] is player:
                self.slots[slot]['player'] = None
                self.slots[slot]['ready'] = False
                self.available_slots += 1
                print(f'Player {player.name} has left the lobby {self.name} {self.id_}')
                return True

        return False

    def change_host(self, player: Player | None = None):
        if player:
            self.host = player
            return

        for slot in self.slots:
            if self.slots[slot]['player'] is not None:
                self.host = self.slots[slot]['player']
                return

        self.host = None
        self.state = LobbyState.DELETE

    def leave(self, player: Player):
        if not isinstance(player, Player):
            raise Exception(f'Invalid player object: {type(player)}')

        status = self.remove_player_from_lobby(player)
        self.change_host()

        return status

    def set_ready_status(self, player: Player, status: bool):
        for slot in self.slots:
            if self.slots[slot]['player'] is player:
                self.slots[slot]['ready'] = status
                break

    def display(self):
        for slot in self.slots:
            print(f'{slot}: {self.slots[slot] if self.slots[slot] is None else self.slots[slot].name}')

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, new_state: int):
        if self.host is None:
            self._state = LobbyState.DELETE

        if new_state in LobbyState.ALL:
            self._state = new_state
        else:
            raise Exception(f'{new_state} is not a valid state!')

    def start_lobby(self, player: Player):
        if self.host is not player:
            return

        print(f'Host {self.host.name} is starting the lobby {self.name}')
        self.state = LobbyState.LOOKING_FOR_FIGHT


class LobbyManager:
    def __init__(self):
        self.lobbies: list[Lobby] = []
        self.looking_for_fight = {
            LobbyType.ARENA_1v1: [],
            LobbyType.ARENA_2v2: [],
            LobbyType.ARENA_3v3: [],
            LobbyType.ARENA_4v4: [],
            LobbyType.DUNGEON: [],
        }
        self.ongoing_combats = []

    def process(self):
        if not self.lobbies:
            print('No active lobbies found!')

        for lobby in self.lobbies:
            state = lobby.state

            if state == LobbyState.DELETE:
                print(f'Deleting Lobby {lobby.name}')
                self.lobbies.remove(lobby)
            elif state == LobbyState.LOOKING_FOR_FIGHT:
                print(f'{lobby.id_} {lobby.name} {lobby.lobby_type} is looking for a fight!')
                if lobby not in self.looking_for_fight[lobby.lobby_type]:
                    self.looking_for_fight[lobby.lobby_type].append(lobby)

        self.fights_match_up()

    def create_new(self, player: Player, name: str, lobby_type: int, size: int) -> Lobby:
        if player.active_lobby is not None:
            raise Exception(f'You are already in lobby {player.active_lobby.name}!')

        id_ = self.generate_lobby_id()
        lobby = Lobby(id_, player, name, lobby_type, size)
        print(f'\nPlayer {player.name} has created a new lobby {lobby.name}')

        self.lobbies.append(lobby)
        return lobby

    def find_lobbies(self, lobby_type: int):
        result = []

        for lobby in self.lobbies:
            if lobby.lobby_type == lobby_type:
                result.append(lobby)

        return result

    def fights_match_up(self):
        for lobby_type in self.looking_for_fight:
            if len(self.looking_for_fight[lobby_type]) >= 2:
                left_lobby = self.looking_for_fight[lobby_type][0]
                right_lobby = self.looking_for_fight[lobby_type][1]

                left_team, right_team = left_lobby.get_players(), right_lobby.get_players()
                FIGHTS_MGR.fights.append(CombatManager(left_team, right_team))

                self.looking_for_fight[lobby_type].remove(left_lobby)
                self.looking_for_fight[lobby_type].remove(right_lobby)

    def generate_lobby_id(self) -> int:
        global LATEST_LOBBY_ID

        LATEST_LOBBY_ID += 1
        return LATEST_LOBBY_ID


class FightsManager:
    def __init__(self):
        self.fights: list[CombatManager] = []

    def process(self):
        for fight in self.fights:
            if not fight.started:
                fight.start()


# endregion

# region HELPERS
def init_players():
    p1 = Player('P1')
    p2 = Player('P2')
    p3 = Player('P3')
    p4 = Player('P4')
    p5 = Player('P5')
    p6 = Player('P6')
    p7 = Player('P7')
    p8 = Player('P8')

    return p1, p2, p3, p4, p5, p6, p7, p8


# endregion

LOBBY_MGR = LobbyManager()
FIGHTS_MGR = FightsManager()


def main():
    p1, p2, p3, p4, p5, p6, p7, p8 = init_players()

    p1.create_lobby('Arena 2v2', LobbyType.ARENA_2v2, 2)
    lobbies_found = LOBBY_MGR.find_lobbies(LobbyType.ARENA_2v2)
    p7.join_lobby(lobbies_found[0])
    p1.ready()
    p7.ready()
    p1.start_lobby()

    LOBBY_MGR.process()
    FIGHTS_MGR.process()

    p2.create_lobby('Arena 2v2', LobbyType.ARENA_2v2, 2)
    lobbies_found = LOBBY_MGR.find_lobbies(LobbyType.ARENA_2v2)
    p3.join_lobby(lobbies_found[1])
    p2.ready()
    p3.ready()
    p2.start_lobby()

    print()
    LOBBY_MGR.process()
    FIGHTS_MGR.process()

    print()
    combat: CombatManager = FIGHTS_MGR.fights[0]

    hero_card = Card('Hero', CardType.MINION)
    sky_card = Card('Sky', CardType.MINION)

    combat.play_card(p2, hero_card, (1, 2))
    combat.play_card(p1, sky_card, (4, 4))
    combat.process()


if __name__ == '__main__':
    main()
