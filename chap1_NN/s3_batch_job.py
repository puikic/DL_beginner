import numpy as np

if __name__ == '__main__':
    a = np.array([[1,2],[1,3]])
    b = np.array([1,2])
    c = np.dot(a,b)
    print(c, c.shape)
    c = np.dot(b,a)
    print(c, c.shape)