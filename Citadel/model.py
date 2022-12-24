import torch
import torch.nn as nn

import torch.nn.functional as F

import numpy as np

import matplotlib.pyplot as plt

class TheCitadel(nn.Module):
    def __init__(self,config):
        super().__init__()

    def forward(self,x):
        return "My son, the day you were born, the very forests of Lordaeron whispered the name Arthas.\
                My child, I watched with pride as you grew into a weapon of righteousness.\
                Remember, our line has always ruled with wisdom and strength. And I know you will show restraint when exercising your great power.\
                But the truest victory, my son, is stirring the hearts of your people. I tell you this, for when my days have come to an end, you shall be King." + x