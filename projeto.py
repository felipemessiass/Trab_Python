produto = 0
valor = 0
lista = []
listavalor = []
soma = 0
clube = 0
while True:
    produto = str(input("Digite o nome do produto: "))
    if produto == "sair":
        break
    valor = float(input("Informe o Valor do Produto: "))
    lista.append(produto)
    listavalor.append(valor)
    soma = soma + valor
    print(f"Lista: {lista}")
    print(f"Valores cadastrados em Reais: {listavalor}")
clube = str(input("Está participando do Clube?"))
if clube == "sim":
    soma = soma - 1.20
print(f"O valor da compra: R${soma}")