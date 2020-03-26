from FloppyData import FloppyData
from Algos import first_fit_algo
from Algos import bin_to_list

data = FloppyData(1.44, 128).get_data()
floppy_disks = bin_to_list(first_fit_algo(data, 1.44))

for i in range(0, len(floppy_disks)):
    print("Floppy Disk " + str(i) + ": " + str([round(elem,3) for elem in floppy_disks[i]]))

if (i<120):
    print("Floppy Disks from " + str(i+1) + " to 120 are empty")   
