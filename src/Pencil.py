class Pencil:

    def __init__(self, pointDurability=20, length=10, eraserDurability=10):
        self.writtenText = ""
        self.pointDurabilitySharp = pointDurability
        self.pointDurability = pointDurability
        self.length = length
        self.eraserDurability = eraserDurability
        self.erasedIndex = []

    def write(self, text):
        index = 0
        while index < len(text):
            char = text[index:index+1]
            if self.canWrite(char):
                self.writeOneCharacter(char)
            else: 
                break
            index += 1
        return self.writtenText

    def canWrite(self, char):
        return self.pointDurability >= self.pointDurabilityCost(char)

    def pointDurabilityCost(self, text):
        durabilityCost = 0
        for char in text:
            if len(char.strip()) == 0:
                pass
            elif char.islower():
                durabilityCost += 1
            else:
                durabilityCost += 2
        return durabilityCost

    def writeOneCharacter(self, char):
        self.writtenText += char
        self.degradePoint(char)

    def degradePoint(self, text):
        self.pointDurability -= self.pointDurabilityCost(text)

    def sharpen(self):
        if self.length > 0:
            self.shortenPencil()

    def shortenPencil(self):
        self.length -= 1
        self.resetPointDurability()

    def resetPointDurability(self):
        self.pointDurability = self.pointDurabilitySharp

    def erase(self, textToErase):
        lastIndex = self.writtenText.rfind(textToErase)
        if lastIndex != -1:
            index = lastIndex + len(textToErase)
            while index > lastIndex and self.canErase():
                self.eraseOneCharacter(index)
                index -= 1
            self.addToErasedIndex(index)

    def canErase(self):
        return self.eraserDurability > 0

    def eraseOneCharacter(self, index):
        self.writtenText = self.writtenText[:index-1] + " " + self.writtenText[index:]
        self.degradeEraser()

    def degradeEraser(self):
        self.eraserDurability -= 1

    def addToErasedIndex(self, index):
        self.erasedIndex.append(index)

    def edit(self, text):
        index = self.erasedIndex.pop(0)
        for num, character in enumerate(text):
            self.changeOneCharacter(index + num, character)

    def changeOneCharacter(self, index, character):
        if self.canWrite(character):
            writtenCharacter = self.writtenCharacter(index)
            if not self.whiteSpaceCharacter(writtenCharacter):
                character = "@"
            self.writtenText = self.writtenText[:index] + character + self.writtenText[index+1:]
            self.degradePoint(character)

    def whiteSpaceCharacter(self, character):
        return len(character.strip()) == 0

    def writtenCharacter(self, index):
        return self.writtenText[index:index+1]