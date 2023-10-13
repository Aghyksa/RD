import requests
import json

def api():
    try:
        response = requests.get('https://64c36aa4eb7fd5d6ebd0d8b8.mockapi.io/api/v1/username/')
        response.raise_for_status() 
        parsed_json = response.json()
        return parsed_json
    except requests.exceptions.RequestException as e:
        return None
    except json.JSONDecodeError as e:
        return None
    
data = api()