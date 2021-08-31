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
>> 1.`self.insert()` - Insert a new TrieNode in the children of this node instance. Time complexity = O(1)\
>> 2.`self.set_absolutePath()` - Set the absolutePath (aka the prefix). Time complexity = O(1)\
>> 3.`self.set_handler()` - Set the handler. Time complexity = O(1)\
>> 4.`self.__repr__()`  - represent the node as`Node path, child node(s)`

>**RouteTrie Class**
> 
>> **Attributes**:\
>>`self.root` - The root node directory.
> 
>> **Methods**\
>> 1.`self.insert()` - Insert a new TrieNode in the children of this node instance. Time complexity = O(1)\
>> 2.`self.find()` - Return suffixes given this instance node. Time complexity = O(num of paths in long path * num of available paths)\
>>3.`self._finder()` - Recursive Helper method for the `self.find()` method. Time complex = O(number of available paths)
>> 4.`self._cleanPathLists()` - Helper function to managed empty elements after splitting longPaths with '/'. 

>**Router Class**
>> **Attributes**:\
>> `self.trie` - Initiate a RouteTrie Class
> 
>> **Methods**\
>> 1.`self.add_handler()` - Create a path if not present and assign the handler to the path node. Time complexity = O(1)\
>> 2.`self.lookup()` - Finds and prints the Node given the long path using the RouteTrie method. Return None is no path available. Time complexity = O(num of paths in long path * num of available paths)\
>> 3.`self.split_path` - Not neccessary here because this component is already implemented in my Trie and TrieNode classes.