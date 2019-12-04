class Pencil:

    def __init__(self, 
                 point_durability=20, 
                 length=10, 
                 eraser_durability=10):
        self.written_text = ""
        self.point_durability_sharp = point_durability
        self.point_durability = point_durability
        self.length = length
        self.eraser_durability = eraser_durability
        self.erased_index = []

    def write(self, text):
        index = 0
        while index < len(text):
            char = text[index:index+1]
            if self.can_write(char):
                self.write_one_character(char)
            else: 
                break
            index += 1

    def can_write(self, char):
        return self.point_durability >= self.point_durability_cost(char)

    def point_durability_cost(self, text):
        durability_cost = 0
        for char in text:
            if self.white_space_character(char):
                pass
            elif char.islower():
                durability_cost += 1
            else:
                durability_cost += 2
        return durability_cost

    def write_one_character(self, char):
        self.written_text += char
        self.degrade_point(char)

    def read(self):
        return self.written_text

    def degrade_point(self, text):
        self.point_durability -= self.point_durability_cost(text)

    def sharpen(self):
        if self.length > 0:
            self.length -= 1
            self.reset_point_durability()

    def reset_point_durability(self):
        self.point_durability = self.point_durability_sharp

    def erase(self, text_to_erase):
        last_index = self.written_text.rfind(text_to_erase)
        if last_index != -1:
            index = last_index + len(text_to_erase) - 1
            while index >= last_index and self.can_erase():
                self.erase_one_character(index)
                index -= 1
            self.add_to_erased_index(index+1)

    def can_erase(self):
        return self.eraser_durability > 0

    def erase_one_character(self, index):
        self.change_one_character(index, " ")
        self.degrade_eraser()

    def degrade_eraser(self):
        self.eraser_durability -= 1

    def add_to_erased_index(self, index):
        self.erased_index.append(index)

    def edit(self, text):
        index = self.erased_index.pop(0)
        for num, char in enumerate(text):
            self.change_one_character(index + num, char)

    def change_one_character(self, index, char):
        if self.can_write(char):
            char = self.character_collision(char, index)
            self.written_text = (self.written_text[:index] 
                                + char 
                                + self.written_text[index+1:])
            self.degrade_point(char)

    def white_space_character(self, char):
        return len(char.strip()) == 0

    def existing_character(self, index):
        return self.written_text[index:index+1]

    def character_collision(self, char, index):
        existing_character = self.existing_character(index)
        if (not self.white_space_character(char) 
            and not self.white_space_character(existing_character)):
            char = "@"
        return char

def input_point_durability():
    point_durability = input("Enter the point durability: ")
    if not isinstance(point_durability, int):
        point_durability = ""
    return point_durability

if __name__ == "__main__":

    input_point_durability()
