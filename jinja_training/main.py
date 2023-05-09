import os
from templating.templating import MyTemplating

tmpl = MyTemplating(r'templating\templates')
out = tmpl.read_template('base.html')


tmpl.dump_file(out, r'results\test.html')
tmpl.dump_css(os.path.join(os.getcwd(), r'results\stylesheet.css'))
