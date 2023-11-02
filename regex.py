#Regular Expression
import re

#creating class
class Regex:
    
    #creating constructor for the class
    def __init__(self, data):
        self.data=data

    #creating email function to validate emails
    def Email(self):
        pattern="([a-z0-9_.])+\@+([a-z0-9])+(\.)+([a-z]{2,6})"

        if re.match(pattern, self.data):
            return True
        else:
            return False

    #function to validate Bangladesh Mobile number
    def Bangladesh_ph(self):
        pattern="^01[11-9]\d{8}$"

        if re.match(pattern, self.data):
            return True
        else:
            return False

    #function to validate USA telephone number
    def Teleph_US(self):
        pattern="^[0-9]{3}-[0-9]{3}-[0-9]{4}$"

        if re.match(pattern, self.data):
            return True
        else:
            return False

    #function to validate password pattern
    def password(self):
        pattern="^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[!@#$%^&*-]).{16,}$"

        if re.match(pattern, self.data):
            return True
        else:
            return False

#calling the functions
print("Validating given email-ID : ",Regex("suriyamoorthyksm@gmail.com").Email())
print("Validating given Bangladesh Phone number : ",Regex("01234567890").Bangladesh_ph())
print("Validating given USA Telephone : ",Regex("123-123-1234").Teleph_US())
print("Validating given password : ",Regex("KSM@7497suriya21").password())