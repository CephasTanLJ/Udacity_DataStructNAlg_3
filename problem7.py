class RouteTrieNode:
    def __init__(self, path, handler=None):
        self.path = path
        self.children = dict()
        self.absolutePath = None
        self.handler=handler

    def insert(self, path):
        if path not in self.children:
            self.children[path] = RouteTrieNode(path)
            self.children[path].set_absolutePath(self.absolutePath)

    def set_absolutePath(self, prefix):
        self.absolutePath = f'{prefix}{self.path}/'

    def set_handler(self, handler):
        self.handler = handler

    def __repr__(self):
        '''Node path, child node(s)'''
        return f'Node({self.absolutePath}, handler= {self.handler}, child_nodes={[i for i in self.children.keys()]})'



class RouteTrie:
    def __init__(self, rootHandler=None):
        self.root = RouteTrieNode('')
        self.root.set_handler(rootHandler)
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
    def __init__(self, root_handler=None):
        self.trie = RouteTrie(root_handler)

    def add_handler(self, longPath, handler):
        '''What does a handler do?'''
        self.trie.insert(longPath)
        self.trie.find(longPath).set_handler(handler)

    def lookup(self, longPath):
        '''returns the handler.'''
        pathNode = self.trie.find(longPath)
        if pathNode is not None:
            print(pathNode.handler)
            return pathNode.handler # for my assert test
        else:
            print(None)
            return None

    def split_path(self, longPath):
        return list(filter(lambda x: x != '', longPath.split('/')))




def test():
    # Here are some test cases and expected outputs you can use to test your implementation

    # create the router and add a route
    router = Router("root handler") # remove the 'not found handler' if you did not implement this
    router.add_handler("/home/about", "about handler")  # add a route

    # some lookups with the expected output
    assert router.lookup("/") == 'root handler' # should print 'root handler'
    assert router.lookup("/home") == None # should print 'not found handler' or None if you did not implement one
    assert router.lookup("/home/about") == 'about handler' # should print 'about handler'
    assert router.lookup("/home/about/") == 'about handler' # should print 'about handler' or None if you did not handle trailing slashes
    assert router.lookup("/home/about/me") == None # should print 'not found handler' or None if you did not implement one

def testEdgeCase1():
    '''If multiple // are returned between path, ignore the extra //'''
    router = Router("root handler")  # remove the 'not found handler' if you did not implement this
    router.add_handler("/home/about", "about handler")  # add a route
    router.add_handler("/home//about",'new handler')
    assert router.lookup("/home//about") == 'new handler', 'add handler did not ignore the extra "/" in the add_handler method'


def testEdgeCase2():
    '''PAth do not exist'''
    router = Router("root handler")  # remove the 'not found handler' if you did not implement this
    router.add_handler("/home/about", "about handler")  # add a route
    assert router.lookup("PathThatDoNotExists") == None, f'Router lookup path that do not exists did not return None, {router.lookup("PathThatDoNotExists")} was returned instead.'

if __name__ == '__main__':
    testEdgeCase1()
    testEdgeCase2
    test()
