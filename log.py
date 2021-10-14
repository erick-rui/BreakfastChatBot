class Log:
    
    def __init__(self):
        print("This conversation will be recorded")
        self.entryNum = 0
        self.logHistory = {}
    
    def addEntry(self, question="", answer=""):
        self.entryNum += 1
        entry = {question: answer}
        self.logHistory[self.entryNum] = entry

    def runReport(self):
        print("Transcript:")
        for chatNum in self.logHistory:
            entry = self.logHistory[chatNum]
            print("Chat number,", chatNum, entry)
