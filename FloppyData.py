import random

class FloppyData:
    """
    Class representing data to be stored on a Floppy Disk
    """
    # https://en.wikipedia.org/wiki/Megabyte
    # Assume 1000*1024 bytes in a MB (for consistency)
    CONVERSION_BYTES_IN_1_MB = 1000*1024
    
    def __init__(self, size_of_disk, total_size_of_files):
        """
        @size_of_disk: in MB
        @total_size_of_files: in MB
        """
        self.size_of_disk = size_of_disk
        self.total_size_of_files = total_size_of_files
    
    def get_data(self) -> list:
        """
        Returns a list of file sizes which sum to @total_size_of_files.
        
        Each file is no larger than @size_of_disk.
        """
        file_sizes = []

        while(sum(file_sizes) < self.total_size_of_files*self.CONVERSION_BYTES_IN_1_MB):
            # Generate random integer which represents a file size in bytes
            file_size = random.randint(1, self.CONVERSION_BYTES_IN_1_MB*self.size_of_disk)

            if(sum(file_sizes)+file_size >= self.total_size_of_files*self.CONVERSION_BYTES_IN_1_MB):
                file_size = self.total_size_of_files*self.CONVERSION_BYTES_IN_1_MB-sum(file_sizes)

            file_sizes.append(file_size)
        
        file_sizes_mb = [file/self.CONVERSION_BYTES_IN_1_MB for file in file_sizes]
        
        return file_sizes_mb