import os
from datetime import datetime


class HistoryManager:
    VIDEO_SEPARATOR = ' | '
    def __init__(self, history_dir=rf'.\history'):
        self._history_dir = history_dir
        self._daily_path = os.path.normpath(os.path.join(self._history_dir, 'daily.txt'))


    @property
    def daily_path(self):
        '''Get the daily history file abs path'''
        return os.path.normpath(os.path.abspath(self._daily_path))

    def save(self, file, content):
        '''Create/Save a file with given path and content'''
        with open(file, 'w') as handler:
                handler.writelines(content)

    def load_history_file(self, file):
        '''Load the content from the given history file'''
        if not os.path.isfile(file):
            raise Exception(f'"{file}" is not a valid file!')

        with open(file, 'r') as handler:
            lines = handler.readlines()

        return lines[0].strip().split(self.VIDEO_SEPARATOR)

    def append(self, file, existing, new):
        '''
        Append a video link to a file.
        WARNING: Not suitable for usage in a loops since it access the file on each vid!
        '''
        if new not in existing:
            existing.append(new)
            with open(file, 'w') as handler:
                handler.writelines(self._content_to_single_line(existing))

    def create_daily_history(self, new_content: list):
        '''Create/Overwrite the daily history file'''
        with open(self._daily_path, 'w') as handler:
            handler.writelines(self._content_to_single_line(new_content))

    def update_daily_history(self, new_content):
        '''Update the daily history file with new videos'''
        if not os.path.isfile(self._daily_path):
            self.save(self._daily_path, self._content_to_single_line(new_content))
            return

        daily_content = self.load_history_file(self._daily_path)

        for video in new_content:
            if video not in daily_content:
                daily_content.append(video)

        daily_content = self._content_to_single_line(daily_content)
        self.save(self._daily_path, daily_content)

    def create_temp_history(self, content: list):
        '''Create a "temp" history after each downloads'''
        filename = f'{self.generate_timestamp()[0]}.txt'
        file_path = os.path.normpath(os.path.join(self._history_dir, filename))
        content = self._content_to_single_line(content)

        self.save(file_path, content)

    def _content_to_single_line(self, content: list):
        '''Convert the given list of links to a single line format for the history files'''
        return f'{self.VIDEO_SEPARATOR}'.join(content)

    def generate_timestamp(self):
        '''Generate full date and time, date only and time only timestamps '''
        time_now = datetime.now()
        full_time_stamp = time_now.strftime('%d-%m-%Y_%H-%M-%S')
        nice_full_time_stamp = time_now.strftime('%d-%m-%Y, %H:%M:%S')
        date, time = full_time_stamp.split('_')
        return full_time_stamp, date, time, nice_full_time_stamp

