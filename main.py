def split_binary(bin):
    n = 8
    split_strings = [bin[index : index + n] for index in range(0, len(bin), n)]

    return split_strings


def main():
    BINARY = '10111010AAAAAAAABBBBBBBBCCCCCCCC'

    list = split_binary(BINARY)

    print(list)

    # DECIMAL = int(BINARY, 2)

    # print(DECIMAL)




if __name__ == "__main__":
    main()
