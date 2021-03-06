class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Bitree:
    def __init__(self, root=None):
        self.root = root

    def preOrder(self, root):  # 先序遍历
        ans, stack = [], [root]
        while stack:
            node = stack.pop()  # 弹出打印，先右后左
            ans.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return ans

    def inOrder(self, root):  # 中序遍历
        ans, stack = [], []
        while stack or root:
            if root:  # 1. 整条左边界依次入栈
                stack.append(root)
                root = root.left
            else:  # 2. 条件1无法时，弹出就打印，来到右，继续条件1
                root = stack.pop()
                ans.append(root.val)
                root = root.right
        return ans

    def posOrder(self, root):  # 后序遍历
        ans, stack = [], [root]
        while stack:
            top = stack[-1]
            if (top.left and top.left != root and top.right != root):  # 左右都没处理
                stack.append(top.left)
            elif (top.right and top.right != root):  # 左边处理完了，右边没处理
                stack.append(top.right)
            else:  # 左右都处理完了
                node = stack.pop()
                ans.append(node.val)
                root = node
        return ans

    def posOrder2(self, root):
        ans, stack = [], [root]
        stack2 = []
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            stack2.append(node)

        for i in stack2[::-1]:  # 将stack2中的元素出栈，即为后序遍历次序
            ans.append(i.val)
        return ans

    def levelOrder(self, root):  # 层次遍历,可以加个levermap记录节点与层数
        ans, queue = [], [root]
        while queue:
            temp = []
            for i in range(len(queue)):
                node = queue.pop(0)
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(temp)
        return ans

    def DFS(self, root):  # 类似先序遍历
        ans, stack = [], [root]
        while stack:
            node = stack.pop()
            ans.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return ans

    def BFS(self, root):  # 类似层次遍历
        ans, queue = [], [root]
        while queue:
            node = queue.pop(0)
            ans.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return ans


class BuildTree:  # 构造二叉树
    def build(self, preorder, inorder):
        if not preorder:
            return None

        x = preorder.pop(0)
        node = TreeNode(x)
        i = inorder.index(x)

        node.left = self.build(preorder[:i], inorder[:i])
        node.right = self.build(preorder[i:], inorder[i + 1:])
        return node

    def build2(self, preorder, inorder):
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        stack = [root]
        inorderIndex = 0
        for i in range(1, len(preorder)):
            preorderVal = preorder[i]
            if stack[-1].val != inorder[inorderIndex]:
                stack[-1].left = TreeNode(preorderVal)
                stack.append(stack[-1].left)
            else:
                while stack and stack[-1].val == inorder[inorderIndex]:
                    node = stack.pop()
                    inorderIndex += 1
                node.right = TreeNode(preorderVal)
                stack.append(node.right)
        return root


def printTree(root):  # 打印整棵树的打印函数
    if not root:
        return
    print('Binary Tree:')
    printInOrder(root, 0, 'H', 17)


def printInOrder(root, height, preStr, length):  # 打印整棵树的打印函数
    if not root:
        return
    printInOrder(root.right, height + 1, 'v', length)
    string = preStr + str(root.val) + preStr
    leftLen = (length - len(string)) // 2
    rightLen = length - len(string) - leftLen
    res = " " * leftLen + string + " " * rightLen
    print(" " * height * length + res)
    printInOrder(root.left, height + 1, '^', length)


if __name__ == "__main__":
    treeroot = TreeNode("A", TreeNode("B", TreeNode("D"), TreeNode("E", TreeNode('H'))),
                        TreeNode("C", TreeNode("F"), TreeNode("G")))
    t = Bitree()
    print("preOrder:", t.preOrder(treeroot))
    print("inOrder:", t.inOrder(treeroot))
    print("posOrder:", t.posOrder(treeroot), t.posOrder2(treeroot))
    print("levelOrder:", t.levelOrder(treeroot))
    print("DFS:", t.DFS(treeroot))
    print("BFS:", t.BFS(treeroot))

    preorder, inorder = [3, 9, 8, 5, 4, 6, 10, 20, 15, 7], [4, 5, 6, 8, 10, 9, 3, 15, 20, 7]
    b = BuildTree()
    printTree(b.build(preorder, inorder))
