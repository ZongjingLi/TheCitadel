import torch
import torch.nn as nn

class Symbol(nn.Module):
    def __init__(self):
        super().__init__()

class Expression(nn.Module):
    def __init__(self):
        super().__init__()
    
    def parse(self, expr):
        return expr