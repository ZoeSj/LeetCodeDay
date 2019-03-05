# @File    : maximum_depth_of_binary_tree.py
# @Date    : 2019-03-05
# @Author  : shengjia
input = [3, 9, 20, '', '', 15, 7]


def depth(root):
    depth = 0
    l = [root] if root else []
    while l:
        depth += 1
        queue = []
        for el in l:
            if el.left:
                queue.append(el.left)
            elif el.right:
                queue.append(el.right)
        l = queue
    return depth


print(depth(input))
