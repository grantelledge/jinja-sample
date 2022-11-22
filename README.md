# Jinja Sample
Super simple example of outputting merged HTML files using the Python [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/) library. Here the `filler#.html` files will be used to populate `mainframe.html`, creating four nearly identical pages. From here, adding content to the filler pages allows for the construction of a simple website.

## Configuration
1. Jinja is not in the standard Python library, so will need to be installed: `pip install Jinja2`
2. The sample pages will be built in `/output` after running `./build.py`.
3. HTML files must be in the root directory, or else `./build.py` will need to be modified accordingly
