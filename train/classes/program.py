class Exercise:
    def __init__(self, name, reps, rest, sets):
        self.name = name
        self.reps = reps
        self.rest = rest
        self.sets = sets

    def get_exercise_info(self, indent):
        result = f'{indent}reps  -  {self.reps}\n'
        result += f'{indent}sets  -  {self.sets}\n'
        result += f'{indent}rest  -  {self.rest}\n'
        return result


class Program:
    def __init__(self, name, dict_data, file_path):
        self.file_path = file_path
        self.name = name
        self._dict_data = dict_data
        self.exercises = []

        self._parse_data()

    def _parse_data(self):
        for exercise in self._dict_data:
            self.exercises.append(
                Exercise(
                    exercise,
                    self._dict_data[exercise]['reps'],
                    self._dict_data[exercise]['rest'],
                    self._dict_data[exercise]['sets']
                )
            )

    def dump(self):
        return self._dict_data

    @property
    def dict_data(self):
        return self._dict_data

    def get_preview(self):
        indent = 8 * ' '
        exercise_separator = '===================================================\n'
        preview = exercise_separator

        for exercise in self.exercises:
            preview += f'{exercise.name}\n'
            preview += f'{exercise.get_exercise_info(indent)}'
            preview += exercise_separator

        return preview
