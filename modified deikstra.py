G = {}
def write_in_graph(a, b, w):
    if a not in G:
        G[a] = {b:w}
    else:
        G[a][b] = w
    if b not in G:
        G[b] = {a:w}
    else:
        G[b][a] = w

def deikstra(G, start):
    sh_path = {vertex:float('+inf') for vertex in G}
    sh_path[start]=0
    Queue=[start]
    while Queue:
        current = Queue.pop(0) # Удаляет i-ый элемент и возвращает его. Если индекс не указан, удаляется последний элемент
        for neig in G[current]:
            offer = sh_path[current]+G[current][neig]
            if offer < sh_path[neig]:
                sh_path[neig] = offer
                Queue.append(neig)
    return sh_path

def get_way(G, start, finish, min_path, shortest_path):
    Way = [finish]
    min_way = min_path
    fired = {finish}
    current = finish
    while current!= start:
        for neighboor in G[current]:
            if neighboor not in fired:
                suggestion = min_way - G[current][neighboor]
                if suggestion == shortest_path[neighboor]:
                    Way.append(neighboor)
                    min_way = suggestion
                    current = neighboor
                    fired.add(neighboor)
    return Way[::-1]

N, M = map(int, input().split())
for i in range(M):
    a, b, w = input().split()
    w = float(w)
    a0, a1 = a + 'a', a + 'b'
    b0, b1 = b + 'a', b + 'b'
    write_in_graph(a1, b0, w)
    write_in_graph(a0, b1, w)

k = int(input())
start, stop = input().split()
start = start + '0'
stop = stop + '0'
sh_path = deikstra(G, start)
path = sh_path[stop]
# Way = get_way(G, start, stop, path, sh_path)
# print(Way)