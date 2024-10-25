def filter_numbers(data):
    return [num for num in data if isinstance(num, int)]


if __name__ == '__main__':
    print(filter_numbers([1, 'hello', 3, 0, 'world', 5]))
