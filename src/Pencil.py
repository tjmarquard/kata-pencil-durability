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

    def canWrite(self, char):
        return self.pointDurability >= self.pointDurabilityCost(char)

    def pointDurabilityCost(self, text):
        durabilityCost = 0
        for char in text:
            if self.whiteSpaceCharacter(char):
                pass
            elif char.islower():
                durabilityCost += 1
            else:
                durabilityCost += 2
        return durabilityCost

    def writeOneCharacter(self, char):
        self.writtenText += char
        self.degradePoint(char)

    def read(self):
        return self.writtenText

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
            index = lastIndex + len(textToErase) - 1
            while index >= lastIndex and self.canErase():
                self.eraseOneCharacter(index)
                index -= 1
            self.addToErasedIndex(index+1)

    def canErase(self):
        return self.eraserDurability > 0

    def eraseOneCharacter(self, index):
        self.changeOneCharacter(index, " ")
        self.degradeEraser()

    def degradeEraser(self):
        self.eraserDurability -= 1

    def addToErasedIndex(self, index):
        self.erasedIndex.append(index)

    def edit(self, text):
        index = self.erasedIndex.pop(0)
        for num, char in enumerate(text):
            self.changeOneCharacter(index + num, char)

    def changeOneCharacter(self, index, char):
        if self.canWrite(char):
            char = self.characterCollision(char, index)
            self.writtenText = self.writtenText[:index] + char + self.writtenText[index+1:]
            self.degradePoint(char)

    def whiteSpaceCharacter(self, char):
        return len(char.strip()) == 0

    def existingCharacter(self, index):
        return self.writtenText[index:index+1]

    def characterCollision(self, char, index):
        existingCharacter = self.existingCharacter(index)
        if not self.whiteSpaceCharacter(char) and not self.whiteSpaceCharacter(existingCharacter):
            char = "@"
        return char