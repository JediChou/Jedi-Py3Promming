# coding: utf-8

if __name__ == "__main__":
    """演示Python的变量定义"""

    # 定义一些变量
    var1 = -973
    bigInteger = 21062458337114373395836055367340864637790190801098222508621955072
    zero = 0
    string1 = "Infinitely Demanding"
    string2 = 'Simon Critchley'
    special_characters = "αβγδεζηθ"

    # 将这些变量放置到list中
    lst = [var1, bigInteger, zero, string1, string2, special_characters]

    # 打印这些变量
    for elt in lst:
        print(elt)
