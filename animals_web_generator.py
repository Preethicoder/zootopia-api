import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

output = ''
for animal in animals_data:
    output += '<li class="cards__item">\n'
    output +='<div class="card__title">'+ f'Name: {animal["name"]}'+'</div>\n'
    output +='<p class="card__text">\n'
    output += '<strong>Diet: </strong>'+f"{animal['characteristics']['diet']}<br/>\n"
    output += '<strong>Location: </strong>'+f"{animal['locations'][0]}<br/>\n"
    if "type" in animal["characteristics"]:
        output +='<strong>Type: </strong>'+f"{animal['characteristics']['type']}<br/>\n"
    output += " </p>\n"
    output += '</li>'



with open("animals_template.html","r") as handle:
    html_content = handle.read()

html_content = html_content.replace("__REPLACE_ANIMALS_INFO__",output)

with open("animals_template.html","w") as handle1:
    handle1.write(html_content)

