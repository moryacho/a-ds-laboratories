from math import *
class Graph():
    def __init__(self, tops, distance):
        self.tops = tops
        self.graph = self.create_graph(tops, distance)

    def create_graph(self, tops, distance):
        graph = {}
        for i in tops:
            graph[i] = {}
        graph.update(distance)
        for key1, j in graph.items():
            for key2, value in j.items():
                if graph[key2].get(key1, False) == False:
                    graph[key2][key1] = value
        return graph

    def get_tops(self):
        return self.tops

    def get_neighbors(self, key1):
        pair = []
        for i in self.tops:
            if self.graph[key1].get(i, False) != False:
                pair.append(i)
        return pair

    def value(self, top1, top2):
        return self.graph[top1][top2]


def deikstra(graph, start_top):
    ways = graph.get_tops()
    current_way = {}
    max_value = inf
    for i in ways:
        current_way[i] = max_value
    current_way[start_top] = 0
    while ways:
        min_top = None
        for way in ways:
            if min_top == None:
                min_top = way
            elif current_way[way] < current_way[min_top]:
                min_top = way
        neighbors = graph.get_neighbors(min_top)
        for i in neighbors:
            sum_value = graph.value(min_top, i) + current_way[min_top]
            if sum_value < current_way[i]:
                current_way[i] = sum_value
        ways.remove(min_top)
    return current_way


tops = ['Kazakhstan', 'China', 'Mongolia', 'Russia', 'Kirgisia', 'Usbekistan', 'Tadjikistan', 'Turkmenia', 'Afganistan',
        'Pakistan', 'Iran']
distance = {}
for i in tops:
    distance[i] = {}
distance['Mongolia']['China'] = 1223
distance['Mongolia']['Russia'] = 1591
distance['Russia']['Kazakhstan'] = 2444
distance['China']['Kazakhstan'] = 3361
distance['China']['Russia'] = 4572
distance['Kirgisia']['Kazakhstan'] = 909
distance['Kirgisia']['China'] = 2702
distance['Kirgisia']['Usbekistan'] = 928
distance['Kirgisia']['Tadjikistan'] = 438
distance['Tadjikistan']['Usbekistan'] = 675
distance['Tadjikistan']['China'] = 3034
distance['Tadjikistan']['Afganistan'] = 804
distance['Tadjikistan']['Pakistan'] = 1004
distance['Usbekistan']['Kazakhstan'] = 776
distance['Usbekistan']['Turkmenia'] = 410
distance['Usbekistan']['Afganistan'] = 982
distance['Turkmenia']['Kazakhstan'] = 1133
distance['Turkmenia']['Iran'] = 1049
distance['Turkmenia']['Afganistan'] = 940
distance['Afganistan']['Iran'] = 1223
distance['Afganistan']['Pakistan'] = 504

graph = Graph(tops, distance)
a = input('Введите начальную точку: ')
current_way = deikstra(graph=graph, start_top=a)
print(current_way)