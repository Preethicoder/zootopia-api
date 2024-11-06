import requests

API_KEY = "XtqZydX183Zhf+X/9V6fug==rCL9bWK2Qv9MNWKN"

def fetch_data(animal_name):
    """fetch the data through API  and return as dict"""
    url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    # Include the API key in the headers
    headers = {
        "X-Api-Key": API_KEY
    }
    res = requests.get(url, headers)
    animal_data = res.json()
    return animal_data

def main():
    pass


if __name__ == "__main__":
    main()