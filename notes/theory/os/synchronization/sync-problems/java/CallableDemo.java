import java.util.Random;
import java.util.concurrent.Callable;
import java.util.concurrent.FutureTask;

public class CallableDemo {
    public static void main(String[] args) throws Exception {
        // FutureTask is a concrete class that implements both Runnable and Future
        // We can only pass a runnable to a thread!
        // ExecutorService however accepts Callable directly apart from Runnable!
        FutureTask[] tasks = new FutureTask[5];
        for (int i = 0; i < 5; i++) {
            tasks[i] = new FutureTask(new RandGenerator());
            Thread t = new Thread(tasks[i]);
            t.start();
        }

        for (int i = 0; i < 5; i++) {
            // As it implements Future, we can call get()
            System.out.println(tasks[i].get());
        }
    }
}

class RandGenerator implements Callable {
    public Integer call() throws Exception {
        Random generator = new Random();
        Integer randomNumber = generator.nextInt(5);
        // Heavy processing.
        Thread.sleep(randomNumber * 1000);
        return randomNumber;
    }
}