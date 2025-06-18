import numpy as np


if __name__ == '__main__':
    a = np.array([1, 2])
    print(a, a.shape)  # NumPy会根据你的运算自动把它作为行向量或列向量对待。
    '''
    一维向量的 shape 为什么是 (2,) 而不是 (2)？
    
    Python 里，(2) 不是元组
        (2) 只是括号里的数字，等价于数字 2 本身，不是元组。
        type((2))  # <class 'int'>
        
        (2,) 才是长度为1的元组（tuple），这是Python规定的语法。
        type((2,))  # <class 'tuple'>
        
    而 NumPy 的 .shape 返回的是一个“元组”，表示每个维度的长度：
    '''
    b = np.array([[3, 4], [5, 6]])
    c = np.dot(a, b)
    print(c, c.shape)
    c = np.dot(b,a)
    print(c, c.shape)

    a = np.array([[1, 2]])
    print(a, a.shape)
    a = np.array([[1], [2]])
    print(a, a.shape)

    arr = np.array([1, 2, 3, 4])  # 形状 (4,) 一维
    # 转换为列向量（二维）,。参数 -1 表示 NumPy 自动计算该维度的大小，而 1 表示新数组的列数为 1。
    reshaped = arr.reshape(-1, 1)
    print("原数组形状:", arr.shape)
    print("新数组形状:", reshaped.shape)
    print("新数组内容:\n", reshaped)
    reshaped = arr.reshape(1, -1)
    print("新数组形状:", reshaped.shape)
    print("新数组内容:\n", reshaped)

    ns = np.random.random(5)  # 生成5个随机数，shape是一维向量(5,)
    print(ns, type(ns), ns.shape)