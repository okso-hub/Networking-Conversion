from os import system, name


def clear(): system("clear") if name == "posix" else system("cls")


def split_binary(bin):
    n = 8
    split_strings = [bin[index : index + n] for index in range(0, len(bin), n)]

    return split_strings


def generate_decimal(bin, binaries):
    decimals = []

    for i in binaries:
        decimals.append(int(i, 2))

    ip = ""

    for i in decimals:
        ip += str(i)
        ip += "."

    return ip[:-1]


def main():
    BINARY = input("Enter binary number: ")

    list = split_binary(BINARY)

    IP_ADDRESS = generate_decimal(BINARY, list)

    clear()
    print(f"Binary number: {BINARY} \nIP address: {IP_ADDRESS}")
    


if __name__ == "__main__":
    main()
