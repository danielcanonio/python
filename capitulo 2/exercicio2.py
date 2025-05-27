precocapalivro = 24.95
precocapalivrodesconto = precocapalivro - (precocapalivro * 0.40)
custofreteprimeiroexemplar = precocapalivrodesconto + 3.00
custofreterestanteexemplares = precocapalivro + 0.75
custotalatacado = custofreteprimeiroexemplar + (custofreterestanteexemplares * 59)

print("o preco total de atacado para 60 exemplares é de: ", custotalatacado)