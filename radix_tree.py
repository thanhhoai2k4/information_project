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

        # truong hop 1: 1 tu da ton tai trong cay roi va is_leaf == false thi tich if_leaf.
        if  self.value == word and not self.is_leaf:
            self.is_leaf = True

        # Truong 2: net 1 tu chua co trong nodes thi tao ra 1 radix_tree roi them vao node
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

        """

        head = [x.value[0] for x in self.nodes]
        indexBegin = head.index(word[0])
        currentNode = self.nodes[indexBegin]
        if word[0] not in head:
            return False

        else:
            _, remaining_prefix, remaining_word = self.match(currentNode.value, word)
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



def remove_duplicates(words):
    seen = set()
    result = []
    
    for word in words:
        if word not in seen:
            result.append(word)
            seen.add(word)
    return result
import time                
import psutil
import os
# Lấy pid của chương trình hiện tại
pid = os.getpid()
# Lấy đối tượng Process của chương trình
process = psutil.Process(pid)

start_time = time.time()

root = Radix_Tree()
string1 = """A teacher is someone who guides the path of knowledge for their students They are always patient dedicated and passionate about their work 
Despite facing challenges they are ready to share wisdom and help students overcome difficult problems and obstacles A teacher is not only an educator 
Humans are highly intelligent beings capable of thinking creating, and interacting with the world in ways no other species can We possess the ability 
to understand ourselves and the universe, which has led to the development of language culture, science and the arts Humans do not merely exist in society 
we form relationships communicate emotions and share life experiences What sets humans apart is our capacity for self-awareness and reflection. We can question our existence 
the meaning of life and moral values This ability drives us to grow improve and contribute to the collective progress of society""".split()
words = remove_duplicates(string1)
root.insertManyWord(words)
end_time = time.time()

#tính thời gian chạy của thuật toán Python
elapsed_time = end_time - start_time
print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

# pridct word in here
# completeWord = root.predictWord("roman")
# print(completeWord)

# find word:
# bool_word = root.findWord("improve")
# print(bool_word)

# Lấy bộ nhớ đang sử dụng của chương trình (in MB)
memory_info = process.memory_info()
print(f"Chương trình đang sử dụng {memory_info.rss / (1024 * 1024):.2f} MB bộ nhớ.")