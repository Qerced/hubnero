def accum(data):
    result = data[0].capitalize()
    for i in range(1, len(data)):
        result += '-' + (data[i] * (i + 1)).capitalize()
    return result


if __name__ == '__main__':
    print(accum('abcd'))
    print(accum('RqaEzty'))
    print(accum('cwAt'))
