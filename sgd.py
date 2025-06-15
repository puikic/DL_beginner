import numpy as np
import matplotlib.pyplot as plt

# 训练数据
x = np.array([1, 2, 3, 4])
y = np.array([2.1, 3.9, 6.0, 8.2])

# 初始化参数
w = np.random.randn()
b = np.random.randn()

# 学习率
lr = 0.01

# 训练轮数
epochs = 100

# SGD训练过程
for epoch in range(epochs):
    for i in range(len(x)):
        # 取单个样本
        xi = x[i]
        yi = y[i]

        # 计算预测值
        y_pred = w * xi + b

        # 计算梯度
        dw = -2 * xi * (yi - y_pred)
        db = -2 * (yi - y_pred)

        # 更新参数
        w -= lr * dw
        b -= lr * db

    # 每10轮输出一次loss
    if epoch % 10 == 0:
        y_preds = w * x + b
        loss = np.mean((y - y_preds) ** 2)
        print(f"Epoch {epoch}: Loss={loss:.4f}, w={w:.4f}, b={b:.4f}")

print(f"\n训练完成：w={w:.4f}, b={b:.4f}")

# 可视化结果
plt.scatter(x, y, color='blue', label='真实数据')
plt.plot(x, w * x + b, color='red', label='拟合线')
plt.legend()
plt.show()