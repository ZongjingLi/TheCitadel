import torch
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name",default = "The Citadel")
parser.add_argument("--concept_dim",default = 100)
config = parser.parse_args(args = [])
