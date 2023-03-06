from icc import *
import time

class NeuroHeurisicSearch(nn.Module):
    def __init__(self,config):
        super().__init__()

        self.config = config

    def setup_heustics(self,program,task):
        cost = 1.0
        return cost # return the cost of the program

    def search(time_out = 2):
        # search over the primitive graph start with.
        timeout = time.time() + time_out
        while 1:
            if (time.time() > timeout):
                break
        return "return program"