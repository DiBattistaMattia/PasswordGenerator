from hashlib import sha256
from threading import Thread
from rdoclient import RandomOrgClient
import os

class classMainController():

    password = None
    key = ""
    social = None

    def __init__(self, stringOption, stringSocial, stringKey):

        if stringOption == 'generate' and stringSocial == None:
            thread = classThread()
            self.key = thread.key
            return

        elif stringOption == 'recover' and stringSocial != '':
            self.key = stringKey
            self.social = stringSocial
            self.generatePassword()
        else:
            return

    def generatePassword(self):

        stringInputSha = (self.social + self.key).encode('utf-8')
        self.password = sha256(stringInputSha).hexdigest()
        return

class classThread(Thread):

    key = ""
    API_KEY = "ab54ba50-e1ed-4c4e-948a-a7b96f44984f"
    key_lenght = 20
    key_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&*_-"
    key_number = 1

    def __init__(self): 

        self.generateKey()
        return

    def accessFile(self, stringNameFile, charPermission, stringToWrite):

            file = open(stringNameFile, charPermission)
            if (charPermission == 'w'):
                file.write(stringToWrite)
                file.close()
                return

            else:
                file.close()
                return

    def generateKey(self):

            response = RandomOrgClient(self.API_KEY)
            result = response.generate_strings(self.key_number, self.key_lenght, self.key_characters)
            self.key = result[0]
            self.accessFile('key.txt', 'w', self.key)
            return

class classRecoverView():

    inputSocialId = 0
    inputSocialName = ""
    keyInput = ""

    def __init__(self):

        arrayStringSocial = ["facebook", "twitter", "instagram", "github", "gmail", "unicredit", "linkedin", "delphi", "amazon"]
        print("Select a social:\n")
        for i in range(0, len(arrayStringSocial)):
            print(arrayStringSocial[i] + " " + str(i) + "\n")

        self.inputSocial = int(input(""))
        if self.inputSocial not in range(0, len(arrayStringSocial)):
            print("Invalid digit!\n")
            return

        self.keyInput = input("Please enter your key\n")
        self.inputSocialName = arrayStringSocial[self.inputSocialId]
        self.clickOnRecover()

    def clickOnRecover(self):

        if self.keyInput == "":
            print("You forget to insert your key\n")
            return

        mainController = classMainController('recover', self.inputSocialName, self.keyInput)
        print("Your password is:\n" + mainController.password)

def main():

    os.system('cls' if os.name == 'nt' else 'clear')
    print("******** Welcome to the PasswordGenerator ********\n")
    optionUser = input("Digit:\n1 -> generate secret key\n2 -> recover a password\n")
    optionUserNumber = int(optionUser)
    
    if optionUserNumber == 1:
        clickOnGenerate()
        endFunction()
    elif optionUserNumber == 2:
        clickOnRecover()
        endFunction()
    else:
        print("Invalid command\n")
        return

def clickOnGenerate():

    os.system('cls' if os.name == 'nt' else 'clear')
    mainController = classMainController('generate', None, None)
    print("Your key is: " + mainController.key + "\n")
    return

def clickOnRecover():

    os.system('cls' if os.name == 'nt' else 'clear')
    classRecoverView()
    return

def endFunction():

    end = ""
    while (end != 'y') or (end != 'n'):
        end = input("Do you want go out? [y/n]")
        print(end)
        if end == 'y' : 
            print("Bye!")
            return
        if end == 'n' : 

            main()
    return

main()