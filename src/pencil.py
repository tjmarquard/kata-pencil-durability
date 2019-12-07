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
        if len(self.erased_index) > 0:
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

def build_pencil():
    args = build_pencil_args()
    pencil = Pencil(**args)
    return pencil

def build_pencil_args():
    args = {}
    point_durability = input_point_durability()
    length = input_length()
    eraser_durability = input_eraser_durability()
    if not point_durability == "":
        args['point_durability'] = point_durability
    if not length == "":
        args["length"] = length
    if not eraser_durability == "":
        args["eraser_durability"] = eraser_durability
    return args

def input_point_durability():
    prompt = "Enter the point durability as an integer: "
    return input_attribute(prompt)

def input_length():
    prompt = "Enter the length of the pencil as an integer: "
    return input_attribute(prompt)

def input_eraser_durability():
    prompt = "Enter the eraser durability as an integer: "
    return input_attribute(prompt)

def input_attribute(prompt):
    value = input(prompt)
    return massage_input(value)

def massage_input(value):
    if value.isdigit():
        value = int(value)
    else:
        value = ""
    return value

def use_pencil(pencil):
    user_input = ""
    while not user_input == "4":
        print("1. Read")
        print("2. Write")
        print("3. Erase")
        print("4. Quit")
        user_input = input("Which option: ")
        if user_input == "1":
            view_text(pencil)
        elif user_input == "2":
            write_text(pencil)
        elif user_input == "3":
            erase_text(pencil)

def view_text(pencil):
    print("The current text is:")
    print(pencil.read())

def write_text(pencil):
    text = input("Enter text to write: ")
    pencil.write(text)

def erase_text(pencil):
    text = input("Enter text to erase: ")
    pencil.erase(text)

if __name__ == "__main__":
    pencil = build_pencil()
    use_pencil(pencil)