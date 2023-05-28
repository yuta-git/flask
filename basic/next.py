"""
イテレータは、「繰り返し可能なオブジェクト（イテラブル）の分身のようなオブジェクト」のことを指します。
イテレータは「イテレータの先頭要素を取得するために用いる関数」であるnext関数を使うことによって先頭要素を取得することが可能です。
"""
list_a = [1, 2, 3, 4, 5]
iter_a = iter(list_a) # iter() イテレータに変換()
print(next(iter_a))
print(next(iter_a))
print(next(iter_a))
print(next(iter_a))
print(next(iter_a))
print(next(iter_a))