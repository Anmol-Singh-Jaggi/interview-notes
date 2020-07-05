- The code is not complete and is not runnable.
- I prioritized high-level designing over implementing only a subset of features (cannot do both because of time constraints).

# Strategy for compression:
- Split a file into multiple parts, such that each part is within the specified max file size.
- Lets say `abc.txt` is split into `abc.txt.1`, `abc.txt.2` ....
- For each input file, we create a **metafile** `abc.txt.meta` which contains:
    - The path of the file relative to input directory.
        For example, if file is `/root/data/docs/abc.txt`, and input directory is `/root/data`, then metafile will contain `docs/abc.txt`.
        This is important as while decompressing, we will need to know the directory structure of the original file.
    - The list of part files (`[ 'abc.txt.1', 'abc.txt.2' ... ]`).
    - With these 2 pieces of information, we can completely merge and restore back the original file in its original parent directory structure.
- Finally, we will compress each part file indidually (`abc.txt.1` -> `abc.txt.1.zip`).

# Strategy for decompression:
- Read one of the meta files.
- Make the parent directory structure of the original file.
- Decompress all the part files into the parent directory.
- Merge back the part files into 1.
- Do this for all the meta files.
- The number of meta files will be same as the number of files in the input directory and all its subdirectories.

# Example:
- Input directory:
  - `/file1.txt`
  - `/dir1/file2.txt`
  - `/dir2/dir3/file3.txt`
  - `/dir1/dir4/file4.txt`
- Output directory (will always be flat):
  - `/file1.txt.1.zip`
  - `/file1.txt.2.zip`
  - `/file1.txt.3.zip`
  - `/file1.txt.meta`
  - `/file2.txt.1.zip`
  - `/file2.txt.2.zip`
  - `/file2.txt.meta`
  - `/file3.txt.1.zip`
  - `/file3.txt.2.zip`
  - `/file3.txt.3.zip`
  - `/file3.txt.4.zip`
  - `/file3.txt.meta`
  - `/file4.txt.zip`
  - `/file4.txt.meta`

# Design highlights:
- Concurrent compression and merging.
- Handling large files: Splitting and compression will happen using buffered streams.
- Code can be easily extended to use custom compression algorithms.

# Shortcomings left unaddressed:
- A redundant metafile is being generated to mainly store the parent directory structure of the original file.
- Did not get the time to implement a server.
- A lot of edge cases were left unhandled due to time constraints:
  - What if output directory already has some files ?? (Handle overwrites)
  - The files are being split even before being compressed. This might lead to too many tiny files in the output.
  - What if 2 files have the same name in the input directory?