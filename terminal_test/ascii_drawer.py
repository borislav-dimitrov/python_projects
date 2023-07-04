import os
from PIL import Image


class Drawer:
    _ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

    def __init__(self, width=50, ascii_chars=None):
        self._ascii_chars = ascii_chars if ascii_chars is not None else self._ASCII_CHARS
        self.width = width

    def _resize_image(self, image: Image):
        '''Resize the specified image'''
        width, height = image.size
        ratio = height / width / 1.65
        new_height = int(self.width * ratio)
        resized_image = image.resize((self.width, new_height))
        return resized_image

    @staticmethod
    def _grayscale(image: Image):
        '''Convert the specified image to grayscale'''
        grayscale = image.convert('L')
        return grayscale

    def _pixels_to_ascii(self, image: Image):
        '''Convert pixels to ascii characters'''
        pixels = image.getdata()
        characters = ''.join([self._ascii_chars[pixel // 25] for pixel in pixels])
        return characters

    def _format_output(self, output):
        new_output = ''
        while output:
            chunk = output[:self.width]
            output = output[self.width:]
            new_output += f'{chunk}\n'
        return new_output

    def img_to_ascii(self, image_path: str):
        '''Convert image to ascii symbols'''
        if not os.path.isfile(image_path):
            raise Exception(f'Invalid file path {image_path}')

        try:
            image = Image.open(image_path)
        except Exception as exc:
            raise Exception(f'Oops!\n{exc}')

        try:
            image = self._resize_image(image)
            image = self._grayscale(image)
            output = self._pixels_to_ascii(image)
            return self._format_output(output)
        except Exception as exc:
            raise Exception(f'Oops!\n{exc}')
