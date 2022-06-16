# -----------------------------
#                             |
#    github.com/nudimannui4e  |
#                             |
# -----------------------------

"""
 Алгоритм работает следующим образом:
1. Начните с размещения любой вершины графа в конце очереди.
2. Возьмите передний элемент очереди и добавьте его в список посещенных.
3. Создайте список смежных узлов этой вершины.
 Добавьте те, которых нет в списке посещенных, в конец очереди.
4. Продолжайте повторять шаги 2 и 3, пока очередь не опустеет. 

"""


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['B'],
    'E': ['F'],
    'F': ['B', 'E']
}
visited = []  # List to keep track of visited nodes.
queue = []  # Initialize a queue


def bfs(visited, graph, node):
    global queue
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")
        for i in graph[s]:
            if i not in visited:
                visited.append(i)
                queue.append(i)


bfs(visited, graph, 'A')
