import torch
import torch.nn as nn

from citadel import *
from citadel.models.icecrown_citadel import IceCrownCitadel
from config import *

def train(model, config, args):
    pass


argparser = argparse.ArgumentParser()

argparser.add_argument("--name",                default = "ICC")
argparser.add_argument("--pretrain_checkpoint", default = False)

args = argparser.parse_args()


if args.pretrain_checkpoint:
    model = torch.load(args.pretrain_checkpoint, map_location=config.device)
else:
    model = IceCrownCitadel(config)

print(model)