import json
import requests as r
# fetch data from api
def get_api_data(api):
    response = r.get(api)
    if response.status_code == 200:
        print("Successfully fetched the data")
        return response.json()
    else:
        print(f"Error: {response.status_code}. Failed to fetch data.")
        print("Response content:", response.content)




