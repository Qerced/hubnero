def gain(items):
    return sum([item['price'] * item['quantity'] for item in items])


if __name__ == '__main__':
    print(gain(
        [
            {'name': 'Футболка', 'price': 20, 'quantity': 2},
            {'name': 'Джинсы', 'price': 50, 'quantity': 1},
            {'name': 'Носки', 'price': 5, 'quantity': 10},
            {'name': 'Штаны', 'price': 30, 'quantity': 1}
        ]
    ))
