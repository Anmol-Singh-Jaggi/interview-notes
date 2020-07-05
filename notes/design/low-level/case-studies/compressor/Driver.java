public class Driver {
    public static void main(String[] args) {
        String inputDirPathString = "d:/data";
        String outputDirPathString = "d:/data";
        int maxSize = 5;
        DirectoryCompressor compressor = new DirectoryCompressor(inputDirPathString, outputDirPathString, maxSize);
        compressor.compressDirectory();
        DirectoryDecompressor decompressor = new DirectoryDecompressor(outputDirPathString, inputDirPathString);
        decompressor.decompressDirectory();
    }
}