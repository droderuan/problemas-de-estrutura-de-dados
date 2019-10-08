''' 
                    Desafio HackerRank - Maximize It!
                    Resolvido por: Ruan Ferreira

        Meu entendimento: Basicamente será uma função recursiva que
        sempre irá se instânciar quando ainda não chegamos no final
        "da matriz". A ideia é um deslocamento vertical sempre que puder,
        quando chegar no final do array, passará a se deslocar verticalmente
        checando todas as possibilidades e então volta para onde foi chamada.
        Não é a melhor opção em desempenho mas funcionou :D
'''


inputs = list(map(int, input().split(' ')))
array = []
linha_total = inputs[0]-1
M = inputs[1]
modMax = 0

for i in range(inputs[0]):
    array.append(list(map(int, input().split(' '))))

for x in range(len(array)):
    array[x].pop(0)

def calcModMax(soma=0, linha=0):
    for index in range(len(array[linha])):
        if linha<linha_total:   #checa se pode descer mais
            y = linha           #deve ser feito isso para manter o valor da linha
            y += 1              #em sua respectiva instância
            x = soma + (array[linha][index]**2)
            calcModMax(x, y)
        else:
            for x in array[linha]:  #verifica o calculo e ve se achou o maior mod
                t = (soma +(x**2))%M
                global modMax
                if (t> modMax):
                    modMax = t

calcModMax()

print(modMax)