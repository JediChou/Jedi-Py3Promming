# coding: utf-8

if __name__ == '__main__':
    """演示对象引用操作: 赋值"""

    # 初始化
    x = "blue"
    y = "red"
    z = x

    # 步骤1
    print("step 1: initialize")
    print("x", x)
    print("y", y)
    print("z", z)

    # 步骤2
    z = y
    print("step 2: z = y")
    print("x", x)
    print("y", y)
    print("z", z)

    # 步骤3
    x = z
    print("step 3: x = z")
    print("x", x)
    print("y", y)
    print("z", z)
