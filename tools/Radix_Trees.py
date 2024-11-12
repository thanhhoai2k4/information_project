class RadixNode:
    def __init__(self, prefix: str="", is_leaf: bool=False)->None:
        # declares the type of Nodes attribute.
        # dict:
        #   + Keys: are strings.
        #   + values: are pointers.
        self.nodes: dict[str, RadixNode] = {}

        # IF1: S + v/s/es + O , s + will + Vo: tobe: be
        # if the tree constans its word , a node will be a leaf.
        self.is_leaf = is_leaf

        self.prefix = prefix
    
    def match(self, word: str) -> tuple[str, str, str]:

        """
            compute the common substring (chuoi con chung) of the prefix .
            arguments:
                + word(str): word to compare(So sanh).
            returns:
                ->tuple[str, str, str]: (str, str, str) common substring, remaining(adj: con lai) prefix, remaining(adj: con lai) word
                ex: myprefix vs myfriends
                - (my, prefix, friends)
        """

        x = 0
        for q,w in zip(self.prefix, word):
            if q!= w:
                break
            x += 1
        return self.prefix[:x], self.prefix[x:], word[x:]
    
    def insert_many(self, words: list[str]) -> None:

        """Insert many words in the tree

        Args:
            words (list[str]): list of words

        >>> RadixNode("myprefix").insert_many(["mystring", "hello"])
        """

        for word in words:
            self.insert(word)

    def insert(self, word : str):

        # IF0: S + Vs/es + O, S + Vs/es + O
        # case 1: if the word is the prefix of the node
        # set current(adj) node ad leaf 
        if self.prefix == word and not self.is_leaf:
            self.is_leaf = True

        #
        # case 2: the node has no edges that has a prefix to the word
        # we create an edge.
        elif word[0] not in self.nodes:
            self.nodes[word[0]] = RadixNode(prefix=word, is_leaf=True)

        else:
            incoming_node = self.nodes[word[0]]
            matching_string, remaining_prefix, remaining_word = incoming_node.match(
                word
            )     

            # case 3: remaining_prefix == ""
            # insert: remaining_word.
            if remaining_prefix == "":
                self.nodes[matching_string[0]].insert(remaining_word)

            # case 4: the remaining_prefix and remaining_word are  in a state of coexistence
            # create anode in between both nodes...
            else:
                incoming_node.prefix = remaining_prefix

                aux_node = self.nodes[matching_string[0]]
                self.nodes[matching_string[0]] = RadixNode(matching_string, False)
                self.nodes[matching_string[0]].nodes[remaining_prefix[0]] = aux_node

                if remaining_word == "":
                    self.nodes[matching_string[0]].is_leaf = True
                else:
                    self.nodes[matching_string[0]].insert(remaining_word)     

    def find(self, word: str) -> bool: 

        """
            Does the tree contain the word?
            if contained return True else False
        """

        # dict: https://docs.python.org/2/library/stdtypes.html#dict.get
        incoming_node = self.nodes.get(word[0],None)

        # if incoming_node doesn't exist.
        if not incoming_node:
            return False
        else:
            matching_string, remaining_prefix, remaining_word = incoming_node.match(word)
            if remaining_prefix != "":
                return False
            elif remaining_word == "":
                return incoming_node.is_leaf
            else:
                return incoming_node.find(remaining_word)
            
    def delete(self, word: str) -> bool:

        """Deletes a word from the tree if it exists

        Args:
            word (str): word to be deleted

        Returns:
            bool: True if the word was found and deleted. False if word is not found

        >>> RadixNode("myprefix").delete("mystring")
        False
        """

        incoming_node = self.nodes.get(word[0], None)
        if not incoming_node:
            return False
        else:
            matching_string, remaining_prefix, remaining_word = incoming_node.match(
                word
            )
            # If there is remaining prefix, the word can't be on the tree
            if remaining_prefix != "":
                return False
            # We have word remaining so we check the next node
            elif remaining_word != "":
                return incoming_node.delete(remaining_word)
            # If it is not a leaf, we don't have to delete
            elif not incoming_node.is_leaf:
                return False
            else:
                # We delete the nodes if no edges go from it
                if len(incoming_node.nodes) == 0:
                    del self.nodes[word[0]]
                    # We merge the current node with its only child
                    if len(self.nodes) == 1 and not self.is_leaf:
                        merging_node = next(iter(self.nodes.values()))
                        self.is_leaf = merging_node.is_leaf
                        self.prefix += merging_node.prefix
                        self.nodes = merging_node.nodes
                # If there is more than 1 edge, we just mark it as non-leaf
                elif len(incoming_node.nodes) > 1:
                    incoming_node.is_leaf = False
                # If there is 1 edge, we merge it with its child
                else:
                    merging_node = next(iter(incoming_node.nodes.values()))
                    incoming_node.is_leaf = merging_node.is_leaf
                    incoming_node.prefix += merging_node.prefix
                    incoming_node.nodes = merging_node.nodes

                return True
            
    def print_tree(self, height: int = 0) -> None:

        """Print the tree

        Args:
            height (int, optional): Height of the printed node
        """

        if self.prefix != "":
            print("-" * height, self.prefix, "  (leaf)" if self.is_leaf else "")

        for value in self.nodes.values():
            value.print_tree(height + 1)

    def Enumerate(self,string: str="", result: list=[]) -> list:

        """
            List words related to trees.

            Args:
                 Strings are used to join character sequences(tuan tu) together.
        """

        if self.is_leaf == False:
            string = string + self.prefix
        else:
            string += self.prefix
            result.append(string)
        for value in self.nodes.values():
            value.Enumerate(string, result)
        return result
    
    def predictWord(self , chars: str, result: str=[] , string: str="") ->list :

        """
            predict which words are likely appear

        """
        if self.is_leaf == False:
            string = string + self.prefix
        else:
            string += self.prefix
            if chars in string:
                result.append(string)
        for value in self.nodes.values():
            value.predictWord(chars, result, string)
        return result

    def predictWord_fast():
        pass



# Instruction:
#
# root = RadixNode()
# words = list(set("banana bananas datada datadas".split()))
# root.insert_many(words)
# a = root.pauseNode("ba")