#grupo: igor melo, marco e gustavo

from time import sleep
import random

cores = ["Vermelho", "Amarelo", "Verde"]

processo_semaforo1 = [["X", 3], ["Z", 5]]
processo_semaforo2 = [["Y", 7], ["O", 2]]

def executar_processos(processos):
    for processo in processos:
        while processo[1] > 0:
            processo[1] -= 1
            print(processo)
            sleep(0.3)

def alocar_memoria():
    tamanho = int(input("Qual é o tamanho do programa de 1 a 4? "))
    algoritmo = input("First-fit (f), Best-fit (b), Worst-fit (w)\nQual algoritmo você deseja usar? ")
    tipo = ["outro app", "livre"]
    lista = []
    memoria = 0
    espaco_escolhido = 0

    while memoria < 40:
        x = random.randrange(1, 6)
        y = random.choice(tipo)
        if y == "livre":
            lista.append(x)
            memoria += x

    print("Lista de espaços disponíveis:", lista)

    if tamanho > 4:
        print("Tamanho inválido, reinicie o programa")
    else:
        if algoritmo == "f":
            for i in range(len(lista)):
                if tamanho <= lista[i]:
                    espaco_escolhido = i
                    print(f'O espaço livre de índice "{espaco_escolhido}" foi o escolhido')
                    break
        elif algoritmo == "b":
            for i in range(len(lista)):
                if tamanho <= lista[i]:
                    espaco_escolhido = i
                    break
            if espaco_escolhido == 0:
                for i in range(len(lista)):
                    if tamanho + 1 == lista[i]:
                        espaco_escolhido = i
                        break
            if espaco_escolhido == 0:
                for i in range(len(lista)):
                    if tamanho + 2 == lista[i]:
                        espaco_escolhido = i
                        break
            print(f'O espaço livre de índice "{espaco_escolhido}" foi o escolhido')
        elif algoritmo == "w":
            espaco_escolhido = lista.index(max(lista))
            print(f'O espaço livre de índice "{espaco_escolhido}" foi o escolhido')
        else:
            print("Algoritmo inválido")

for cor in cores:
    if cor == "Vermelho":
        print(f"\nSemáforo 1 {cor} ligado")
        print(f"Semáforo 2 Verde ligado\n")
        print(f"Os Processos do Semáforo 2 começam a rodar")
        executar_processos(processo_semaforo2)
        alocar_memoria()
    elif cor == "Verde":
        print(f"\nSemáforo 1 {cor} ligado")
        print(f"Semáforo 2 Vermelho ligado\n")
        print(f"\nOs Processos do Semáforo 1 começam a rodar")
        executar_processos(processo_semaforo1)
        alocar_memoria()
    else:
        print(f"\nSemáforo 1 Vermelho ligado")
        print(f"Semáforo 2 Amarelo ligado\n")