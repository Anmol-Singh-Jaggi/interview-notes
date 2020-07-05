import java.util.Date;
import java.util.concurrent.CountDownLatch;
import java.util.logging.Level;
import java.util.logging.Logger;

public class CountDownLatchDemo {

    public static void main(String args[]) {
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
            latch.await();
            System.out.println("All services are up, Application is starting now");
        } catch (InterruptedException ie) {
            ie.printStackTrace();
        }

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

    @Override
    public void run() {
        try {
            Thread.sleep(processingTime);
        } catch (InterruptedException ex) {
            Logger.getLogger(Service.class.getName()).log(Level.SEVERE, null, ex);
        }
        System.out.println(name + " is Up");
        latch.countDown();
    }

}