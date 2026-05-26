class TriNode:
    def __init__(self):
        self.children = []
        self.wordEnd = False
        self.val = ""

class PrefixTree:
    def __init__(self):
        self.root = TriNode()

    def insert(self, word: str) -> None:
        def dfs_insert(root, remWord):
            if not remWord:
                root.wordEnd = True  # ✅ fixed typo
                return

            char = remWord[0]
            for node in root.children:
                if node.val == char:
                    dfs_insert(node, remWord[1:])
                    return

            newNode = TriNode()
            newNode.val = char
            root.children.append(newNode)
            dfs_insert(newNode, remWord[1:])
        
        dfs_insert(self.root, word)

    def search(self, word: str) -> bool:
        def dfs_search(root, remWord):
            if not remWord:
                return root.wordEnd  # ✅ don’t set it
            
            char = remWord[0]
            for node in root.children:
                if node.val == char:
                    return dfs_search(node, remWord[1:])
            return False
        
        return dfs_search(self.root, word)

    def startsWith(self, prefix: str) -> bool:
        def dfs_search(root, remWord):
            if not remWord:
                return True
            char = remWord[0]
            for node in root.children:
                if node.val == char:
                    return dfs_search(node, remWord[1:])
            return False
        
        return dfs_search(self.root, prefix)
