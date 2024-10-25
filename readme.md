# Тестовое задание "Hubnero"

## [Требования](#требования)

### Основные требования:

- [x] Напишите функцию, которая берет список неотрицательных целых чисел и строк и возвращает новый список с отфильтрованными числами.
- [x] Напишите функцию accum:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
- [x] Напишите функцию, которая выдаёт сумму выручку на основании входного формата данных
const products = [
{ name: 'Футболка', price: 20, quantity: 2 },
{ name: 'Джинсы', price: 50, quantity: 1 },
{ name: 'Носки', price: 5, quantity: 10 },
{ name: 'Штаны', price: 30, quantity: 1 }
];

## [Запуск](#запуск)

Решение с фильтрацией чисел представлено в [nums_filter.py](nums_filter.py):
```bash
python ./nums_filter.py
```

Реализация функции accum находится в [accum.py](accum.py):
```bash
python ./accum.py
```

Сумму выручки можно рассчитать с помощью [gain.py](gain.py):
```bash
python ./gain.py
```
