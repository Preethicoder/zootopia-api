import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

output = ''
for animal in animals_data:
    output += '<li class="cards__item">'
    output += f"Name: {animal['name']}<br/>\n"
    output += f"Diet: {animal['characteristics']['diet']}<br/>\n"
    output += f"Location: {animal['locations'][0]}<br/>\n"
    if "type" in animal["characteristics"]:
        output +=f"Type: {animal['characteristics']['type']}<br/>\n"
    output += '</li>'

print(output)

with open("animals_template.html","r") as handle:
    html_content = handle.read()

html_content = html_content.replace("__REPLACE_ANIMALS_INFO__",output)

with open("animals_template.html","w") as handle1:
    handle1.write(html_content)

