from itertools import permutations

V = 8
INT_MAX = 1000000
vertex = []
cities = ["Mumbai","goa","aurangabad","Dharwad","Hyderabad","Chennai","Bangalore","Thrissur" ]


def tsp(graph, s):
    global vertex, cities
    for i in cities:
        if i != s:
            vertex.append(i)
    min_path = INT_MAX
    perm = list(permutations(vertex))
    for j in perm:
        current_pathweight = 0
        k = s
        vertex = j
        for i in vertex:
            current_pathweight += graph[k][i]
            k = i
        current_pathweight += graph[k][s]
        h = list(j)
        h.insert(0, s)
        h.append(s)
        print("path:", h, " path cost:", current_pathweight)
        if current_pathweight < min_path:
            min_path = current_pathweight
            l = list(j)
    l.insert(0, s)
    l.append(s)
    print("minimum cost path:", l, "\n path cost:", min_path)


graph = {"Mumbai":{ "goa":605, "aurangabad":349,"Dharwad": 552,"Hyderabad": 710,"Chennai":     1334,"Bangalore": 980, "Thrissur":1351},
         "goa":{"Mumbai":605, "aurangabad":645, "Dharwad":130, "Hyderabad":677, "Chennai":968, "Bangalore":560, "Thrissur":701},
         "aurangabad":{"Mumbai":349, "goa":645, "Dharwad":612, "Hyderabad":564, "Chennai":1201, "Bangalore":930, "Thrissur":1301},
         "Dharwad":{"Mumbai":552, "goa":130,"aurangabad": 612,  "Hyderabad":506,"Chennai": 790, "Bangalore":437, "Thrissur":808},
         "Hyderabad":{"Mumbai":710, "goa":677, "aurangabad":564, "Dharwad":506,"Chennai":627, "Bangalore":569, "Thrissur":1048},
         "Chennai":{"Mumbai":1334, "goa":968, "aurangabad":1201, "Dharwad":790, "Hyderabad":627, "Bangalore":347, "Thrissur":616},
         "Bangalore":{"Mumbai":980, "goa":560,"aurangabad": 930, "Dharwad":437,"Hyderabad": 569, "Chennai":347, "Thrissur":473},
         "Thrissur":{"Mumbai":1351,"goa": 701, "aurangabad":1301,"Dharwad": 808, "Hyderabad":1048, "Chennai":616, "Bangalore":473,}}

tsp(graph, "Mumbai")
