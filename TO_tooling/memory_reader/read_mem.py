import pymem
import pymem.process as pm_proc
from pymem.ptypes import RemotePointer


class MemReader:
    def __init__(self) -> None:
        self._pm = pymem.Pymem()
        self._game_base_addr = None

        self._hp_pointer = 0x00C15980
        self._hp_offsets = [0x7A0, 0x64, 0x8, 0xE4, 0x38, 0x218, 0x3B8]

        self._mp_pointer = 0x00D39C10
        self._mp_offsets = [0x64, 0x30, 0x7B8, 0x30, 0x28, 0x7E8, 0x3BC]

        self._target_pointer_1 = 0x00ECE2E0  # or 0x049E6B68
        self._target_1_offsets = [0x18, 0x16C, 0x0, 0xC, 0x1F4, 0x54, 0x54]

        self._target_pointer_2 = 0x00ECE2E0 # or 0x049E6B68
        self._target_2_offsets = [0x18, 0x16C, 0x0, 0xC, 0x1F4, 0x50, 0x4D4]

    def set_current_process(self, pid: int) -> None:
        self._pm.open_process_from_id(pid)
        self._game_base_addr = list(self._pm.list_modules())[0].lpBaseOfDll

    def get_ptr_addr(self, base_addr, pointer, offsets, as_int: bool = True):
        addr = self._pm.read_int(base_addr + pointer)

        for i in offsets[:-1]:
            try:
                addr = self._pm.read_int(addr + i)
            except pymem.exception.MemoryReadError:
                return -1

        if as_int:
            self._pm.read_bytes(addr + offsets[-1], 20).decode()
            return self._pm.read_int(addr + offsets[-1])
        else:
            str_len = 20
            import pdb; pdb.set_trace()
            return self._pm.read_string(addr + offsets[-1], str_len, encoding='UTF-8')

    def get_hp_mp(self) -> tuple[int, int]:
        if not self._pm or not self._game_base_addr:
            return -1, -1

        hp = self.get_ptr_addr(self._game_base_addr, self._hp_pointer, self._hp_offsets)
        mp = self.get_ptr_addr(self._game_base_addr, self._mp_pointer, self._mp_offsets)
        return hp, mp

    def get_target_name(self) -> str:
        if not self._pm or not self._game_base_addr:
            return 'null'

        target = self.get_ptr_addr(
            self._game_base_addr, self._target_pointer_1, self._target_1_offsets, as_int=False
        )
        print(target)
        import pdb; pdb.set_trace()
