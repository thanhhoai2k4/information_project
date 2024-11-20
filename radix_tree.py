class Radix_Tree:
    def __init__(self, value: str="", is_leaf: bool=False)->None:

        """
            constructor: 
        """
        self.is_leaf = is_leaf
        self.value = value
        self.nodes = []

    def match(self, firstWord, secondWord):
        """
        
        """

        x = 0
        numberOfSequence = len(firstWord) if len(secondWord) > len(firstWord) else len(secondWord)
        
        for i in  range(numberOfSequence):
            if (firstWord[i] != secondWord[i]):
                break
            x += 1

        return firstWord[:x], firstWord[x:], secondWord[x:]
    
    def insertWord(self, word: str):
        """

        """
        head = [x.value[0] for x in self.nodes]

        # truong hop 1 1 tu da ton tai trong cay roi thi tich if_leaf
        if  self.value == word and not self.is_leaf:
            self.is_leaf = True

        # net 1 tu chua co trong cay thi them node do vao cay 
       
        elif word[0] not in head:
            self.nodes.append(Radix_Tree(value=word, is_leaf=True))
        
        else:
            index_a = head.index(word[0])
            incoming_node = self.nodes[index_a] 

            matching_string, remaining_prefix, remaining_word = self.match(incoming_node.value, word)

            if remaining_prefix == "":
                self.nodes[index_a].insertWord(remaining_word)

            else: 
                incoming_node.value = remaining_prefix
                aux_node = self.nodes[index_a]
                self.nodes[index_a] = Radix_Tree(matching_string, False)
                self.nodes[index_a].nodes.append(aux_node)

                if remaining_word== "":
                    self.nodes[index_a].is_leaf = True
                else:
                    self.nodes[index_a].insertWord(remaining_word)
    
    def insertManyWord(self, words: list[str]) ->None:
        for word in words:
            self.insertWord(word=word)


    def findWord(self, word: str) ->bool:

        head = [x.value[0] for x in self.nodes]
        indexBegin = head.index(word[0])
        currentNode = self.nodes[indexBegin]
        if word[0] not in head:
            return False

        else:
            matching_string, remaining_prefix, remaining_word = self.match(currentNode.value, word)
            if remaining_prefix != "":
                return False
            elif remaining_word == "":
                return currentNode.is_leaf
            else:
                return currentNode.findWord(remaining_word)

    def delete(self):
        pass

    def predictWord(self, word: str,string: str="" ,result: str=[])->str:
        if self.is_leaf == False:
            string +=  self.value
        else:
            string += self.value
            if word in string:
                result.append(string)
        for value in self.nodes:
            value.predictWord(word, string, result)
            
        return result
                

root = Radix_Tree()
words = list(("romane romanus romulus").split())
root.insertManyWord(words)


# pridct word in here
# completeWord = root.predictWord("roman")
# print(completeWord)

# find word:
# bool_word = root.findWord("romane")
# print(bool_word)