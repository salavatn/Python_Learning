from jinja2 import Template, Environment, FileSystemLoader

tm_path = FileSystemLoader('venv/template')
env = Environment(loader=tm_path)

homePage = env.get_template('base.html').render(
    base_Title='Home Page')
print(homePage)
