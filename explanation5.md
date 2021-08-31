# Problem 5: Autocomplete with Tries
by Cephas Tan Li-Jie
## Assignment description
Using a trie data structure to apply autocomplete. The coding environment I use is Pycharm, 
but this assignment uses Ipython widgets. Therefore, my final solution is in the jupyter notebook file.  

## Method of implementation
Each letter of a word is treated as a node. The first node of the trie is just
a "root" node - no letters are assigned to it. The first letter of a word is assigned as
the child Node of this root node and subsequent letters form the child of each subsequent node.
At the last letter node is tagged as a final letter of a word with the `self.is_word`boolean attribute 
(assigned as <span style="color:blue">True</span>). The children attribute uses a dictionary dataStructure to allow
O(1) time complexity to retrieve child nodes.

>**TrieNode Class**
>> **Attributes**:
>>
>> 1.`self.value` - Letter (e.g., 'a', 'b'...)\
>> 2.`self.children` - Dictionary of next available letter of a prefix.\
>> 3.`self.is_word` - bool attribute to identify if this letter/node is the last letter/node of a word.
> 
>> **Methods**\
>> 1.`self.insert()` - Insert a new TrieNode in the children of this node instance. Time complexity = O(1)\
>> 2.`self.suffixes()` - Return suffixes given this instance node. Time complexity = O(NumberOfAvailableSuffix*LengthOfSuffixes)\
>> 3.`self.__repr__()` - Represent the Node as `Node(parent, child(ren))`

>**Trie Class**
>> **Attributes**:\
>>`self.root`
> 
>> **Methods**\
>> 1.`self.insert()` - Insert a word into a trie (when word alr there no new nodes are created). Time complexity O(n) \
>> 2.`self.find()` - Given a prefix find all available suffix. Time complexity O(PrefixLength*NumberOfNodeBranches).