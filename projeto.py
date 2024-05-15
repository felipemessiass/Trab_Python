produto = 0
valor = 0
lista = []
listavalor = []
soma = 0
clube = 0
juncao = 0
mud_valor = 0
intem = 0
cpf = 0
def func():
    global cpf
    dej_cpf = 0
    dej_cpf = str(input("Cpf na Nota?: ")).lower()
    if dej_cpf == "sim":
        cpf = input("Insira o CPF: ")
        return
func()
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
    print(f"O valor da compra foi de: R${soma} (Sem Clube)")
    print("-----------------------------------------------")
print("Nota Fiscal")
print("-----------")
for intem in lista:
    print(f"{intem}")
print(f"Total a pagar: R${soma}")
print(f"CPF: {cpf}")
