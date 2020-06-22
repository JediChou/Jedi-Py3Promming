# coding: utf-8

if __name__ == '__main__':
    """演示对象引用操作: 不同类型的值也可交换"""

    var1, var2 = 123, "四五六"
    var1, var2 = var2, var1
    print(var1, var2)  # 体现Python是动态语言的特性
