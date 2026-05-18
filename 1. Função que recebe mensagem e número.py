def mostrar_mensagem_numero(mensagem, numero):
    print("Mensagem:", mensagem)
    print("Número:", numero)


def main():
    msg = input("Digite uma mensagem: ")
    num = int(input("Digite um número: "))

    mostrar_mensagem_numero(msg, num)


if __name__ == "__main__":
    main()