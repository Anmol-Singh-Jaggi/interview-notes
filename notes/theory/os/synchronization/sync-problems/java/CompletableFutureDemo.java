import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.function.Function;
import java.util.function.Supplier;

public class CompletableFutureDemo {
    public static void main(String[] args) throws Exception {
        CompletableFuture<Integer> f = CompletableFuture.supplyAsync(new MySupplier()).thenApply(new PlusOne());
        System.out.println(f.get()); // Waits until the "calculation" is done, then prints 2
    }
}

class MySupplier implements Supplier<Integer> {
    @Override
    public Integer get() {
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            // Do nothing
        }
        return 1;
    }
}

class PlusOne implements Function<Integer, Integer> {
    @Override
    public Integer apply(Integer x) {
        return x + 1;
    }

}