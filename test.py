from icc import *

print(I ** 2)
print(log(E))

print(oo >= 1e9)

print(pi)
print(pi.evalf())

x,y = symbols("x y")

print(diff(cos(x),x))

pf = ParticleFilter(40)

import matplotlib.pyplot as plt

ims = read_image("citadel/web/src/arthas.jpg")

from icc.reflection.domains.arithmetics import *

programs = [
    ("(+. 1. 1.)",None),
    ("(+. 1. (+. 0. 1.))",None),
]

programs = [
                ("(+. 1. 1.)",None),
                ("(*. (+. 1. 1.) pi)",None),
                ("(+. (*. (+. 1. 1.) pi) 1.)",None),
                ("(+. (*. (+. 1. 1.) pi) 0.)",None),
                ("(+. (*. (+. 1. 1.) pi) (*. (+. 1. 1.) pi))",None),
                ("(+. (*. (+. 1. 1.) pi) (*. (+. 1. 1.) pi))",None),
            ] 

programs = [(Program.parse(p),t) for p,t in programs ]

arity = 3
from icc.reflection.version_space import *
import gc

v = VersionTable(typed=False, identity=False)
with timing("constructed %d-step version spaces"%arity):
    versions = [[v.superVersionSpace(v.incorporate(e[0]), arity)] for e in programs]
    eprint("Enumerated %d distinct version spaces"%len(v.expressions))

    topI = 50
    candidates = v.bestInventions(versions, bs=3*topI)[:topI]

    eprint("Only considering the top %d candidates"%len(candidates))

    # Clean caches that are no longer needed
    v.recursiveTable = [None]*len(v)
    v.inhabitantTable = [None]*len(v)
    v.functionInhabitantTable = [None]*len(v)
    v.substitutionTable = {}
    gc.collect()

CPUs = 1
with timing("scored the candidate inventions"):
            scoredCandidates = parallelMap(CPUs,
                                           lambda candidate: \
                                           (candidate, .0),
                                            candidates,
                                           memorySensitive=True,
                                           chunksize=1,
                                           maxtasksperchild=1)

oldScore = 100

if len(scoredCandidates) > 0:
    bestNew, bestScore = max(scoredCandidates, key=lambda sc: sc[1])
if len(scoredCandidates) == 0 or bestScore < oldScore:
            eprint("No improvement possible.")
            # eprint("Runner-up:")
            # eprint(next(v.extract(bestNew)))
            # Return all of the frontiers, which have now been rewritten to use the
            # new fragments

candidate = bestNew
new_name = next(v.extract(candidate))

print(new_name,type(new_name))

print(Primitive.GLOBALS)


Primitive("I", treal, new_name)
print(new_name)


e = Program.parse("(#(lambda (* (+ 1 $0) 4)))")
print(e)
print(e.runWithArguments([3]))

e = Program.parseHumanReadable("(/. 1. 1.)")
print(e)
print(e.f,e.x)
print(e.runWithArguments([]))