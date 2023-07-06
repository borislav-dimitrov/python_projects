import os

from classes import Program
from managers import JsonFileManager


class ProgramsController:
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self._json_fm = JsonFileManager()
        self._programs_repo = r'.\programs'
        self._all_programs = []
        self.load_all()

    # region CRUD
    def create(self, name, data):
        if not self._validate_new_program_name(name):
            raise Exception(f'Program name ({name}) already exists!')
        if not self._validate_new_program_data(data):
            raise Exception(f'Invalid input for creating new program ({name})!')

        new_program = Program(name=name, dict_data=data, file_path=self._build_program_path(name))
        self._save_program(new_program)
        return self._add_program(new_program)

    def copy(self, program, new_name):
        program = self._get_program_by_name(program.name)
        return self.create(new_name, program.dict_data)

    def update(self, old_program: Program, new_program: Program):
        index = self._get_program_index(old_program)
        self._all_programs[index] = new_program
        return new_program

    def delete(self, program: Program):
        index = self._get_program_index(program)
        deleted = self._all_programs.pop(index)
        os.remove(program.file_path)
        return deleted

    # endregion

    # region UTILS
    @property
    def programs(self):
        return self._all_programs

    def _build_program_path(self, new_program_name):
        return os.path.join(self._programs_repo, f'{new_program_name}.json')

    def load_all(self):
        files = os.listdir(self._programs_repo)

        for file in files:
            abs_path = os.path.abspath(os.path.join(self._programs_repo, file))
            self._load_program(abs_path)

    def _load_program(self, file_path):
        content = self._json_fm.read_file(file_path)
        name = os.path.splitext(os.path.basename(file_path))[0]
        program = Program(name=name, dict_data=content, file_path=file_path)
        self._add_program(program)

    def save_all(self):
        for program in self._all_programs:
            self._save_program(program)

    def _save_program(self, program: Program):
        content = program.dump()
        self._json_fm.write_file(content, program.file_path)

    def _add_program(self, program: Program):
        self._all_programs.append(program)
        return program

    # endregion

    # region VALIDATIONS
    @staticmethod
    def _validate_new_program_data(data):
        if not isinstance(data, dict):
            return False

        for exercise in data:
            if 'reps' not in data[exercise] or 'rest' not in data[exercise] or 'sets' not in data[exercise]:
                return False

        return True

    def _validate_new_program_name(self, new_name):
        for program in self._all_programs:
            if program.name == new_name:
                return False

        return True

    # endregion

    # region SEARCH
    def _get_program_index(self, program) -> int | None:
        if program in self._all_programs:
            return self._all_programs.index(program)

    def _get_program_by_name(self, name: str) -> Program | None:
        for program in self._all_programs:
            if program.name == name:
                return program
    # endregion
