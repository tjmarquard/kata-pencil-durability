class Pencil:

    def __init__(self, pointDurability=20):
        self.writtenText = ""
        self.pointDurability = pointDurability

    def write(self, wordString):
        self.writtenText += wordString
        return self.writtenText