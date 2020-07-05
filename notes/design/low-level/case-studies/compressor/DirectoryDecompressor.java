import java.io.FileNotFoundException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class DirectoryDecompressor {
    public DirectoryCompressor(String inputDirPathString, String outputDirPathString) {
    
    }

    public decompressDirectory(){
        // Decompress all files and delete the original ones.
        // Read all the meta files one by one.
        // Get the list of files and the parent directory from meta file.
        // Make the parent directory if not exists.
        // Merge the files and write to parent directory.
        // Delete the split files.
        // Do this for all meta files.
        FileCombiner combiner = new FileCombiner();
        //combiner.mergeFiles(metaFilePath);
    }

}