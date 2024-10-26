import os

TEXT_FILE = os.path.abspath(os.path.join(os.path.dirname(__file__),  'src', 'test.txt'))


class Class1:
    def __init__(self):
        self.content_file = TEXT_FILE

    def show_content(self):
        content = ''
        with open(self.content_file, 'r') as h:
            content = ''.join(h.readlines()).strip()

        command = f'msg %username% {content}'
        os.system(command)
