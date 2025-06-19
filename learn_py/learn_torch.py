import torch
from torch import nn
r = torch.randn(2,3)
print(r, r.shape,type(r))
print('================================================')
r = torch.randn(3)
x = nn.Parameter(r)
print(x, x.shape,type(x))