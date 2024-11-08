import data_fetcher


def serialize_animal(animal):
    """Serialize and create html tag for each item"""
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

def write_newhtml(result):
    """with new generate data it create new html file"""
    with open("animals_template.html", "r") as handle:
        html_content = handle.read()

    html_content = html_content.replace("__REPLACE_ANIMALS_INFO__", result)

    with open("animals.html", "w") as handle1:
        handle1.write(html_content)



def main():


    result =""
    user_input = input("Enter a name of an animal:::")
    animal_data = data_fetcher.fetch_data(user_input)
    for index,animal in enumerate(animal_data):
        result += serialize_animal(animal)
    if result == "":
        result += "The animal \"" + user_input + "\" is not found"
    write_newhtml(result)
    print("Website was successfully generated to the file animals.html.")

if __name__ =="__main__":
    main()






