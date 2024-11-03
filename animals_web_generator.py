import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

def serialize_animal(animal):
    output = ''
    output += '<li class="cards__item">\n'
    output += f'<div class="card__title">Name: {animal["name"]}</div>\n'
    output += '<p class="card__text">\n'
    output += '<ul class="animal-details-list">\n'
    output += f'<li><strong>Diet:</strong> {animal["characteristics"]["diet"]}</li>\n'
    output += f'<li><strong>Location:</strong> {animal["locations"][0]}</li>\n'

    if "color" in animal["characteristics"]:
        output += f'<li><strong>Color:</strong> {animal["characteristics"]["color"]}</li>\n'
    if "type" in animal["characteristics"]:
        output += f'<li><strong>Type:</strong> {animal["characteristics"]["type"]}</li>\n'

    output += '</ul>\n'
    output += '</p>\n'
    output += '</li>'
    return output





skin_types = set()
for animal in animals_data:
    #result += serialize_animal(animal)
    if "skin_type" in animal["characteristics"]:
        skin_types.add(animal["characteristics"]["skin_type"])
skin_types = sorted(skin_types)

print("Available skin Type:::")
for skin_type in skin_types:
    print(f"{skin_type}")

user_input = input("Please enter the skin type::")
include_missing = input("\nDo you want to include animals without a skin_type? (yes/no): ").strip().lower()


result =""
for animal in animals_data:
    if "skin_type" in animal["characteristics"] and animal["characteristics"]["skin_type"] == user_input:
        result += serialize_animal(animal)
    if "skin_type" not in animal["characteristics"] and include_missing == "yes":
        result += serialize_animal(animal)



with open("animals_template.html","r") as handle:
    html_content = handle.read()

html_content = html_content.replace("__REPLACE_ANIMALS_INFO__",result)

with open("animals_template.html","w") as handle1:
    handle1.write(html_content)

