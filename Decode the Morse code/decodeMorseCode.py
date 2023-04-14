import re
from modules.morse_code import MORSE_CODE

def decode_morse(morse_code):
    morse_words = morse_code.strip().split('   ')  # Separa a string do código Morse em palavras usando 3 espaços como separador

    decoded_words = []  # Cria uma lista vazia para armazenar as palavras decodificadas

    for char in morse_words:
        morse_chars = char.split()  # Separa cada caractere Morse em uma lista usando 1 espaço como separador
        decoded_chars = [MORSE_CODE[char] for char in morse_chars]  # Decodifica cada caractere Morse usando o dicionário MORSE_CODE
        decoded_words.append(''.join(decoded_chars))  # Adiciona a palavra decodificada à lista decoded_words

    return ' '.join(decoded_words)  # Converte a lista decoded_words em uma string, unindo as palavras com 1 espaço



def main():
    # Exemplo de uso da função decode_morse
    morse_code = ".... . -.--   .--- ..- -.. ."
    decoded_text = decode_morse(morse_code)
    print(f"Morse code: {morse_code}")
    print(f"Decoded text: {decoded_text}")

if __name__ == "__main__":
    main()
