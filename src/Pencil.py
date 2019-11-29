class Pencil:

    def __init__(self):
        self.writtenText = ""

    def write(self, wordString):
        self.writtenText += wordString
        return self.writtenText