from random import randint

class NumberGuessingGame:
    @staticmethod
    def jogar() -> None:
        while True:
            numero_secreto = randint(0, 100)
            contador: int = 0

            while True:
                try:
                    chute = int(input("Digite um número de 0 a 100: "))

                except ValueError:
                    print("Entrada inválida. Digite um número inteiro.")
                    continue

                if chute == numero_secreto:
                    print(f"Parabéns! Você acertou o número {numero_secreto} em {contador} Tentativas.")
                    break

                contador += 1
                print("Seu número é MENOR que o número secreto." if chute < numero_secreto
                      else "Seu número é MAIOR que o número secreto.")

            continuar = input("Quer jogar novamente? [S/N] ").strip().upper()

            if continuar != "S":
                print("Parando o jogo...")
                break

if __name__ == "__main__":
    NumberGuessingGame.jogar()
