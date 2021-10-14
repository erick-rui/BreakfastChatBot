from log import Log
from bot import Bot

def main():
    chatLog = Log()
    cBot = Bot()
    cBot.createKnownResponses()
    cBot.createUnknownResponses()
    while(True):
        userInput = input(" --- ")
        if(userInput.lower() == "bye"):
            break
        response = cBot.getResponse(userInput)
        print(response)
        chatLog.addEntry(userInput, response)
    chatLog.runReport()

if __name__ == "__main__":
    main()