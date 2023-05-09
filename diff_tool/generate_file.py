import os
import random
import time


class FileGenerator:
    def __init__(self):
        self._template_1450 = ['Lorem consectetur nulla enim sunt ex reprehenderit veniam commodo ut qui. Eu est exercitation labore fugiat sit pariatur. Aliquip eu magna exercitation sint. Duis deserunt est magna eu.',
                               'Dolor nostrud laboris aliqua id cillum. Aute exercitation enim ex occaecat ea id adipisicing aliquip et cupidatat. Et aliquip excepteur qui pariatur et laboris. Exercitation dolore commodo velit aute culpa non aute consequat sit ut quis mollit. Aute aliquip minim Lorem qui tempor. Quis pariatur duis consequat ea exercitation adipisicing officia esse.',
                               'Labore eiusmod officia duis veniam consequat sint esse id velit nisi. Eu mollit elit consectetur ut adipisicing reprehenderit reprehenderit nostrud dolore proident anim labore id culpa. Lorem qui deserunt aliquip Lorem laboris qui dolor laboris adipisicing. Excepteur sint esse nisi minim tempor ut pariatur dolore. Adipisicing esse nisi cillum velit ex ut. Ullamco mollit aliqua nulla ullamco aute aute proident nostrud consequat minim qui enim.',
                               'Aute adipisicing adipisicing excepteur ea quis culpa in. Proident duis tempor minim et commodo consectetur do amet. Officia sint voluptate anim culpa est incididunt. Ut nostrud magna fugiat elit non ex quis duis. Minim reprehenderit ex ea eu mollit laboris ad.',
                               'Est cupidatat ut amet laborum commodo incididunt est culpa eu pariatur in elit ex. Eu irure aute sunt nostrud sit. Labore excepteur cillum consequat cupidatat non labore dolore nostrud reprehenderit.']
        self._temp_content = []


    def _build_the_content(self):
        rng = random.randrange(0, len(self._template_1450))
        self._temp_content.append(self._template_1450[rng])

    def new_file(self, file_path, rows_nr=100, max_row_len=500):
        self._temp_content.clear()

        while len(self._temp_content) < rows_nr:
            self._build_the_content()

        with open(file_path, 'w') as file:
            for line in self._temp_content:
                file.write(f'{line}\n')

def main_func():
    start = time.time()

    gen = FileGenerator()
    gen.new_file('file1.txt', rows_nr=10000)
    gen.new_file('file2.txt', rows_nr=10000)

    end = time.time() - start
    print(f'Finished in - {end}s')

if __name__ == '__main__':
    main_func()
