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


def generate_network_adress(ip, sub):
    network_address = ""

    IP = generate_binary(ip)
    SUB = generate_binary(sub)

    for i in range(32):
        if IP[i] == "1" and SUB[i] == "1":
            network_address += "1"
        else:
            network_address += "0"
    
    return generate_ip(split_binary(network_address))


def generate_device_part(ip, sub):
    device_part = ""

    ip = generate_binary(ip)
    sub = generate_binary(sub).replace("1", "a").replace("0", "1").replace("a", "0")

    for i in range(32):
        if ip[i] == "1" and sub[i] == "1":
            device_part += "1"
        else:
            device_part += "0" 

    return generate_ip(split_binary(device_part))


def generate_broadcast(ip, sub):
    ip = generate_binary(ip)
    sub = generate_binary(sub).replace("0", "a")
    sub_ones = sub.count("a")

    size = len(ip)
    new_ip = ip[:size - sub_ones]

    for i in range(sub_ones):
        new_ip += "1"

    return generate_ip(split_binary(new_ip))


def generate_default_gateway(ip, sub):
    network_address = generate_network_adress(ip, sub)
    
    network_address = network_address[:-1] + "1"

    return network_address


def generate_max_ip(ip="10.0.0.15", sub="255.0.0.0"):
    broadc = generate_broadcast(ip, sub).split(".")
    max_ip = ""
    
    last = int(broadc[-1]) - 1

    broadc[-1] = str(last)

    for i in broadc:
        max_ip += f"{i}."

    return max_ip[:-1]


def main():
    choice = int(input("Choose a mode: \n1: Binary to IP \n2: IP to binary \n3: Generate everything else\n"))

    if choice == 1:
        clear()
        BINARY = input("Enter binary number: ")
        list = split_binary(BINARY)
        IP_ADDRESS = generate_ip(list)
        clear()
        print(f"Binary number: {BINARY} \nIP address: {IP_ADDRESS}")

    elif choice == 2:
        clear()
        IP = input("Enter IP adress: ")
        solution = generate_binary(IP)
        clear()
        print(f"IP Adress: {IP} \nBinary number: {solution}")
    elif choice == 3:
        clear()
        ip = str(input("Enter IP Address: "))
        sub = str(input("Enter Subnet Mask: "))

        network_address = generate_network_adress(ip, sub)
        device_part = generate_device_part(ip, sub)
        broadcast = generate_broadcast(ip, sub)
        default_gateway = generate_default_gateway(ip, sub)
        max_ip = generate_max_ip(ip, sub)

        print(f"\nNetwork Address: {network_address} \nDevice Part: {device_part} \nBroadcast: {broadcast} \nDefault Gateway: {default_gateway} \nMax IP: {max_ip}")


if __name__ == "__main__":
    main()
