import torch
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name",default = "The Citadel")
parser.add_argument("--load_ckpt",default = False)
parser.add_argument("--ckpt_path",default = "Citadel/checkpoints/icc.ckpt")
parser.add_argument("--reserved_path",default = "Citadel/reserved.json")
parser.add_argument("--concept_dim",default = 100)
config = parser.parse_args(args = [])
