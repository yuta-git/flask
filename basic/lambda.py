"""
lambdaは引数として関数（呼び出し可能なオブジェクト）を指定する場合などに使うと便利。

"""


def add_def(a, b=1):
    return a + b


add_lambda = lambda a, b=1: a + b

print(add_def(3, 4))

print(add_lambda(3, 4))

get_odd_even = lambda x: "even" if x % 2 == 0 else "odd"

print(get_odd_even(3))

l = [0, 1, 2, 3, 4, 5]

map_square = map(lambda x: x**2, l)
print(list(map_square))

l_square = [x**2 for x in l]
print(l_square)

filter_even = filter(lambda x: x % 2 == 0, l)
print(list(filter_even))

l_s = ["apple", "orange", "straqberry"]
print(list(filter(lambda x: not x.endswith("e"), l_s)))
