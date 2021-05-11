# W dowolny sposób ponumeruj wierzchołki grafu miasteczka:
#
# Korzystając z dowolnej metody reprezentacji grafu zapisać istniejące połączenia pomiędzy budynkami.
#
# Wyświetl wszystkie krawędzie parami, podzielone za pomocą ---

graph = {
    'dom': ['szkola', 'kosciol', 'bar'],
    'szkola': ['szpital', 'dom'],
    'szpital': ['szkola', 'bar', 'kino', 'teatr'],
    'teatr': ['szpital', 'kino'],
    'kino': ['kosciol', 'szpital', 'teatr'],
    'kosciol': ['dom', 'bar', 'kino'],
    'bar': ['kosciol', 'dom', 'szpital'],
}

for item in graph:
    print('----> krawedzie z ', item)
    for e in graph[item]:
        print(item, '---', e)