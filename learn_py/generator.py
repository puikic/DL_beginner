from chap1_NN import data_generator
def data_iter(dates, batch_size=24):
    begin = 0
    end = batch_size
    while begin < len(dates):
        yield dates[begin:end]
        begin += batch_size
        end += batch_size

if __name__ == '__main__':
    data = data_generator.generateData([2,3], n=10)
    print(data)
    print('=================')
    for d in data_iter(data, batch_size=3):
        print(d)
        print('================')