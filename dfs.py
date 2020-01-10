from collections import deque,defaultdict


dic = defaultdict(list)

def add_graph(a,b):
    dic[a].append(b)


def dfs(s):
    visited= []
    stack = [s]

    # visited.append(s)
    while stack:
        abc = stack.pop()
        if abc not in visited:
            # print(abc)
            visited.append(abc)
            for i in reversed(dic[abc]):
                stack.append(i)
    print(visited)
    print(stack)
add_graph(0,1)
add_graph(0,2)
# add_graph(0,3)
add_graph(1,3)
add_graph(2,4)
add_graph(1,4)
add_graph(3,4)
add_graph(3,5)
add_graph(4,5)
# add_graph(2,0)
# add_graph(2,3)
# add_graph(3,3)


print(dic)
dfs(0)