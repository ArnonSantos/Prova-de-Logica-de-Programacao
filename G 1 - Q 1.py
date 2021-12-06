num = 0
inter = [0,0,0,0]

while (num >= 0):
    num = int(input('Insira um número positivo para começar a contagem e um negativo para encerrar: '))
    if (num >= 0):
        if (num <= 25):
            inter [0] = inter [0] + 1
        elif (num <= 51):
            inter [1] = inter [1] + 1
        elif (num <= 75):
            inter [2] = inter [2] + 1
        elif (num <= 100):
            inter [3] = inter [3] + 1

print ('Intervalos: ' , inter [0], inter [1], inter [2], inter [3])