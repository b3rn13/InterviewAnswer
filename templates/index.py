#this is the views module to render the html file
import jinja2

templateLoader = jinja2.FileSystemLoader(searchpath="Interview/templates")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "index.html"
template = templateEnv.get_template(TEMPLATE_FILE)
outputText = template.render()  # this is where to put args to the template renderer

print(outputText)
