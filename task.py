import requests as r
import json

# fetch data from api
def get_api_data(api):
    response = r.get(api)
    if response.status_code == 200:
        print("Successfully fetched the data")
        return response.json()
    else:
        print(f"Error: {response.status_code}. Failed to fetch data.")
        print("Response content:", response.content)

get_api_data("https://api.worldbank.org/v2/country/ARG;BOL;BRA;CHL;COL;ECU;GUY;PRY;PER;SUR;URY;VEN/indicator/NY.GDP.MKTP.CD?format=json&page=1&per_page=50")

