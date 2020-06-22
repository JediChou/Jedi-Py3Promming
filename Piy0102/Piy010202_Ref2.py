# coding: utf-8

if __name__ == '__main__':
    """演示对象引用操作: 赋值（交换）"""

    # 直接赋值
    a, b = "jedi", "becky"
    print(a, b)

    # 通过赋值的操作进行两个变量的值交换
    a, b = b, a
    print(a, b)
