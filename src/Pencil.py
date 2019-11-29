class Pencil:

    def __init__(self, pointDurability=20):
        self.writtenText = ""
        self.pointDurability = pointDurability

    def write(self, text):
        self.writtenText += text
        return self.writtenText

    def degradePoint(self, text):
        for char in text:
            if char.islower():
                self.pointDurability -= 1
        return self.pointDurability
