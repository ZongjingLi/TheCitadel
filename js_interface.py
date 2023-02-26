import numpy as np
import matplotlib.pyplot as plt

import torch
import torch.nn as nn
import torch.nn.functional as F

import eel

from config  import *
from Citadel import *

import json

citadel_model = TheCitadel(config)
if config.load_ckpt:citadel_model = torch.load(config.ckpt_path)
else:print("failed to load the citadel")

# load the reserved words for the citadel response
with open(config.reserved_path) as file:
    reserved_keywords = json.load(file)

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
    if text in reserved_keywords:
        return reserved_keywords[text]
    else:return citadel_model(text)
