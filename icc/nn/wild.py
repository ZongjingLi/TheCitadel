import torch
import torch.nn as nn

import torch.nn.functional as F

import scipy 

class ParticleFilter(nn.Module):
    def __init__(self, world_size = 50):
        super().__init__()
        self.world_size = world_size
        self.particles = None
    
    def forward(self,x):
        return x
    
    def upate_particle(self):
        return