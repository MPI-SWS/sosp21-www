#
# Run with python
#

import csv
#import markdown
from jinja2 import Environment, FileSystemLoader, Markup, select_autoescape

env = Environment(
        loader = FileSystemLoader('templates'),
        autoescape=select_autoescape(['html', 'xml'])
        )

# Parse Template
template = env.get_template('index.html')
index_file = open("index.html", "w")
index_file.write(template.render(page = "home", title = ""))
