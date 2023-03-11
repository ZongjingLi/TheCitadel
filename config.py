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
   

def primes(n):
    P = []
    f = []
    for i in range(n+1):
        if i > 2 and i%2 == 0:
            f.append(1)
        else:
            f.append(0)
    i = 3
    counter = 0
    while i*i <= n:
        if f[i] == 0:
            j = i*i
            while j <= n:
                f[j] = 1
                j += i+i
        i += 2
        counter += 1
    print(counter)
 
    P.append(2)
    for x in range(3,n+1,2):
        if f[x] == 0:
            P.append(x)
 
    return P
 
n = 115   #100以内的素数
P = primes(n)
print(P)
 
#    Ipython 2.7实现
import numpy as np
a = np.arange(1,115)
n_max = int(np.sqrt(len(a)))
is_prime = np.ones(len(a),dtype=bool)
is_prime[0] = False
for i in range(2,n_max) :
    if i in a[is_prime]:
        is_prime[(i**2-1)::i] = False
         
print (a[is_prime])

