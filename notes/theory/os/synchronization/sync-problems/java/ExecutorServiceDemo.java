import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

/*
 - FixedThreadPool:
   - Unbounded blocked queue.
   - Threads act like consumers.
 - CachedThreadPool:
   - Queue of size 1.
   - Spawn new thread if all existing are busy.
   - Kill idle threads.
   - Similar to AWS auto scale.
   - https://stackoverflow.com/a/1800583/1925388
*/
public class ExecutorServiceDemo {

    public static void main(String args[]) {
        ExecutorService executor = Executors.newFixedThreadPool(3);
        // ExecutorService executor = Executors.newWorkStealingPool(3);
        // ExecutorService executor = Executors.newSingleThreadExecutor();
        // ExecutorService executor = Executors.newCachedThreadPool();
        // ExecutorService executor = Executors.newScheduledThreadPool(3);
        executor.submit(new Service("CacheService", 1000));
        executor.submit(new Service("AlertService", 1000));
        executor.submit(new Service("ValidationService", 1000));
    }
}

class Service implements Runnable {
    private final String name;
    private final int processingTime;

    public Service(String name, int processingTime) {
        this.name = name;
        this.processingTime = processingTime;
    }

    @Override
    public void run() {
        try {
            Thread.sleep(processingTime);
        } catch (InterruptedException ex) {
            ex.printStackTrace();
        }
        System.out.println(name + " is Up");
    }

}