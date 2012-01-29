#!/usr/bin/env dumbo

"""
Writes a subset of columns.
"""

class Mapper:
    def __init__(self):
        file = open("indices.txt","r")
        self.indices = set(line.strip() for line in file)
        file.close()

    def __call__(self,key,value):
        w=[0]*len(self.indices)
        for (i,ind) in enumerate(self.indices):
            w[i]=value[int(ind)]
        yield key, w
    
if __name__ == '__main__':
    import dumbo
    import dumbo.lib
    dumbo.run(Mapper,dumbo.lib.identityreducer)
