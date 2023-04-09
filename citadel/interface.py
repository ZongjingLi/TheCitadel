import eel

from config  import *
from citadel import *

import json


citadel_model = TheCitadelInterface(config)
if config.load_ckpt:citadel_model = torch.load(config.ckpt_path)
else:print("failed to load the citadel")

# load the reserved words for the citadel response
with open(config.reserved_path) as file:
    reserved_keywords = json.load(file)


@eel.expose 
def get_icc_respond(text):
    print(text)
    return text
    if text in reserved_keywords:
        return reserved_keywords[text]
    else:return citadel_model(text)

