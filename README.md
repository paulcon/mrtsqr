MRTSQR: Tall-and-skinny QR in MapReduce
======

### David F. Gleich
### Paul G. Constantine

The QR factorization is a standard matrix factorization used to solve
many problems.  Probably the most famous is linear regression:

    minimize || Ax - b ||,

where _A_ is an _m-by-n_ matrix, and _b_ is an _m-by-1_ vector.
When the number of rows of the matrix _A_ is much larger than
the number of columns, then _A_ is called a _tall-and-skinny_
matrix because of its shape.  

The MrTSQR codes implement a routine to compute a QR factorization
of a tall-and-skinny matrix using Hadoop's implementation of the
MapReduce computational platform.  The underlying
algorithm for this implementation is due to Demmel et al. .

The codes are written in Python, and use the NumPy library
for the numerical routines.  This introduces a mild-ineffiency
into the code, which we explore by studying three different 
packages to use Hadoop with Python: dumbo, pydoop, and hadoopy.

This package describes the code and experiments used in our 
paper: A tall-and-skinny QR factorization in MapReduce.

Synopsis
--------

Here, we detail the minimum possible steps required to get things
working.

### Setup

Ideally, there would be no setup.  However, to make things easier
at other stages, there are a few things you must do.

### Assumptions

* dumbo is installed and working
* numpy is installed and working
* hadoop is installed and working

### Example

    # Load all the paths.  You should update this for your setup.
    # This example only needs HADOOP_INSTALL set
    source setup_env.sh
    
    # Move a matrix into HDFS, properly formatted for our tools
    hadoop fs -mkdir tsqr
    hadoop fs -copyFromLocal data/verytiny.tmat tsqr/verytiny.tmat
    dumbo start dumbo/matrix2seqfile.py \
        -hadoop $HADOOP_INSTALL \
        -input tsqr/verytiny.tmat -output tsqr/verytiny.mseq
    
    # Look at the matrix in HDFS
    dumbo cat tsqr/verytiny.mseq -hadoop $HADOOP_INSTALL
        
    #    
    # Compute it's QR factorization
    #
    
    dumbo start dumbo/tsqr.py -mat tsqr/verytiny.tmat -use_system_numpy
    
    # The -use_system_numpy option tells tsqr.py to 
    # use the numpy on the system.  On my cluster, the
    # compute nodes don't have numpy installed, so I ship
    # an egg with the streaming job to give them numpy.
    
    #
    # Look at the R in the QR
    #
    
    dumbo cat tsqr/verytiny-qrr.mseq -hadoop $HADOOP_INSTALL

Overview
--------

* `dumbo/tsqr.py` - the tsqr function for dumbo
* `hadoopy/tsqr.py` - the tsqr code for hadoopy
* `cxx/tsqr.cc` - the tsqr code using C++
* `cxx/typedbytes.h` - the header file for the C++ typedbytes library
* `java/org.../FixedLengthRecordReader.java` - a record reader based on
  MapReduce 1176 Jira
* `experiments/tinyimages/ti_regress.py` - Code for least-squares regression
  using a TSQR  

Figures and Tables
-------------------

* `experiments/framework` - Table 2
* `experiments/blocksize` - Table 3
* `experiments/splitsize` - Table 4
* `experiments/tinyimages` - Regression Side-fig and Figure 5
* - Main file: `ti_pca.py` and `ti_regress.py`
* - Extraction files: `pca_svd.py` and `regression_output.py`
* - Plotting files: `plot_pc.m` and `plot_regress.m`


