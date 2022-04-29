import requests
from flask import Flask, render_template, request
from addressbook import AddressBook
from addressbook import Contact

app = Flask(__name__)

def getUsers():
    URL = "https://randomuser.me/api/?nat=us&results=25"
      
    try:
        response = requests.get(URL, timeout=5)
        
        response.raise_for_status()
            
        response_JSON = response.json()
            
        return response_JSON
        
    except requests.exceptions.HTTPError as errh:
        print(f"HTTPError - {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Connection Error - {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timout - {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Request Exception - {err}")
    
userList = AddressBook()

@app.route("/")
def index():
    jsonUserData = getUsers()

    for user in jsonUserData["results"]:
        userFirstName = user["name"]['first']
        userLastName = user["name"]['last']
        userEmail = user['email']
        userPhone = user["phone"]
        userPhoto = user["picture"]["large"]
        contact = Contact(userFirstName, userLastName, f"({userEmail})", userPhone, userPhoto)
        userList.addAddress(contact)
    contacts = userList.getAllAddresses()
    return render_template('index.html', results = contacts)

@app.route("/search", methods=["POST"])
def search():
    searchStr = str(request.form.get("search"))
    contacts = userList.findAllMatching(searchStr)
    return render_template('index.html', results = contacts)

if __name__ == "__main__":
    app.run()