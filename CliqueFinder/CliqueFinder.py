import copy

file = open('input.txt')

def bron_kerbosch(clique:set[str], consider:set[str], ignore:set[str], cliques:list[set[str]]):
    if len(consider) == 0 and len(ignore) == 0:
        if len(clique) > 2:
            cliques.append(clique)
        return
    d, pivot = max([(len(network[v]), v) for v in consider.union(ignore)])
    for vertex in consider.difference(network[pivot]):
        bron_kerbosch(clique.union({vertex}), consider.intersection(network[vertex]), ignore.intersection(network[vertex]), cliques)
        consider.remove(vertex)
        ignore.add(vertex)

network = dict()
found_tris = set()
for line in file:
    sida, sidb = line.strip().split('-')
    if sida not in network:
        network[sida] = {sidb}
    else:
        network[sida].add(sidb)
    if sidb not in network:
        network[sidb] = {sida}
    else:
        network[sidb].add(sida)
    for additional in network[sida].intersection(network[sidb]):
        if sida.startswith('t') or sidb.startswith('t') or additional.startswith('t') and additional != sida and additional != sidb:
            found_tris.add(','.join(sorted([sida, sidb, additional])))

print(len(found_tris))

cliques = []
bron_kerbosch(set([]), set(network.keys()), set([]), cliques)
cliques.sort(key=len, reverse=True)
for i in range(10):
    password = ','.join(sorted(cliques[i]))
    print(len(cliques[i]), password)