class Vector_shuffle_set:
    def __init__(self,mux,increment,module):
        self.mux=mux
        self.increment=increment
        self.module=module
        self.mux=1664525
        self.increment=1013904223
        self.module=2**32
        vector=[]

    def lcg(self,lenght,seed):
        for i in range(self,lenght):
            seed=(self.mux*seed+increment)%module
            vector.append(seed)
        return  vector

    def run_lcg(self,vector_len,initial_seed):
        self.vector_len=vector_len
        self.initial_seed=initial_seed
