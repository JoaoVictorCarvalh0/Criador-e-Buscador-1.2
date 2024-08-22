import random
import os
from memory_profiler import profile
import time
import psutil

def criar_arquivo(nome_arq, quant_num=1000000):
    with open(nome_arq, 'w') as arquivo:
        for _ in range(quant_num):
            numero = random.randint(1, 1000000000000)
            arquivo.write(f"{numero}\n")
    print(f"Arquivo {nome_arq} criado com {quant_num} números.")

def procurar_numero(nome_arq, numero_procurado):
    with open(nome_arq, 'r') as arquivo:
        for linha in arquivo:
            if int(linha.strip()) == numero_procurado:
                return True
    return False

@profile
def main():
    nome_arq = "numerosTri.txt"
    num_procurado = random.randint(1, 1000000000000)
    print(f"Procurando pelo número {num_procurado}...")
    encontrou = False

    while not encontrou:
        criar_arquivo(nome_arq)
        encontrou = procurar_numero(nome_arq, num_procurado)

        if encontrou:
            print(f"Número {num_procurado} encontrado no arquivo!")
            break 
        else:
            print(f"Número {num_procurado} não encontrado. Excluindo arquivo e criando um novo.")
            os.remove(nome_arq)

if __name__ == "__main__":
    process = psutil.Process()

    start_time = time.time()
    start_memory = process.memory_info().rss / (1024 * 1024)

    main()
    
    end_time = time.time()
    end_memory = process.memory_info().rss / (1024 * 1024)

    print(f"Tempo de execução: {end_time - start_time:.2f} segundos")
    print(f"Uso de memória: {end_memory - start_memory:.2f} MB")
    print(f"Uso de CPU: {psutil.cpu_percent(interval=1)}%")
