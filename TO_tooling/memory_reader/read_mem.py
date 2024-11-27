import pymem
import pymem.process as pm_proc
from pymem.ptypes import RemotePointer


class MemReader:
    def __init__(self, proc_name):
        self.pm = pymem.Pymem(proc_name)
        self.game_module = pm_proc.module_from_name(self.pm.process_handle, proc_name).lpBaseOfDll

        self.hp_pointer = 0x00C15980
        self.hp_offsets = [0x7A0, 0x64, 0x8, 0xE4, 0x38, 0x218, 0x3B8]

        self.mp_pointer = 0x00D39C10
        self.mp_offsets = [0x64, 0x30, 0x7B8, 0x30, 0x28, 0x7E8, 0x3BC]

    def get_ptr_addr(self, base_addr, pointer, offsets):
        addr = self.pm.read_int(base_addr + pointer)

        for i in offsets[:-1]:
            addr = self.pm.read_int(addr + i)

        return self.pm.read_int(addr + offsets[-1])

    def get_hp_mp(self) -> tuple[int, int]:
        hp = self.get_ptr_addr(self.game_module, self.hp_pointer, self.hp_offsets)
        mp = self.get_ptr_addr(self.game_module, self.mp_pointer, self.mp_offsets)
        return hp, mp
