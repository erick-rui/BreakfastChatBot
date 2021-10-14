import random

class Bot:
    def __init__(self):
        self.responses = {}
        self.defaults = {}
        print("Welcome 👋 to our breakfast website. How may I help you?")

    def createKnownResponses(self):
        self.responses = {"hello": "Greetings! I'd be happy to talk more to you about our breakfast options",
         "hi ": "Greetings! I'd be happy to talk more to you about our breakfast options", 
         "hey": "Greetings! I'd be happy to talk more to you about our breakfast options",
         "pancakes": "We have the best pancakes around! Over 40 great varieties",
         "waffles": "Unfortunately we don't serve waffles. We are known for our pancakes",
         "eggs": "We got tons of eggs options that can be made to your liking",
         "bacon": "adding bacon will be an extra $1.50",
         "sausage": "sausages coming right up!",
         "oj": "Having glass of orange juice is the best way to start the day",
         "orange": "Having glass of orange juice is the best way to start the day",
         "coffee": "We'll brew you a fresh pot of coffee at your request",
         "recommend": "Our top selling item on the menu is the 2*3. It includes two pancakes, two eggs, and two strips of bacon",
         "recommendation" : "Our top selling item on the menu is the 2^3. It includes two pancakes, two eggs, and two strips of bacon",
         "menu": "Our Menu includes a variety of food including eggs, pancakes, bacon, etc. Ask for a recommendation to hear about our best seller",
         "thank": "You're welcome! Is there anything else I can help you with",
          }

    def createUnknownResponses(self):
        self.defaults = ["We have the best breakfast selections in town, come on down", 
                        "Feel free to call us if you wish to speak to a more intelligent being", 
                        "Sorry, I don’t understand your questions but I'd be happy to tell you more about our menu"]

    def getDefaultResponse(self):
        randomResponse = random.choice([0, 1, 2])
        return self.defaults[randomResponse]

    #I cant figure out how to change the directory so you might have to look for the text file in a different directory
    def questionsToAdd(self, stringToAdd=""):
        with open("Output.txt", "a") as text_file:
            text_file.write(stringToAdd + "\n")

    def getResponse(self, question):
        foundAnswer = False
        question = question.lower()
        for key in self.responses:
            keyLen = int(len(key))
            if len(key) <= len(question):
                for i in range((len(question) - keyLen) + 1):
                    currentStr = question[i: (keyLen + i)]
                    if(currentStr == key):
                        foundAnswer = True
                        return self.responses[key]
        if(foundAnswer == False):
            self.questionsToAdd(question)
            return self.getDefaultResponse()
                    

    def __repr__(self):
        print()


#cBot = Bot()
#cBot.getResponse("abcdefHiMenu")