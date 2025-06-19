import numpy as np

def data_iter(dates,batch_size=24):
    begin = 0
    end = batch_size
    while begin<len(dates):
        yield dates[begin:end]
        begin+=batch_size
        end+=batch_size

if __name__ == '__main__':
    a = np.array([[1,2],[1,3]])
    b = np.array([1,2])
    c = np.dot(a,b)
    print(c, c.shape)
    c = np.dot(b,a)
    print(c, c.shape)