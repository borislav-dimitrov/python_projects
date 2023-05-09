from jinja2 import Environment, FileSystemLoader, select_autoescape


class MyTemplating:
    def __init__(self, templates_folder, css_location='stylesheet.css'):
        self.environment = Environment(lstrip_blocks=False,
                                       trim_blocks=False,
                                       loader=FileSystemLoader(templates_folder)
                                       )
        self.css = css_location

    def read_template(self, filename, **kwargs):
        '''
        Read template and return its content.

        :param filename: Str - path to the template file
        :param kwargs: variables to be passed to the templating engine [key - var name, value - var value]
        :return: Str - Output ready to build a html file
        '''
        template = self.environment.get_template(filename)

        template_output = template.render(**kwargs)

        return template_output

    @staticmethod
    def dump_file(template_content, file_name, encoding='utf-8'):
        '''
        Dump the pre-built html content to file.

        :param template_content: Str - pre-built html content
        :param file_name: Str - Path of the new file that will be created
        :param encoding: Str - File encoding
        :return: None
        '''
        with open(file_name, 'w', encoding=encoding) as file:
            file.write(template_content)

    def dump_css(self, location):
        '''TODO:'''
        self.dump_file(self.read_template(self.css), location)
