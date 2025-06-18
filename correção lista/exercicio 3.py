def calculadiametro(raio):
    return 2* raio

def calculacircuferencia(pi, raio):
    return pi* raio * 2

def calculaareacircuferencia(pi, raio):
    return pi * (raio**2)

#main
raio = float(input("Digite o valor do raio:"))
pi = 3.14159

diametro = calculadiametro(raio)
circuferencia = calculacircuferencia (pi, raio)
area = calculaareacircuferencia(pi, raio)

print("o diametro é de :", diametro)
print("a medida da circuferencia:", circuferencia)
print("a medida da circuferencia é de:", area)