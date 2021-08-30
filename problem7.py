class RouteTrieNode:
    def __init__(self, path):
        self.path = path
        self.children = dict()
        self.absolutePath = None

    def insert(self, path):
        if path not in self.children:
            self.children[path] = RouteTrieNode(path)
            self.children[path].set_absolutePath(self.absolutePath)

    def set_absolutePath(self, prefix):
        self.absolutePath = f'{prefix}{self.path}/'

    def __repr__(self):
        '''Node path, child node(s)'''
        return f'Node({self.absolutePath}, child_nodes={[i for i in self.children.keys()]})'



class RouteTrie:
    def __init__(self):
        self.root = RouteTrieNode('')
        self.root.set_absolutePath('')

    def insert(self, longPath):
        paths = longPath.split('/')
        paths = self._cleanPathLists(paths)
        tracerNode = self.root
        for path in paths:
            if path in tracerNode.children:
                tracerNode = tracerNode.children[path]
            else:
                tracerNode.insert(path)
                tracerNode = tracerNode.children[path]

    def find(self, longPath):
        paths = longPath.split('/')
        paths = self._cleanPathLists(paths)
        node_tracer = self.root
        for path in paths:
            node_tracer = self._finder(path, node_tracer)
        return node_tracer

    def _finder(self, path, node_tracer):

        if path in node_tracer.children:
            return node_tracer.children[path]
        elif len(node_tracer.children) != 0:
            for childNode in node_tracer.children.values():
                self._finder(path,childNode)

    def _cleanPathLists(self, arr):
        '''
        Remove empty elements from list.
        e.g., ["","a", "b", "", "c"] -> ["a","b", "c"]
         '''
        return filter(lambda x: x != '', arr)





class Router:
    def __init__(self):
        self.trie = RouteTrie()
        self.handler = None

    def add_handler(self, handler):
        self.handler = handler

    def lookup(self):
        pass

    def split_path(self):
        pass



route1 = RouteTrie()
route1.insert('home/users/user1')
route1.insert('home/users/user2')
route1.insert('home/bin/')
route1.insert('home/bin2/')
# a.root.children['home'].children

print(route1.find('/home/users'))
print(route1.find('/home/bin'))
