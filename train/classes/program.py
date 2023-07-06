class Exercise:
    def __init__(self, name, reps, rest, sets):
        self.name = name
        self.reps = reps
        self.rest = rest
        self.sets = sets


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
