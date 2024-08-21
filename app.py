import random
import cProfile

def criar_arquivo(nome_arq, quant_num=1000000):
    with open(nome_arq, 'w') as arquivo:
        for _ in range(quant_num):
            numero = random.randint(1, 1000000)
            arquivo.write(f"{numero}\n")
    print(f"Arquivo {nome_arq} criado com {quant_num} números.")

def procurar_numero(nome_arq, numero_procurado):
    with open(nome_arq, 'r') as arquivo:
        for linha in arquivo:
            if int(linha.strip()) == numero_procurado:
                return True
    return False

def main():
    nome_arq = "numeros.txt"
    num_procurado = random.randint(1, 1000000)
    encontrou = False

    while not encontrou:
        criar_arquivo(nome_arq)
        encontrou = procurar_numero(nome_arq, num_procurado)

        if encontrou:
            print(f"Número {num_procurado} encontrado no arquivo!")
            break 
        else:
            print(f"Número {num_procurado} não encontrado. Recriar arquivo")

if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()
    
    main()
    
    profiler.disable()
    profiler.print_stats(sort='cumtime')
