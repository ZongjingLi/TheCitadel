import torch
import torch.nn as nn
import torch.nn.functional as F

import eel

from config  import *
from citadel import *

import json
import time

citadel_model = TheCitadelInterface(config)
if config.load_ckpt:citadel_model = torch.load(config.ckpt_path)
else:print("failed to load the citadel")

# load the reserved words for the citadel response
with open(config.reserved_path) as file:
    reserved_keywords = json.load(file)


@eel.expose 
def get_icc_respond(text):
    time.sleep(0.5)
    if text in reserved_keywords:
        return reserved_keywords[text]
    else:return citadel_model(text)
