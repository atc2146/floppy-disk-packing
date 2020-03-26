# Floppy Disk Optimization
  
An implmentation of the Bin Packing (Offline) Algorithm as applied to optimizing Floppy Disk memory distribution.

Problem statement (summary):  
 * You have an aribitrary amount of files, each less than 1.44MB. The files total 128MB and you have 120 floppy disks.  Each floppy disk has a capacity of 1.44MB. Find the optimal distribution of files to floppy disks.

## Methodology and Summary
A First Fit Decreasing Algorithm was implemented to solve this problem.  It runs in O(n^2) time.  Given the small data set, this is sufficient.  A more complex (and faster) way of implmenting the First Fit Decreasing Algorithm can be done using self balancing tress with a runtime of O(nlogn).

## Data
  
Data is self-generated via the FloppyData.py file 

## Commentary
Further optimzations may include using a Modified First Fit Decreasing Algorithm (see Wikipedia page) to decrease, on average, the number of Floppy Disks required.

## How to run

Requires no third party libraries.
Simply clone this repo, shell into the folder, and run Main.py

```sh
$ python Main.py
```

## Resources/Sources

 * Wikipedia: https://en.wikipedia.org/wiki/Bin_packing_problem
 * Google Dev: https://developers.google.com/optimization/bin/bin_packing
 * UCSB: https://sites.cs.ucsb.edu/~suri/cs130b/BinPacking
 * Geeksforgeeks: https://www.geeksforgeeks.org/bin-packing-problem-minimize-number-of-used-bins/
 * https://en.wikipedia.org/wiki/Megabyte

## Author
Alex Chung
