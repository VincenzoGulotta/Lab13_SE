from model.model import Model

model = Model()

model.crea_grafo()
a,b,c,d = model.crea_connessioni()

for edge in model.G.edges(data = True):
    print(edge)

print(a,b,c,d)

e,f = model.conta_archi_soglia(3)
print(e,f)

g, h = model.ricerca_percorso(3)

print(g,h)
