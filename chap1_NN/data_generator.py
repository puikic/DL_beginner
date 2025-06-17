import numpy as np

# 该函数生成符合以下线性关系的数据集：
# y = (x₁ * w₁ + x₂ * w₂ + ... + xₖ * wₖ) + b
def generateData(Ws,b=0,n=128):
    '''
    :param Ws: [1,2] 给定包含所有权重w的列表
    :param b: 0.5 偏置项
    :param n: 数据组数量
    :return: 生成的数据组，最后一列是标注。
    '''
    x = np.random.rand(n, len(Ws))
    y = (x*Ws).sum(axis=1)+b
    datas = np.column_stack((x, y))
    datas = datas.astype(np.float32)
    return datas

if __name__=='__main__':
    Ws = [2,3,4]
    data = generateData(Ws)
    print(data,type(data))