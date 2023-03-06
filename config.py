import torch
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name",default = "The Citadel")
parser.add_argument("--load_ckpt",default = False)
parser.add_argument("--ckpt_path",default = "Citadel/checkpoints/icc.ckpt")
parser.add_argument("--reserved_path",default = "Citadel/reserved.json")

# [Neuro-Symbolic] add the neuro symbolic config (not implemented yet)
parser.add_argument("--concept_dim",default = 100)

# [Abstract] add the program abstraction config
parser.add_argument("--arity",default = 3)

# [Language] add the config of the language encoder
parser.add_argument("--num_words",default = 1e6)
parser.add_argument("--word_dim",default = 132)

# [Primitive] add the primitive concept embedding structure
parser.add_argument("--num_primitives",default = 1e6)
parser.add_argument("--primitive_dim",default = 64)

config = parser.parse_args(args = [])
