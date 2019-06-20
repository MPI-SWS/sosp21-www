#!/usr/bin/env python3.6

#
# Run with python
#

import csv
#import markdown
from jinja2 import Environment, FileSystemLoader, Markup, select_autoescape

env = Environment(
        loader = FileSystemLoader('templates'),
        autoescape=select_autoescape(['html', 'xml']),
        extensions=['jinja2_highlight.HighlightExtension']
        )

env.extend(jinja2_highlight_cssclass = 'highlight')

common_pages = [
        'index',
        'cfp',
        'cfw',
        'cfs',
        'cft',
        'code',
        'dei',
        'cc',
        'reg',
        'sponsors',
        'scholarship',
        'venue',
        'visa',
        'workshops'
]

for p in common_pages:
    print("Processing " + p)
    template = env.get_template(p + ".html")
    file = open(p + ".html", "w")
    file.write(template.render(page = p, title = ""))
    file.close()

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
file = open("organizers.html", "w")
file.write(template.render(page = "organizers",
                           title = "",
                           pcorganizers = Markup(pchtml)))
file.close()

