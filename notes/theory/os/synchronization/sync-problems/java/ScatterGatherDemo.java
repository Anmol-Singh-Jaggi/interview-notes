import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.concurrent.TimeUnit;
import java.util.logging.Level;

public class ScatterGatherDemo {

    private static void scatterGatherLatch() {
        final CountDownLatch latch = new CountDownLatch(3);
        Thread cacheService = new Thread(new Service("CacheService", 1000, latch));
        Thread alertService = new Thread(new Service("AlertService", 1000, latch));
        Thread validationService = new Thread(new Service("ValidationService", 1000, latch));

        cacheService.start();
        alertService.start();
        validationService.start();

        try {
            // Will block until latch reaches the value 0.
            System.out.println("Waiting...");
            boolean done = latch.await(1, TimeUnit.SECONDS);
            if (done) {
                System.out.println("All services are up, Application is starting now");
            } else {
                System.out.println("Timeout!");
            }
        } catch (InterruptedException ie) {
            ie.printStackTrace();
        }
    }

    private static void scatterGatherAwaitTermination() {
        ExecutorService executor = Executors.newFixedThreadPool(3);
        executor.submit(new Service("CacheService", 1000));
        executor.submit(new Service("AlertService", 1000));
        executor.submit(new Service("ValidationService", 1000));
        try {
            System.out.println("Waiting...");
            boolean done = executor.awaitTermination(1, TimeUnit.SECONDS);
            if (done) {
                System.out.println("All services are up, Application is starting now");
            } else {
                System.out.println("Timeout!");
            }
        } catch (InterruptedException ie) {
            ie.printStackTrace();
        }
    }

    private static void scatterGatherCompletableFuture() {
        ExecutorService executor = Executors.newFixedThreadPool(3);
        List<CompletableFuture<?>> futures = new ArrayList<>();
        futures.add(CompletableFuture.runAsync(new Service("CacheService", 1000), executor));
        futures.add(CompletableFuture.runAsync(new Service("AlertService", 1000), executor));
        futures.add(CompletableFuture.runAsync(new Service("ValidationService", 1000), executor));
        try {
            System.out.println("Waiting...");
            CompletableFuture.allOf(futures.toArray(new CompletableFuture[futures.size()])).get(1, TimeUnit.SECONDS);
            System.out.println("All services are up, Application is starting now");
        } catch (Exception ie) {
            ie.printStackTrace();
        }
    }

    public static void main(String args[]) {
        // Distribute tasks and collect them with timeout.
        // 3 methods:

        // scatterGatherLatch();
        // scatterGatherAwaitTermination();
        scatterGatherCompletableFuture();
    }
}

class Service implements Runnable {
    private final String name;
    private final int processingTime;
    private final CountDownLatch latch;

    public Service(String name, int processingTime, CountDownLatch latch) {
        this.name = name;
        this.processingTime = processingTime;
        this.latch = latch;
    }

    public Service(String name, int processingTime) {
        this(name, processingTime, null);
    }

    @Override
    public void run() {
        try {
            Thread.sleep(processingTime);
        } catch (InterruptedException ex) {
            ex.printStackTrace();
        }
        System.out.println(name + " is Up");
        if (latch != null) {
            latch.countDown();
        }
    }

}