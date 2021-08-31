# Problem 7: HTTPRouter using a Trie
by Cephas Tan Li-Jie
## Assignment description
For this exercise we are going to implement an HTTPRouter like you would find in a typical web server using the Trie data structure we learned previously.

## Method of implementation

>**RouteTrieNode Class**
>> **Attributes**:\
>>1.`self.path` - current path.\
>>2.`self.children` - dictionary of path nodes from this path node instance\
>>3.`self.absolutePath` - The full path from the root directory to the current path node.\
>>4.`self.handler` - Handler for this path.
> 
>> **Methods**\
>> 1.`self.insert()` - Insert a new TrieNode in the children of this node instance.\
>>>A simple operation that creates a single node to the child attribute of this node instance. 
> This increment the memory needed at a constant time and space.\
>>>Time complexity = O(1)\
>>>Space complexity = O(1) 
> 
>> 2.`self.set_absolutePath()` - Set the absolutePath (aka the prefix). 
>>> Same as `self.insert`.  
>>>Time complexity = O(1)\
>>> Space complexity = O(1)
> 
>> 3.`self.set_handler()` - Set the handler.
>>> Same as `self.insert`.  
>>>Time complexity = O(1)\
>>> Space complexity = O(1)
> 
>> 4.`self.__repr__()`  - represent the node as`Node path, child node(s)`

>**RouteTrie Class**
> 
>> **Attributes**:\
>>`self.root` - The root node directory.
> 
>> **Methods**\
>> 1.`self.insert()` - Insert a new TrieNode in the children of this node instance. 
>>> Same as `self.insert`.  
>>>Time complexity = O(1)\
>>> Space complexity = O(1)
> 
>> 2.`self.find(longPath)` - Return suffixes given this instance node.
>>> Since the longPath is first split into paths, the algorithm will be dependent
>>> on the number of available paths (P). The algorithm iterates over each possible path
>>> down the trie which means the time complexity is also dependent on the depth of the trie
>>> for each path, also known as the length of each path (L). This component is implemented 
>>> by the `._finder()` method. The space complexity remains constant becuase variables are 
>>> recursive recycled/reused.\
>>> Therefore, the time complexity of this method is `O(L*P)`.\
>>> Time complexity = `O(L*P)`\
>>> Space complexity = `O(1)`
> 
>>3.`self._finder()` - Recursive Helper method for the `self.find()` method.\
>>> See `self.find()` for explanation of Time and space complexity.\
>>> Time complexity = `O(P)`\
>>> Space complexity = `O(1)`
> 
>> 4.`self._cleanPathLists()` - Helper function to managed empty elements after splitting longPaths with '/'. 

>**Router Class**
>> **Attributes**:\
>> `self.trie` - Initiate a RouteTrie Class
> 
>> **Methods**\
>> 1.`self.add_handler()` - Create a path if not present and assign the handler to the path node. 
>>> Same as `self.insert`.  
>>>Time complexity = O(1)\
>>> Space complexity = O(1)
> 
>> 2.`self.lookup()` - Finds and prints the Node given the long path using the RouteTrie method. Return None is no path available. Time complexity = O(num of paths in long path * num of available paths)\
>>> This used `self.find()` method of the RouteTrie class. (see that method for time and space complexity explanation).\
>>> Time complexity = `O(L*P)`\
>>> Space complexity = `O(1)`\
>>> whereby L = length of path and P = number of available paths\
> 
>> 3.`self.split_path` - Not neccessary here because this component is already implemented in my Trie and TrieNode classes.