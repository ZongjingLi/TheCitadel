import torch
import torch.nn as nn
import torch.nn.functional as F

import matplotlib.pyplot as plt
import numpy as np
import time

from .programRecognition import *
from icc.reflection import *
import gc

class TheCitadel(nn.Module):
    def __init__(self,config):
        super().__init__()
        self.config = config
        self.concept_dim = config.concept_dim
        self.language_encoder = None
        self.program_search = NeuroHeurisicSearch(config)

    def solution_abstraction(self, programs = None):
        if programs == None:
            programs = [
                ("(+. 1. 1.)",None),
                ("(*. (+. 1. 1.) pi)",None),
                ("(+. (*. (+. 1. 1.) pi) 1.)",None),
                ("(+. (*. (+. 1. 1.) pi) 0.)",None),
                ("(+. (*. (+. 1. 1.) pi) (*. (+. 1. 1.) pi))",None),
                ("(+. (*. (+. 1. 1.) pi) (*. (+. 1. 1.) pi))",None),
            ] 
        programs = [(Program.parse(p),t) for p,t in programs ]
        arity = self.config.arity

        v = VersionTable(typed=False, identity=False) # create the version table
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


        candidate = bestNew
        new_name = next(v.extract(candidate))
        return new_name

    def search_timeout(self, secs = 2):
        timeout = time.time() + secs 
        while True:
            if  time.time() > timeout:
                break

    def forward(self,x):
        timeout = time.time() + 2   # 5 minutes from now
        while True:
            if  time.time() > timeout:
                break
        
        return "My son, the day you were born, the very forests of Lordaeron whispered the name Arthas.\
                My child, I watched with pride as you grew into a weapon of righteousness.\
                Remember, our line has always ruled with wisdom and strength. And I know you will show restraint when exercising your great power.\
                But the truest victory, my son, is stirring the hearts of your people. I tell you this, for when my days have come to an end, you shall be King." + x


