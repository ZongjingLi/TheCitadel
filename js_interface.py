import numpy as np
import matplotlib.pyplot as plt

import torch
import torch.nn as nn
import torch.nn.functional as F

import eel

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(2,1)
    def forward(self,x):
        return self.fc1(x)

net = Net()

@eel.expose              
def test_func(a, b):
    return a+b

@eel.expose
def test_str():
    x = torch.randn([1,2])
    x = net(x)
    res = str(x.detach().numpy()[0][0])
    return "ACTUAL ANSWER: " + str(res)

@eel.expose
def test_network(input_sent):
    print(input_sent)
    return "this is the output"

@eel.expose
def run_model():
    return 0