from zen import ZEN


class FileMod:

    def __init__(self):
        self.file_name = 'ZenOfPython.txt'

    def read(self):
        with open(self.file_name, 'r') as file:
            text = file.read()
            if text == '':
                text = 'Empty'
        return text

    def create_file(self, file_data: str = ZEN):
        with open(self.file_name, 'w') as file:
            file.write(file_data)

    def add_line(self, symbol=str):
        with open(self.file_name, 'a') as file:
            file.write(f'\n{symbol}')

    def finder(self, symbol: str):
        text = self.read().split()
        word_list = []
        for word in text:
            if symbol.upper() in word.upper():
                word_list.append(word)
        return word_list

    def erase(self, file_data=""):
        self.create_file(file_data)

    def finder_adv(self, symbol: str, length=0):
        word_list = []
        for word in self.finder(symbol):
            if len(word) >= length:
                word_list.append(word)
        return word_list
