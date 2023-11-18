import random
from os import system, name

# Função para limpar a tela a cada execução:
def limpar_tela():
    
    # Windows:
    if name == 'nt':
        _ = system('cls')
    
    # Mac ou Linux
    else:
        _ = system('clear')


# Função do jogo
def game():
    
    limpar_tela()
    
    print("\nBem-vindo(a) ao jogo da forca!")
    print("Advinhe a palavra abaixo:\n")
    
    # Lista de palavras para o jogo
    lista_palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']
    
    # Escolhe qual a palavra será usada no jogo
    palavra_escolhida = random.choice(lista_palavras)
    
    # Mostra as letras descobertas
    letras_descobertas = ['_' for letra in palavra_escolhida]
    
    # Número de tentativas
    numero_tentativas = 6
    
    # Armazena letras erradas
    letras_erradas = []
    
    while numero_tentativas > 0:
        
        # Prints na tela
        print(" ".join(letras_descobertas))
        print("\nChances restantes:", numero_tentativas)
        print("Letras erradas:", " ".join(letras_erradas))
        
        # Tentativa
        letra_digitada = input("Digite uma letra: ").lower()
        
        if letra_digitada in palavra_escolhida:
            index = 0
            
            for letra in palavra_escolhida:
                if letra_digitada == letra:
                    letras_descobertas[index] = letra_digitada
                index +=1
        else:
            numero_tentativas -= 1
            letras_erradas.append(letra_digitada)
        
        if "_" not in letras_descobertas:
            print("\nVocê venceu! A palavra era:", palavra_escolhida)
            break
    
    if "_" in letras_descobertas:
        print("\nVocê perdeu, a palavra era:", palavra_escolhida)

# Bloco main
if __name__ == "__main__":
    game()