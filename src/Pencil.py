class Pencil:

    def __init__(self, pointDurability=20, length=10, eraserDurability=10):
        self.writtenText = ""
        self.pointDurabilitySharp = pointDurability
        self.pointDurability = pointDurability
        self.length = length
        self.eraserDurability = eraserDurability

    def write(self, text):
        degradedText = self.degradeText(text)
        self.writtenText += degradedText
        self.pointDurability = self.pointDurability - self.textDurabilityCost(degradedText)
        return self.writtenText

    def degradeText(self, text):
        pointDurability = self.pointDurability
        degradedText = ""
        for char in text:
            durabilityCost = self.textDurabilityCost(char)
            if durabilityCost <= pointDurability:
                degradedText += char
                pointDurability -= durabilityCost
            else:
                break
        return degradedText

    def textDurabilityCost(self, text):
        durabilityCost = 0
        for char in text:
            if len(char.strip()) == 0:
                pass
            elif char.islower():
                durabilityCost += 1
            else:
                durabilityCost += 2
        return durabilityCost

    def sharpen(self):
        if self.length > 0:
            self.length -= 1
            self.resetPointDurability()
        return self.length

    def resetPointDurability(self):
        self.pointDurability = self.pointDurabilitySharp

    def erase(self, textToErase):
        lastIndex = self.writtenText.rfind(textToErase)
        if lastIndex != -1:
            index = lastIndex + len(textToErase)
            while index > lastIndex:
                self.writtenText = self.writtenText[:index-1] + " " + self.writtenText[index:]
                index -= 1