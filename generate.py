#!/usr/bin/env python3

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

# CFP
template = env.get_template('cfp.html')
index_file = open("cfp.html", "w")
index_file.write(template.render(page = "cfp", title = ""))

# Venue
template = env.get_template('venue.html')
index_file = open("venue.html", "w")
index_file.write(template.render(page = "venue", title = ""))

# Organizers
template = env.get_template('organizers.html')
index_file = open("organizers.html", "w")
index_file.write(template.render(page = "organizers", title = ""))

# Code of Conduct
template = env.get_template('code.html')
index_file = open("code.html", "w")
index_file.write(template.render(page = "code-of-conduct", title = ""))

# Sponsors
template = env.get_template('sponsors.html')
index_file = open("sponsors.html", "w")
index_file.write(template.render(page = "sponsors", title = ""))


