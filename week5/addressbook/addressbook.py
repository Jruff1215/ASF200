from distutils.command.build_scripts import first_line_re
import requests

class Contact():
    def __init__(self, fname, lname, email, phone, photo):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.phone = phone
        self.photo = photo
        
    def getFirstName(self):
       return self.fname
    def getLastName(self):
       return self.lname
    def getEmail(self):
       return self.email
    def getPhone(self):
       return self.phone
    def getPhoto(self):
       return self.photo
    
    def __str__(self):
        name = self.fname +" "+self.lname + " " 
        email = "(" + self.email + ")"
        return name + email
    def __repr__(self):
        name = self.fname +" "+self.lname + " " 
        email = "(" + self.email + ")"
        return name + email
       

class AddressBook():
    def __init__(self):
        self.addresses = []
        
    def addAddress(self,address):
        self.addresses.append(address)
        
    def getAllAddresses(self):
        return self.addresses
    
    def findAllMatching(self,searchStr):
        results = []
        for address in self.addresses:
            
            if address.getFirstName().lower().startswith(searchStr.lower()) or address.getLastName().lower().startswith(searchStr.lower()):
                results.append(address)
                
        return results
    
   