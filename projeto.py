produto = 0
valor = 0
lista = []
listavalor = []
soma = 0
clube = 0
juncao = 0
mud_valor = 0
intem = 0
while True:
    produto = str(input("Digite o nome do produto: "))
    if produto == "sair":
        break
    valor = float(input("Informe o Valor do Produto: "))
    soma = soma + valor
    mud_valor = str(valor)
    juncao = (produto + ' = ' + 'R$'+mud_valor)
    lista.append(juncao)
    print(lista)
clube = str(input("Está participando do Clube?")).lower()
print("\n")
if clube == "sim":
    soma = soma - 1.20
    print(f"O valor da compra foi de: R${soma} (Com Clube 20% OFF)")
    print("-------------------------------------------------------")
else:
    print(f"O valor da compra foi de: R${soma} (Sem Clube)"'\n')
    print("---------------------------------------------------")
print("\n")
print("Nota Fiscal")
print("_____________________")
for intem in lista:
    print(f"{intem}")
print(f"Total a pagar: R${soma}")