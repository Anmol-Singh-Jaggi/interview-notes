import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.DirectoryStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.FutureTask;
import java.util.concurrent.RunnableFuture;
import java.util.function.Supplier;

public class DirectoryCompressor {
    private final Path inputDir;
    private final Path outputDir;
    private final int numThreads = 16;
    private final ExecutorService executorService = Executors.newFixedThreadPool(numThreads);

    public DirectoryCompressor(String inputDirPathString, String outputDirPathString, int maxSize) {
        this.inputDirPath = new Path(inputDirPathString);
        this.outputDirPath = new Path(outputDirPathString);

        if (Files.notExists(inputDirPath)) {
            String logMsg = String.format("The input directory '%' does not exists!", inputDirPath);
            throw new FileNotFoundException(logMsg);
        }
        if (Files.notExists(outputDirPath)) {
            String logMsg = String.format("The output directory '%' does not exists!", outputDirPath);
            throw new FileNotFoundException(logMsg);
        }
    }

    /**
     * Gets all the files in a directory and children subdirectories, and populates
     * the input list with them.
     * 
     * @param files    The list which will be populated.
     * @param inputDir The directory.
     */

    private void getAllFilesInDirectory(List<Path> files) {
        try (DirectoryStream<Path> stream = Files.newDirectoryStream(inputDir)) {
            for (Path path : stream) {
                if (path.toFile().isDirectory()) {
                    getAllFilesInDirectory(files);
                } else {
                    files.add(path);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private Boolean compressFiles(List<Path> files) {
        // Compress one file in another thread.
        List<RunnableFuture<Void>> futures = new ArrayList<>();
        for (Path file : files) {
            CompressFileTask task = new CompressFileTask(file, outputDir);
            RunnableFuture<Void> taskFuture = new FutureTask<>(task, null);
            futures.add(taskFuture);
            executorService.submit(taskFuture);
        }
        // Wait for all threads to finish.
        for (RunnableFuture<Void> future : futures) {
            future.get();
        }
        return true;
    }

    public void compressDirectory() {
        // TODO: - Handle output path files overwrite (if files exist there already).

        List<Path> inputDirFiles = new ArrayList<>();
        List<CompletableFuture<Void>> futures = new ArrayList<>();
        getAllFilesInDirectory(inputDirFiles);
        for (Path filePath : inputDirFiles) {
            // Allocate one thread for splitting followed by compressing.
            Supplier<List<Path>> supplierOfSplitPaths = new FileSplitSupplier<>(inputFile, outputDir, maxSize);
            CompletableFuture<Void> future = CompletableFuture.supplyAsync(supplierOfSplitPaths, executorService)
                    .thenApply((splitFiles) -> compressFiles(splitFiles));
            futures.add(future);
        }
        // Wait for all tasks/threads to finish.
        for (CompletableFuture<Void> future : futures) {
            future.get();
        }
    }
}

class FileSplitSupplier implements Supplier<List<Path>> {
    private final Path inputFile;
    private final Path outputDir;
    private final int maxSize;

    public FileSplitSupplier(Path inputFile, Path outputDir, int maxSize) {
        this.inputFile = inputFile;
        this.outputDir = outputDir;
        this.maxSize = maxSize;
    }

    @Override
    public List<Path> get() {
        // Split into multiple smaller files.
        List<Path> splitFiles = fileSplitter.splitFile(inputFile, maxSize, outputDir);
        // Create a meta file.
        fileSplitter.createMetaFile(inputFile, outputDir, splitFiles);
        return splitFiles;
    }
}

class CompressFileTask implements Runnable {
    private final Path file;
    private final Path outputDir;
    private final FileCompressor compressor = new FileCompressor();

    public CompressFileTask(Path file, Path outputDir) {
        this.file = file;
        this.outputDir = outputDir;
    }

    @Override
    public void run() {
        compressor.compressFile(file, outputDir);
    }

}