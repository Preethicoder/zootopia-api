import requests
import os
from dotenv import load_dotenv
load_dotenv()

def fetch_data(animal_name):
    """fetch the data through API  and return as dict"""
    url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    API_KEY = os.getenv('API_KEY')
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