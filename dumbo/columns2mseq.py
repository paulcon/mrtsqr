#!/usr/bin/env dumbo

"""
Convert a set of "column" mseq files into a matrix mseq.
"""

import sys

class Mapper:
    opts = [('addpath','yes')]

    def __call__(self,key,value):
        # This assumes the column index is a one-digit integer 
        # that occurs immediately before the . in the file name.
        # It also assumes that the first element in the column
        # file is a row index.
        path,_key = key
        ind = path.rfind('.')
        col = path[ind-1]

        # value[0] is the row index, value[1] is the element.
        yield value[0], (col,float(value[1]))

def reducer(key,values):
    values = sorted(values, key=lambda value: value[0])
    row = [float(v[1]) for v in values]
    yield key,row
    
if __name__ == '__main__':
    import dumbo
    import dumbo.lib
    
    dumbo.run(Mapper,reducer)

    
