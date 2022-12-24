import torch
import torch.nn as nn

import torch.nn.functional as F

import numpy as np

import matplotlib.pyplot as plt

class TheCitadel(nn.Module):
    def __init__(self,config):
        super().__init__()

    def forward(self,x):
        return "namo,"+ x 