import random
import data_generator

def getdata():
    Ws=[2,3]
    b=2
    n=128
    data = data_generator.generateData(Ws,b,n)
    return data

def train(data, lr=0.1, epochs=5):
    w_number = len(data[0])-1
    Ws = [random.random() for _ in range(w_number)]
    b = random.random()
    for e in range(epochs):
        for d in data:
            x = d[:-1]
            y_pred = sum(x*Ws)+b
            dis = y_pred - d[-1]
            Ws -= dis * lr * x
            b -= dis * lr
    print(Ws)
    print(b)

if __name__ == '__main__':
    data = getdata()
    train(data)