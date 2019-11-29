class Pencil:

    def __init__(self, pointDurability=20):
        self.writtenText = ""
        self.pointDurability = pointDurability

    def write(self, text):
        self.writtenText += text
        return self.writtenText

    def degradePoint(self, text):
        for char in text:
            if len(char.strip()) == 0:
                pass
            elif char.islower():
                self.pointDurability -= 1
            else:
                self.pointDurability -= 2       #punctuation counts as 2
        return self.pointDurability
