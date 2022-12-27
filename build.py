# vim:fileencoding=utf-8:ts=4:sw=4:sts=4:expandtab

import os
import os.path
from jinja2 import Environment, FileSystemLoader

# # Compile a single page with Jinja2
# environment = Environment(loader = FileSystemLoader(os.getcwd()))
# template = environment.get_template('./filler1.html')
# output_page = template.render()
# with open('output/filler1.html', 'w') as f:
#     f.write(output_page)

# Compile a batch and write them to files with Jinja2
pages = []
for file in os.listdir('./'):
    if file.endswith('.html') and not file.startswith('mainframe'):
        pages.append(file)

environment = Environment(loader = FileSystemLoader(os.getcwd()))

for page in pages:
    template = environment.get_template(page)
    output_page = template.render()
    with open('output/' + page, 'w') as f:
        f.write(output_page)
