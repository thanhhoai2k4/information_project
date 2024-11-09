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

        """
        # dict: https://docs.python.org/2/library/stdtypes.html#dict.get
        incoming_node = self.nodes.get(word[0])

        # if incoming_node doesn't exist.
        if not incoming_node:
            return False
        else:
            matching_string, remaining_prefix, remaining_word = incoming_node.match(word)
            if remaining_prefix != "":
                return False
            elif remaining_word == "":
                incoming_node.is_leaf
            else:
                return incoming_node.find(remaining_word)