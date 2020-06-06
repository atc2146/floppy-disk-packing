# Summary
  
An implementation of the Bin Packing (Offline) Algorithm as applied to optimizing Floppy Disk memory distribution.

## Problem Statement

`You have an arbitrary number of files, each less than 1.44MB. The files total 128MB and you have 120 floppy disks available.  Each floppy disk has a capacity of 1.44MB. Find the optimal distribution of files to floppy disks.`

## Methodology
A [First Fit Decreasing Algorithm](Algos.py) was implemented to solve this problem.  It runs in O(n<sup>2</sup>) time.  Given the small data set, this is sufficient.  A more complex (and faster) way of implementing the First Fit Decreasing Algorithm can be done using self balancing trees with a runtime of O(nlogn).

## Data
  
Data is self-generated via the [FloppyData.py](FloppyData.py) file 

## How to run

Requires no third party libraries.
Simply [clone](https://github.com/atc2146/floppy-disk-packing.git) this repo, shell into the folder, and run [Main.py](Main.py)

```sh
$ python Main.py
```

## Commentary
Further optimizations may include using a Modified First Fit Decreasing Algorithm (see Wikipedia page) to decrease, on average, the number of floppy disks required.  

## Resources/Sources

 * Wikipedia: https://en.wikipedia.org/wiki/Bin_packing_problem
 * Google Dev: https://developers.google.com/optimization/bin/bin_packing
 * UCSB: https://sites.cs.ucsb.edu/~suri/cs130b/BinPacking
 * Geeksforgeeks: https://www.geeksforgeeks.org/bin-packing-problem-minimize-number-of-used-bins/
 * Wikipedia: https://en.wikipedia.org/wiki/Megabyte

## Author
Alex Chung
