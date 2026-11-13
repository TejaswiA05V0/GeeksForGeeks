def findCommon(self, r1: 'Node', r2: 'Node') -> list[int]:

        def inorder(node: "Node") -> "Iterator[Node]":
            s = [node]
            while s:
                node = s[-1]
                if node.left:
                    s.append(node.left)
                    node.left = None
                else:
                    s.pop()
                    if node.right:
                        s.append(node.right)
                        node.right = None
                    yield node

        common_values = []
        it1, it2 = inorder(r1), inorder(r2)
        n1, n2 = next(it1, None), next(it2, None)
        while n1 and n2:
            if n1.data == n2.data:
                common_values.append(n1.data)
                n1, n2 = next(it1, None), next(it2, None)
            elif n1.data < n2.data:
                n1 = next(it1, None)
            else:
                n2 = next(it2, None)
        return common_values
