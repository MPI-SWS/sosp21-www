#
# Run with python
#

import csv
import markdown
from jinja2 import Environment, FileSystemLoader, Markup, select_autoescape

env = Environment(
        loader = FileSystemLoader('templates'),
        autoescape=select_autoescape(['html', 'xml'])
        )

#
# Home Page
#

# Parse Markdown
index_md = open("index.md", "r")
indexcontent = markdown.markdown(index_md.read(),
                                 extensions = ['extra', 'smarty'], 
                                 output_format='html5')

# Parse Template
template = env.get_template('index.html')
index_file = open("index.html", "w")
index_file.write(template.render(page = "home",
                                 title = "",
                                 indextext = Markup(indexcontent)))

#
# People Page
#

# Parse CSV
people_csv = open("people.csv", "r")
people = csv.reader(people_csv,
                    delimiter = ",",
                    quotechar = '"',
                    skipinitialspace = True)
grouping = env.get_template('grouping.html')
person = env.get_template('person.html')
pc = ""
curgroup = ""
for r in people:
    if (len(r) == 0) or (r[0].startswith("#")):
        # Ignore empty lines and comments
        pass
    elif (r[0].startswith("@")):
        pc += "<div class=\"row\">"
        pc += curgroup
        pc += "</div>"
        pc += "<div class=\"row\"><h2>&nbsp;</h2></div>"
        pc += grouping.render(group = r[0][1:])
        curgroup = ""
    else:
        u = ""
        if (r[1].startswith("~")):
            u = "https://cs.uwaterloo.ca/" + r[1]
        else:
            u = r[1]
        curgroup += person.render(name = r[0], url = u, photo = r[2])
pc += "<div class=\"row\">"
pc += curgroup
pc += "</div>"

# Parse Template
template = env.get_template('people.html')
people_file = open("people.html", "w")
people_file.write(template.render(page = "people",
                                  title = ": People",
                                  peopletext = Markup(pc)))

#
# Seminar Page
#

#
# Publications Page
#

