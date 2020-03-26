from Bin import Bin

def first_fit_algo(files: list, max_size_bin: int, decreasing=True) -> list:
    """
    Implements the First Fit Decreasing Algorithm for Bin Packing Optimization
    
    Runs in O(n^2) time. Can be modified to run in O(nlogn) time.
    
    """
   
    # Toggle between FF/FFD
    if(decreasing):
        list_files = sorted(files, reverse=True)
    else:
        list_files = list(files)
    
    bins = []
    bins.append(Bin())
    
    for file in list_files:
        is_placed = False
        
        for bin in bins:
            if bin.sum() + file <= max_size_bin:
                bin.add(file)
                is_placed = True
                break
        
        if not is_placed:
            # create a new bin, add it to the list of existing bins, and
            # then add that file to the new bin
            b = Bin()
            bins.append(b)
            b.add(file)
            
    return bins
    

def bin_to_list(bins) -> list:
    """
    Function to show the actual bins as lists
    """
    list_show = []
    
    for bin in bins:
        list_show.append(bin.get_items())

    return list_show