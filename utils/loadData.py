class LoadDdata:

    def __init__(self, path,data=None):
        # init value
        self.path = path # path into file txt or dict book
        self.data = self.readData()
    def readData(self, mode='r'):
        """
            returned clean data.
            argument:
                + sentences: list [sentence_1, sentence_2, ...] where sentece_1 has formed "Hi i am Thanh Hoai. my eyes is very light."
        """
        with open(self.path, mode) as file:
            data = file.readlines()
            data = self.prepare(data)
            return data

    def prepare(self,sentences):
        """
            return list of all different words.

        """
        array = []
        for sentence in sentences:
            for word in sentence.split():
                a = self.removeSpecialChar(word, ['.'])
                array.append(a.lower())
        return list(set(array))
    
    def removeSpecialChar(self, word, specialCharList):
        """
            returned word after remove special Char.
            argument:
                + word : string. ex: hi, tensorflow,...
                + special char list: list. ex: ['.', '@', '%']
        """
        result = []
        for char in word:
            if char not in specialCharList:
                result.append(char)
        return "".join(result)

a = LoadDdata("data.txt")
print(a.data)

