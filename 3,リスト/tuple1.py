# ◆ タプル ◆

# タプル(tuple) … 複数のデータをまとめて扱う事が可能。
# タプルは要素の追加、削除、変更ができない。
# タプルは要素をカッコ()で囲んで定義する
a = ('dog', 'cat', 'bird')
print(a)

# タプルに含まれる要素の変更は不可能だが、
# タプル同士をつなげて新しいタプルを定義することは可能。
b = (12, 34)
print(b)

c = a + b
print(c)
