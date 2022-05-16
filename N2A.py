# With em conjunto com o open é uma função de python que permite abrir um arquivo "as file"
# Em seguida, dentro do operador with, o arquivo é lido dentro de uma variável chamada contents
# Após, o conteúdo da variável é transformado em um array

print('Giovanni Oliveira da Silva')
print('Guilherme Castilho')
print('Guilherme Maciel')
print('Renato Caetité Cruz')
print('=' * 42)
print('Totalização Simples de Vendas de Produtos\n')

#Array que recebe os dados do .txt
arrFile = []
#Matriz que contém os array dos produtos.
arrProdutos = []
#Variável que recebe a multiplicação entre a quantidade vendida e o preço.
totVend = 0.0
#soma total das vendas.
soma = 0.0

#Abertura do .txt
with open("vendas.txt") as file:
    #Atribuição do .txt para uma string
    contents = file.read()
    #conversão da string para array
    arrFile = contents.split("\n")

    #Atribuição dos itens do array "arrFile" a matriz "arrProdutos"
    i = 0
    while i < len(arrFile):
        arrProdutos.append(arrFile[i].split(';'))
        i += 1

    #Operação de busca pelo ID do produto
    valor = int(input("Digite o código: "))
    while valor != 0:
        #Validação do ID
        if valor < 10000 or valor > 21000:
            print("{} Código inválido (deve ser entre 10000 e 21000)".format(valor))
            valor = int(input("Digite o código: "))
        else:
            #Operação de cálculo do total vendido por ID
            i = 0
            while i < len(arrProdutos):
                if str(valor) in arrProdutos[i]:
                    totVend = float(arrProdutos[i][1]) * float(arrProdutos[i][2])
                    soma += totVend
                i += 1      

            print("Total vendido do produto {} = R$ {:.2f}".format(valor, soma))
            valor = int(input("Digite o código: "))
            soma = 0.0
            totVen = 0.0

print("Fim do programa")





