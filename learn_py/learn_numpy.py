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