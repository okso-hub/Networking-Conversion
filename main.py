from os import system, name


def clear(): system("clear") if name == "posix" else system("cls")


def split_binary(bin):
    n = 8
    split_strings = [bin[index : index + n] for index in range(0, len(bin), n)]

    return split_strings


def generate_ip(binaries):
    decimals = []

    for i in binaries:
        decimals.append(int(i, 2))

    ip = ""

    for i in decimals:
        ip += str(i)
        ip += "."

    return ip[:-1]


getbinary = lambda x, n: format(x, 'b').zfill(n)


def generate_binary(ip):
    binary = ""

    for i in ip.split("."):
        binary += getbinary(int(i), 8)

    return binary


def main():
    choice = int(input("Choose a mode: \n1: Binary to IP \n2: IP to binary\n"))

    if choice == 1:
        BINARY = input("Enter binary number: ")
        list = split_binary(BINARY)
        IP_ADDRESS = generate_ip(list)
        clear()
        print(f"Binary number: {BINARY} \nIP address: {IP_ADDRESS}")

    elif choice == 2:
        IP = input("Enter IP adress: ")
        solution = generate_binary(IP)
        clear()
        print(f"IP Adress: {IP} \nBinary number: {solution}")
    

if __name__ == "__main__":
    main()
