import numpy as np
import matplotlib.pyplot as plt

import torch
import torch.nn as nn
import torch.nn.functional as F

import eel

from config  import *
from Citadel import *

citadel_model = TheCitadel(config)

@eel.expose
def test_str():
    x = torch.randn([1,2])
    res = str(x.detach().numpy()[0][0])
    return "ACTUAL ANSWER: " + str(res)

@eel.expose
def test_network(input_sent):
    print(input_sent)
    return "this is the output"

@eel.expose 
def get_respond(text):
    results = citadel_model(text)
    print(results)
    return results