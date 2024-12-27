class Radix_Tree:
    def __init__(self, value: str="", is_leaf: bool=False)->None:

        """
            constructor: 
                is_leaf: bool.
                value : str.
                nodes = list[] :Pointer to near object
                            nodes[i]: Radix_Tree.
        """
        self.is_leaf = is_leaf
        self.value = value
        self.nodes = []

    def match(self, firstWord, secondWord):
        """
            split the string into three special part
            args:
                firstWord: str
                secondWord: str
            return: [str, str, str]

            ex:
                match("Hoai", "Hoang")->["Hoa", "i", "ng"].
        """

        x = 0

        # 
        numberOfSequence = len(firstWord) if len(secondWord) > len(firstWord) else len(secondWord)
        
        for i in  range(numberOfSequence):
            if (firstWord[i] != secondWord[i]):
                break
            x += 1

        return firstWord[:x], firstWord[x:], secondWord[x:]
    
    def insertWord(self, word: str):
        """
            insert word into the tree radix

            args:
                word: str

            return : None
        """


        head = [x.value[0] for x in self.nodes]

        try:
            index = head.index(word[0])
            data = self.nodes[index]
        except:
            data = self

        # truong hop 1: 1 tu da ton tai trong cay roi va is_leaf == false thi tich if_leaf.
        if  data.value == word and not self.is_leaf:
            self.is_leaf = True

        # Truong 2: net 1 tu chua co trong nodes thi tao ra 1 radix_tree roi them vao node
        elif word[0] not in head:
            self.nodes.append(Radix_Tree(value=word, is_leaf=True))
        
        else:
            index_a = head.index(word[0])
            incoming_node = self.nodes[index_a]
            matching_string, remaining_prefix, remaining_word = self.match(incoming_node.value, word)

            if remaining_prefix == "":
                incoming_node.insertWord(remaining_word)

            else: 
                incoming_node.value = remaining_prefix
                aux_node = self.nodes[index_a]
                # Add a node with the same string to the current nodes
                self.nodes[index_a] = Radix_Tree(matching_string, False)
                # add a node with string (remaining_prefix) into next current node
                self.nodes[index_a].nodes.append(aux_node)

                if remaining_word== "":
                    self.nodes[index_a].is_leaf = True
                else:
                    self.nodes[index_a].insertWord(remaining_word)
    
    def insertManyWord(self, words: list[str]) ->None:
        """
            insert many word
            args:
                words : list, a array (1 chieu) with each element is the string.
            return: None.
        """
        for word in words:
            self.insertWord(word=word)


    def findWord(self, word: str) ->bool:
        """
            True khi từ tồn tại trong cây, ngược lại.
            args:
            word : str, từ cần tìm.
            return: bool
        """

        head = [x.value[0] for x in self.nodes]
        indexBegin = head.index(word[0])
        currentNode = self.nodes[indexBegin]
        if word[0] not in head:
            return False

        else:
            _, remaining_prefix, remaining_word = self.match(currentNode.value, word)
            # Math giữa 2 chuoi curentNode.value và word
            # TH1 : remaining_prefix != ""
            #   - Giữa node hiện tại và chuổi có phần tử giống nhau và kháu nhau.
            #   - VD: node hiện tại: No và từ word: Na
            #   - Vì thế Return False
            if remaining_prefix != "":
                return False
            
            # TH2 : remaining_prefix == "" (*)
            # curentNode.vallue == word Tương đương với (*)
            elif remaining_word == "":
                return currentNode.is_leaf
            else:
                # TH3: Insert tiếp Remaining_word tại node hiện tại.

                return currentNode.findWord(remaining_word)

    def delete(self, word):
        """
            Hoàng thành sau.
        """
        # get first char list
        head = [x.value[0] for x in self.nodes]
        if word[0] not in head:
            return False
        else:
            index_a = head.index(word[0])
            incoming_node = self.nodes[index_a]
            # giong, khac1, khac2
            match_string, remaining_prefix, remaining_word = self.match(incoming_node.value, word)

            # Truong hop: word chua xuat hien trong cay. return False
            if remaining_prefix!= "":
                return False
            elif remaining_word != "":
                return incoming_node.delete(remaining_word)

            elif not incoming_node.is_leaf:
                return False
            else:
                if len(incoming_node.nodes) == 0:
                    index = head.index(word[0])
                    del self.nodes[index]

                    # hop nhat node hien tai vs nhung thang can ke cua no
                    # khong co canh nao
                    if (len(self.nodes) == 1) and not self.is_leaf:
                        merging_node = self.nodes[0]
                        self.is_leaf = merging_node.is_leaf
                        self.value   += merging_node.value
                        self.nodes = merging_node.nodes
                # > 1 canh
                elif len(incoming_node.nodes) > 1:
                    incoming_node.is_leaf = False

                # 1 canh
                else:
                    merging_node = self.nodes[0]
                    incoming_node.is_leaf = merging_node.is_leaf
                    incoming_node.value += merging_node.value
                    incoming_node.nodes = merging_node.nodes


                return True

    def predictWord(self, word: str,string: str="" ,result: str=[])->str:
        """
            1 node là từ khi is_leaf = True.
            Trả về 1 mảng các từ có thể xuất hiện tiếp theo.
            args: chuổi word, chuổi string, mảng result.
        """

        if self.is_leaf == False:
            string +=  self.value
        else:
            string += self.value
            if word in string:
                result.append(string)
        for value in self.nodes:
            value.predictWord(word, string, result)
        return result

class LOADDATATXT():
    def __init__(self,path):
        self.path = path

    """Load data from a file txt"""
    def load_data(self):
        data = []
        with open(self.path, "r") as f:
            data = f.readlines()
        res = []
        for sub in data:
            res.append(sub.replace("\n", ""))

        return res
    def remove_duplicates(self, words):
        return list(set(words))
    def load(self):
        data = self.load_data()
        results = self.remove_duplicates(data)
        return results




# root = Radix_Tree()
# words = "romane romanus romulus rubens ruber rubicon rubicundus ruberaa ruberbb".split()
# root.insertManyWord(words)
# root.insertWord("rom")
# a = root.delete("rom")
# print(a)