import requests

class User():

    def __init__(self, first, last, email, username, password, uuid, phone, cell, large, thumbnail):
        self.fname = first
        self.lname = last
        self.email = email
        self.username = username
        self.password = password
        self.uuid = uuid
        self.phone = phone
        self.cell = cell
        self.picture = large
        self.thumbnail= thumbnail
        
    def  setFirst(self, first):
         self.fname = first
    
    def setLast(self, last):
        self.lname = last
    
    def setEmail(self, email):
        self.email = email
    
    def setUsername(self, username):
        self.username = username
    
    def setPassword(self, password):
        self.password = password
        
    def setUUID(self, uuid):
        self.uuid = uuid
        
    def setPhone(self, phone):
        self.phone = phone
    
    def setCell(self, cell):
        self.cell = cell
        
    def setPicture(self, large):
        self.picture = large
        
    def setThumbnail(self, thumbnail):
        self.thumbnail = thumbnail
        
    def getFirst(self):
         return self.fname
    
    def getLast(self):
        return self.lname
    
    def getEmail(self):
        return self.email
    
    def getUsername(self):
        return self.username
    
    def getPassword(self):
        return self.password
        
    def getUUID(self):
        return self.uuid
        
    def getPhone(self):
        return self.phone
    
    def getCell(self):
        return self.cell
        
    def getPicture(self):
        return self.picture
        
    def getThumbnail(self):
        return self.thumbnail
    
    def __str__(self):
        retUser = self.fname
        retUser += self.lname
        retUser += self.email
        
        return retUser
    
class AuthorizedUsers():
    def __init__(self):
        self.authUsers = []
        
    def addUser(self, user):
        self.authUsers.append(user)
        
    def showUsers(self):
        for user in self.authUsers:
            userFirstName = user["name"]['first']
            userLastName = user["name"]['last']
            userEmail = user['email']
            print(userFirstName, userLastName, f"({userEmail})")
   

def getUsers():
    URL = "https://randomuser.me/api/?nat=us&results=10"
      
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
    
userList = AuthorizedUsers()
jsonUserData = getUsers()

for userInfo in jsonUserData["results"]:
    
    userList.addUser(userInfo)
    
    
userList.showUsers()