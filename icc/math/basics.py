import torch
import torch.nn as nn

import taichi as ti

class Symbol(nn.Module):
    def __init__(self):
        super().__init__()

class Expression(nn.Module):
    def __init__(self):
        super().__init__()
    
    def parse(self, expr):
        return expr

gui = ti.GUI("math_visualize")

while gui.running:
    gui.show()