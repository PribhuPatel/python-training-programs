from collections import deque,defaultdict


dic = defaultdict(list)

def add_graph(a,b):
    dic[a].append(b)


def bfs(s):
    visited= []
    qu = deque([s])

    # visited.append(s)
    while qu:
        abc = qu.popleft()
        if abc not in visited:
            print(abc)
            visited.append(abc)
            for i in dic[abc]:
                qu.append(i)

add_graph(0,1)
add_graph(0,2)
add_graph(1,2)
add_graph(2,0)
add_graph(2,3)
add_graph(3,3)


print(dic)
bfs(2)