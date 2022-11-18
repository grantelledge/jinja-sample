# vim:fileencoding=utf-8:ts=4:sw=4:sts=4:expandtab

import os
import os.path
from jinja2 import Environment, FileSystemLoader


# Compile a single page with Jinja2
environment = Environment(loader = FileSystemLoader(os.getcwd()))
template = environment.get_template("./postgreSQL.html")
pg_page = template.render()
print(pg_page)

# # Compile the whole batch and write them to files with Jinja2
# pages = [
#     {"title": "PostgreSQL", "content": "./PostgreSQL.html"},
#     {"title": "typeSystem", "content": "./TypeSystem.html"},
# ]


# for i, page in enumerate(pages):
#     pagename = pages[i]["title"]
#     pagetext = pages[i]["content"]
#     content = template.render(
#         page,
#         title = pagename
#         content = pagetext
#     )
#     with open(pagename, mode="w", encoding="utf-8") as message:
#         message.write(content)
