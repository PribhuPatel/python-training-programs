"""Create a python class named Algorithms. It should have following sorting algorithms: Quick sort Bubble sort BFS (
I/P Graph) DFS (I/P Graph) Merge Sort Create a class Sorting which should sort the list provided as input parameter
using the algorithm which is also provided as input parameter. Create a main class which inherits the Sorting class
and calls sort method with list and algorithm to use."""
from collections import deque, defaultdict


# Stores All 5 Algorithms
class Algorithms:
    def quick_sort(self, l, r):
        if l == r:
            return
        k = l
        s = r
        p = self.arr[l]
        l += 1
        while l != r:
            if p <= self.arr[l]:
                if p > self.arr[r]:
                    self.arr[l], self.arr[r] = self.arr[r], self.arr[l]
                else:
                    r -= 1
            else:
                l += 1
        if p > self.arr[r]:
            self.arr[k], self.arr[r] = self.arr[r], p
        self.quick_sort(k, r - 1)
        self.quick_sort(r, s)

    def bubble_sort(self):
        for i in range(0, len(self.arr)):
            temp = True
            for j in range(0, len(self.arr) - i - 1):
                if self.arr[j] > self.arr[j + 1]:
                    temp=False
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
            if temp == True:
                break

    def merge_sort(self, start, end):
        if start == end:
            return
        mid = (end + start) // 2
        self.merge_sort(start, mid)
        self.merge_sort(mid + 1, end)
        s = start
        mt = mid
        mi = self.arr[mid]
        for i in range(mt + 1, end + 1):
            temp = self.arr[i]
            if self.arr[i] <= self.arr[start]:
                for j in range(i, s, -1):
                    self.arr[j] = self.arr[j - 1]
                self.arr[s] = temp
            elif self.arr[start] <= self.arr[i] <= mi:
                k = start
                temp = self.arr[i]
                while self.arr[k] < self.arr[i]:
                    k += 1
                for j in range(i, k, -1):
                    self.arr[j] = self.arr[j - 1]
                self.arr[k] = temp

    def dfs(self, s):
        stack = [s]
        while stack:
            abc = stack.pop()
            if abc not in self.visited:
                self.visited.append(abc)
                for i in reversed(sorted(self.graph[abc])):
                    stack.append(i)

    def bfs(self, s):
        qu = deque([s])

        while qu:
            abc = qu.popleft()
            if abc not in self.visited:
                self.visited.append(abc)
                for i in sorted(self.graph[abc]):
                    qu.append(i)


# Class for Sorting Task
class Sorting(Algorithms):
    def sort(self, algorithm):
        if algorithm == 1:
            self.bubble_sort()
        elif algorithm == 2:
            self.quick_sort(0, len(self.arr) - 1)
        elif algorithm == 3:
            self.merge_sort(0, len(self.arr) - 1)
        else:
            raise Exception("Invalid Input for Sorting")


# Class for Graph traversal Task
class Graph(Algorithms):
    def add_graph(self, a):                     # Add nodes in graph dictionary
        self.graph[a[0]].append(a[1])
        self.graph[a[1]].append(a[0])

    def traverse(self, algorithm):
        if algorithm == 1:
            self.bfs(0)
        elif algorithm == 2:
            self.dfs(0)
        else:
            raise Exception("Invalid Input for Sorting")


class Main(Sorting, Graph):
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = []
        self.arr = []

    def sorting(self):
        try:
            inp = input("Enter Space-saperated Numbers:")
            self.arr = list([int(i) for i in inp.split(" ")])
        except ValueError:
            print("Invalid Input")
            exit(1)
        try:
            inp2 = int(input("1.Bubble Sort\n2.Quick Sort\n3.Merge Sort\nEnter Your Choice: "))
            self.sort(inp2)
            print(self.arr)
        except Exception as e:
            print(e)
            exit(1)

    def graph_traverse(self):
        try:
            inp = int(input("Enter Number of Edges: "))
            for i in range(0, inp):
                inp2 = input("Enter Space saperated from to to: ")
                self.add_graph(list([int(k) for k in inp2.split(" ")]))
        except ValueError:
            print("Invalid Input")
            exit(1)
        try:
            self.visited = []
            inp2 = int(input("1.BFS\n2.DFS\nEnter Your Choice: "))
            inp = int(input("Enter Starting Node: "))
            if inp2 == 1:
                self.bfs(inp)
            elif inp2 == 2:
                self.dfs(inp)
            else:
                raise Exception("Invalid Input for Sorting")
            print(self.visited)
        except Exception as e:
            print(e)
            exit(1)


main = Main()
try:
    inp2 = int(input("1.Sorting\n2.Graph Traverse\nEnter Your Choice: "))
    if inp2 == 1:
        main.sorting()
    elif inp2 == 2:
        main.graph_traverse()
    else:
        raise Exception("Invalid Input for Sorting")
except Exception as e:
    print(e)
    exit(1)
except ValueError:
    print("Enter Valid input")
    exit(1)
