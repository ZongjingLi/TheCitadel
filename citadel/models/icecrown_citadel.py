from .language import *

import torch
import torch.nn as nn


class IceCrownCitadel(nn.Module):
    def __init__(self, config):
        super().__init__()

        self.config = config

    def forward(self,x):

        return x

    def __str__(self):return "Ice Crown Citadel"