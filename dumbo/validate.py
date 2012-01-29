#!/usr/bin/env dumbo

"""
Writes a subset of columns.
"""

def mapper(key,value):
    yield len(value),1

def reducer(key,values):
    yield key,sum(values)
    
if __name__ == '__main__':
    import dumbo
    dumbo.run(mapper,reducer)
