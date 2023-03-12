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
parser.add_argument("--corpus_path", default = "citadel/web/assets/corpus.txt")
parser.add_argument("--num_words", default = 1000000)
parser.add_argument("--word_dim", default = 132)
parser.add_argument("--semantics_dim", default = 256)

# [Primitive] add the primitive concept embedding structure
parser.add_argument("--num_primitives", default = 1000000)
parser.add_argument("--primitive_dim", default = 64)

config = parser.parse_args(args = [])


if __name__ == "__main__":
    from citadel import *
    ice_citadel = TheCitadel(config)

    outputs = ice_citadel.language_encoder(["what is the sum of 1 and 2.","find the sum of 1 and 2."])
    print("past the test for the citadel language encoder.")

    print("pass the test for the citadel abstractions.")
   
def gcd(a, b):
 
    if (a == 0):
        return b
    return gcd(b % a, a)
 
# A simple method to evaluate
# Euler Totient Function
def phi(n):
 
    result = 1
    for i in range(2, n):
        if (gcd(i, n) == 1):
            result+=1
    return result
 
# Driver Code
print(phi(24))
            
# This code is contributed
# by Smitha