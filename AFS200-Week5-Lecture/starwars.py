import requests

def getFromSWAPI(queryType,itemID):
    try:
        # Construct a Request object and use its "get" method
        # Receive a Response object once the Requests gets a response back from the server.
        response = requests.get(f'https://swapi.dev/api/{queryType}/{itemID}', timeout=5)
        
        print(type(response))
        
        # Return an HTTPError object if an error has occurred during the process.
        response.raise_for_status()
        
        # Code here will only run if the request is successful
        response_JSON = response.json()  
        
        return response_JSON
        # print(response_JSON)
        
        # print(f"Name: {response_JSON['name'].title()}")
        # print(f"Eye Color: {response_JSON['eye_color'].capitalize()}")

       
    except requests.exceptions.HTTPError as errh:
        print(f"HTTPError - {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Connection Error - {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timout - {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Request Exception - {err}")
        

    
getFromSWAPI("people",4)   
