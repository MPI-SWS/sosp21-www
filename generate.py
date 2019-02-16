#!/usr/bin/env python3.6

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

# CFS
template = env.get_template('cfs.html')
index_file = open("cfs.html", "w")
index_file.write(template.render(page = "cfs", title = ""))

# Venue
template = env.get_template('venue.html')
index_file = open("venue.html", "w")
index_file.write(template.render(page = "venue", title = ""))

pchtml = ""
with open('pc.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    r = []
    for row in csv_reader:
        if (line_count != 0):
            r.append(row)
        line_count += 1
    def getK(r):
        return r[2]
    rows = sorted(r, key=getK)
    row = rows[0]
    pchtml +=  '      <tr>\n'
    pchtml += f'        <td class=organizers-office> Program Committee</td>\n'
    pchtml += f'        <td class=organizers-bearer> {row[0]}, {row[4]}</td>\n' % row
    pchtml +=  '      </tr>\n'
    for row in sorted(r, key=getK)[1:]:
        pchtml +=  '      <tr>\n'
        pchtml += f'        <td class=organizers-bearer> &nbsp;</td>\n'
        pchtml += f'        <td class=organizers-bearer> {row[0]}, {row[4]}</td>\n' % row
        pchtml +=  '      </tr>\n'

# Organizers
template = env.get_template('organizers.html')
index_file = open("organizers.html", "w")
index_file.write(template.render(page = "organizers", title = "", pcorganizers = Markup(pchtml)))

# Code of Conduct
template = env.get_template('code.html')
index_file = open("code.html", "w")
index_file.write(template.render(page = "code-of-conduct", title = ""))

# Sponsors
template = env.get_template('sponsors.html')
index_file = open("sponsors.html", "w")
index_file.write(template.render(page = "sponsors", title = ""))

