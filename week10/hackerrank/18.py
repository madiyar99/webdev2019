def split_and_join(line):
    lis = list(line.split(" "))

    lis = "-".join(lis)
    return lis


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

