import java.io.IOException;
import java.io.RandomAccessFile;
import java.nio.channels.FileChannel;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;

public class FileSplitter {
    /**
     * Split the files into parts of max size. Write them to output directory.
     * 
     * @param inputFile
     * @param maxSize
     * @param outputDir
     * @return
     * @throws IOException
     */
    public List<Path> splitFile(Path inputFile, int maxSize, Path outputDir) throws IOException {
        // Should not split if input file is already small enough.
        List<Path> splitFiles = new ArrayList<>();
        final long sourceSize = Files.size(inputFile);
        final long bytesPerSplit = 1024L * 1024L * maxSize;
        final long numSplitsTotal = sourceSize / bytesPerSplit;
        final long remainingBytes = sourceSize % bytesPerSplit;
        long numSplit = 0;

        try (RandomAccessFile sourceFile = new RandomAccessFile(inputFile.toAbsolutePath().toString(), "r");
                FileChannel sourceChannel = sourceFile.getChannel()) {
            while (numSplit < numSplitsTotal) {
                writePartToFile(inputFile, outputDir, bytesPerSplit, numSplit * bytesPerSplit, sourceChannel,
                        splitFiles);
                numSplit++;
            }
            if (remainingBytes > 0) {
                writePartToFile(inputFile, outputDir, remainingBytes, numSplit * bytesPerSplit, sourceChannel,
                        splitFiles);
            }
        }
        return splitFiles;
    }

    private void writePartToFile(Path inputFile, Path outputDir, long byteSize, long numSplit,
            FileChannel sourceChannel, List<Path> splitFiles) throws IOException {
        Path splitFile = outputDir.resolve(inputFile.getFileName().toString() + "." + Long.toString(numSplit));
        try (RandomAccessFile toFile = new RandomAccessFile(splitFile.toFile(), "rw");
                FileChannel toChannel = toFile.getChannel()) {
            sourceChannel.position(numSplit);
            toChannel.transferFrom(sourceChannel, 0, byteSize);
        }
        splitFiles.add(splitFile);
    }

    public void createMetaFile(Path inputFile, Path outputDir, List<Path> splitFiles) {
        StringBuilder metadata = new StringBuilder();
        // Write the complete input file path.
        metadata.append(inputFile.toAbsolutePath().toString());
        for (Path splitFile : splitFiles) {
            // Write the split file names.
            metadata.append(splitFile.toAbsolutePath().toString());
        }
        Path metaFile = outputDir.resolve(inputFile.getFileName()) + ".meta";
        Files.write(metaFile, metadata.toString().getBytes());
    }
}