import re

def maskify(cc):
    # Utiliza a compreensão de lista para substituir todos os caracteres, exceto os últimos 4, por '#'.
    # A compreensão de lista itera sobre os caracteres em 'cc' e seus índices usando a função enumerate().
    # Para cada caractere, se seu índice for menor que o comprimento de 'cc' menos 4, ele é substituído por '#'.
    # Caso contrário, o caractere permanece inalterado.
    masked_cc = [ "#" if i < len(cc) - 4 else char for i, char in enumerate(cc)]

    # Junta a lista de caracteres em uma única string e retorna o resultado.
    return "".join(masked_cc)

def main():
    # Exemplo de entrada
    cc = "1234567890123456"

    # Chama a função maskify com a entrada de exemplo e armazena o resultado
    masked_cc = maskify(cc)

    # Imprime o resultado
    print(f"Original: {cc}\nMasked:   {masked_cc}")

if __name__ == "__main__":
    main()