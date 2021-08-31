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
>> 1.`self.insert()` - Insert a new TrieNode in the children of this node instance.\ 
>>>Only a single node is create at a time. Therefore, the time and space used is constant.\  
>>>Time complexity = `O(1)`\
>>> Space complexity = `O(1)`
> 
>> 2.`self.suffixes()` - Return suffixes given this instance node.
>>> This method traverse all available child nodes from this instance. This is equivalent to the 
>>> of branches of each node number of available suffix (N). Within each path, we also need to traverse the depth
>>> of the node which is similar to the length of each suffixes (L). Therefore,
>>> the time complexity is `O(N*L)`.
>>> Since this is a recursive function, vraiables are reused - space complexity is constant.\
>>>Time complexity = `O(N*L)`\
>>>Space complexity = O(1)
> 
>> 3.`self.__repr__()` - Represent the Node as `Node(parent, child(ren))`

>**Trie Class**
>> **Attributes**:\
>>`self.root`
> 
>> **Methods**\
>> 1.`self.insert()` - Insert a word into a trie (when word alr there no new nodes are created). 
>>> For every letter of the word, a Node is created (or inserted). Since Node creation is `O(1)`, 
>>> this means that the time complexity is mainly dependent on the length of the word. Therefore,
>>> the time complexity is `O(n)`. The additional space is also dependent on the number of letters
>>> in the inserted word. Henece, Space complexity is also`O(n)`.\
>>> Time complexity = O(n) \
>>> Space complexity = O(n) 
> 
>> 2.`self.find()` - Given a prefix find return the node of the final letter of the prefix. 
>>> This method traverse every letter of the prefix down the trie starting from the root.\
>>> Time complexity = `O(n)`\
>>> Space complexity = `O(1)`